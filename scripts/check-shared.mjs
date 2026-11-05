import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
const root = fileURLToPath(new URL('../src/', import.meta.url));
let count = 0;
function files(dir) {
return fs.readdirSync(dir, { withFileTypes: true }).flatMap(entry => {
const file = path.join(dir, entry.name);
if (entry.isSymbolicLink()) throw new Error(`Unexpected symbolic link: ${file}`);
return entry.isDirectory() ? files(file) : [file];
});
}
for (const file of files(root)) {
const name = path.relative(root, file);
if (!fs.statSync(file).size) throw new Error(`Empty shared file: ${name}`);
if (file.endsWith('.json')) JSON.parse(fs.readFileSync(file, 'utf8'));
if (file.endsWith('.css')) {
const css = fs.readFileSync(file, 'utf8').replace(/\/\*[\s\S]*?\*\//g, '');
for (const match of css.matchAll(/(?:^|[;{}])\s*(line-height|--[\w-]*(?:line-height|leading)[\w-]*|font)\s*:\s*([^;{}]+)/g)) {
const [, property, raw] = match;
const value = raw.replace(/\s*!important\s*$/, '').trim();
if (value === 'inherit' || /^var\(--[\w-]+\)$/.test(value)) continue;
if (property === 'font' || !/^\d*\.?\d+$/.test(value) || Number(value) < 1.5) throw new Error(`Use explicit font properties and unitless line-height >= 1.5: ${name}: ${value}`);
}
for (const match of css.matchAll(/url\(\s*["']?([^\s"')]+)["']?\s*\)/g)) {
const ref = match[1];
if (/^(?:data:|https?:|\/|#)/.test(ref)) continue;
if (!fs.existsSync(path.resolve(path.dirname(file), ref))) throw new Error(`Missing CSS asset: ${name}: ${ref}`);
}
}
if (file.endsWith('.njk')) {
const template = fs.readFileSync(file, 'utf8');
for (const match of template.matchAll(/{%\s*(?:include|extends|from|import)\s+["']([^"']+)["']\s*(?:%}|-%}|import|as)/g)) {
const ref = match[1];
if (![path.join(root, 'includes', ref), path.join(root, ref)].some(p => fs.existsSync(p))) throw new Error(`Missing include: ${name}: ${ref}`);
}
}
count++;
}
for (const ref of ['css/common.css', 'css/footer.css', 'data/uh/header.json', 'data/uh/footer.json', 'data/uh/languages.json', 'includes/base.njk', 'includes/layouts/branding/footer/footer.njk', 'media/icons/chevron-right.svg']) {
if (!fs.existsSync(path.join(root, ref))) throw new Error(`Missing shared file: ${ref}`);
}
for (const old of ['_includes', '_data', '_media']) {
if (fs.existsSync(path.join(root, old))) throw new Error(`Retired source directory: ${old}`);
}
console.log(`Checked ${count} shared files: JSON, source CSS assets, literal include references, structure and line-height rules.`);

// Unit identity/contact data is independent of optional social accounts.
const unitsDirectory = path.join(root, 'data/units');
const seenNames = new Set();
let unitsChecked = 0;
for (const entry of fs.readdirSync(unitsDirectory, { withFileTypes: true })) {
if (!entry.isDirectory()) continue;
const unitDirectory = path.join(unitsDirectory, entry.name);
const siteFile = path.join(unitDirectory, 'unit-details.json');
if (!fs.existsSync(siteFile)) continue;
const site = JSON.parse(fs.readFileSync(siteFile, 'utf8'));
const fail = message => { throw new Error(`${entry.name}/unit-details.json: ${message}`); };
if (!site.name || !site.shortName || seenNames.has(site.name)) fail('Name and abbreviation are required; unit names must be unique.');
seenNames.add(site.name);
if (!Array.isArray(site.address) || !site.address.length || site.address.some(line => typeof line !== 'string' || !line.trim())) fail('Address must contain nonempty lines.');
if (!site.phone?.label || !/^tel:\+\d{7,15}$/.test(site.phone.href)) fail('Phone requires a label and international tel: href.');
if (!site.email?.label || !site.email.href?.startsWith('mailto:' + site.email.label)) fail('Email requires a matching label and mailto: href.');
const logo = site.logo?.variants?.whiteHorz;
if (!logo?.src?.startsWith('/media/branding/logos/') || !site.logo.alt || !(logo.width > 0 && logo.height > 0)) fail('Logo requires a shared path, alt text, and positive dimensions.');
const logoFile = path.join(root, logo.src.slice(1));
if (!fs.existsSync(logoFile)) fail('Logo file is missing.');
const viewBox = fs.readFileSync(logoFile, 'utf8').match(/viewBox=["']([^"']+)["']/);
if (!viewBox) fail('Logo must retain a viewBox.');
const values = viewBox[1].trim().split(/[\s,]+/).map(Number);
if (values.length !== 4 || Math.abs(values[2] / values[3] - logo.width / logo.height) > 0.00001) fail('Logo dimensions must preserve its viewBox proportions.');
for (const [variant, record] of Object.entries(site.logo.variants)) {
if (!['whiteHorz', 'whiteVert', 'color'].includes(variant) || !record.src?.startsWith('/media/branding/logos/') || !(record.width > 0 && record.height > 0)) fail('Invalid logo variant record.');
const file = path.join(root, record.src.slice(1));
if (!fs.existsSync(file)) fail(`Missing ${variant} logo.`);
const viewBox = fs.readFileSync(file, 'utf8').match(/viewBox=["']([^"']+)["']/);
const box = viewBox?.[1].trim().split(/[\s,]+/).map(Number);
if (!box || box.length !== 4 || Math.abs(box[2] / box[3] - record.width / record.height) > 0.00001) fail(`Invalid ${variant} logo proportions.`);
}
if ('socialLinks' in site || 'bluesky' in site) fail('Move social accounts and feed settings into social.json.');
const socialFile = path.join(unitDirectory, 'social.json');
if (fs.existsSync(socialFile)) {
const social = JSON.parse(fs.readFileSync(socialFile, 'utf8'));
if (!Array.isArray(social.links)) fail('social.json links must be an array.');
for (const link of social.links) {
if (!link.label || !/^https?:\/\//.test(link.url)) fail('Social links require labels and web URLs.');
if (link.icon && !fs.existsSync(path.join(root, 'media/icons', link.icon + '.svg'))) fail(`Social icon missing: ${link.icon}`);
}
if (social.bluesky?.enabled && !social.bluesky.actor) fail('Enabled Bluesky feed requires an actor.');
}
unitsChecked++;
}
console.log(`Checked ${unitsChecked} unit contact/logo records and optional social data.`);

const commonLinks = JSON.parse(fs.readFileSync(path.join(root, 'data/common/links.json'), 'utf8'));
for (const [key, link] of Object.entries(commonLinks)) if (!link.label || !/^https:\/\//.test(link.url)) throw new Error(`Invalid common link: ${key}`);
const palette = new Set(['blue', 'gold', 'teal', 'purple', 'gray']);
for (const entry of fs.readdirSync(unitsDirectory, { withFileTypes: true })) {
if (!entry.isDirectory()) continue;
const dir = path.join(unitsDirectory, entry.name);
if (fs.existsSync(path.join(dir, 'site.json'))) throw new Error(`Retired data file: ${entry.name}/site.json`);
const navFile = path.join(dir, 'navigation.json');
function checkNav(items) {
for (const item of items) {
if (!item.label || (!item.url && !item.children)) throw new Error('Navigation requires label and destination or children.');
if (item.icon && !fs.existsSync(path.join(root, 'media/icons', item.icon + '.svg'))) throw new Error(`Unknown navigation icon: ${item.icon}`);
if (item.iconColor && !palette.has(item.iconColor)) throw new Error(`Unknown navigation color: ${item.iconColor}`);
if (item.children) checkNav(item.children);
}
}
if (fs.existsSync(navFile)) checkNav(JSON.parse(fs.readFileSync(navFile, 'utf8')));
for (const filename of ['faculty.json', 'staff.json', 'graduate-students.json']) {
const file = path.join(dir, filename);
if (!fs.existsSync(file)) continue;
const people = JSON.parse(fs.readFileSync(file, 'utf8'));
const slugs = new Set();
for (const person of people) {
if (!person.name || !person.lastName || !person.slug || slugs.has(person.slug)) throw new Error(`Invalid/duplicate person in ${entry.name}/${filename}`);
slugs.add(person.slug);
}
}
}
console.log('Checked common links, navigation icons/colors, and people records.');
