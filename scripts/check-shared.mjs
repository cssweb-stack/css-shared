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
const sourceFiles = files(root);
// Component variables may be declared in CSS or supplied by shared templates/data.
// An explicit var() fallback is allowed; a missing required token is an error.
const tokenSources = sourceFiles.filter(file => /\.(css|njk|json|html)$/.test(file) && !file.includes('/_uh-reference/'));
const definedTokens = new Set(tokenSources.flatMap(file => [...fs.readFileSync(file, 'utf8').replace(/\/\*[\s\S]*?\*\//g, '').matchAll(/(--[\w-]+)\s*:/g)].map(match => match[1])));
for (const file of sourceFiles) {
const name = path.relative(root, file);
if (!fs.statSync(file).size) throw new Error(`Empty shared file: ${name}`);
if (file.endsWith('.json')) JSON.parse(fs.readFileSync(file, 'utf8'));
// Captured third-party reference CSS is not part of our authored/published styles.
if (file.endsWith('.css') && !name.startsWith('css/_uh-reference/')) {
const css = fs.readFileSync(file, 'utf8').replace(/\/\*[\s\S]*?\*\//g, '');
// Enforce component ownership before styles reach consuming sites.
for (const [, selector, body] of css.matchAll(/([^{}]+)\{([^{}]*)\}/g)) {
if (/\.(?:profile-[\w-]+|faculty-portrait-grid|program-directors-grid|program-office-photo|office-card|unit-contact(?:-[\w-]+)?|map-embed|contact-address|contact-links|advisor-name)\b/.test(selector) && name !== 'css/profile.css' && name !== 'css/diagnostics.css' && !(name === 'css/sidebar.css' && selector.trim() === '.site-main .sidebar-group > .contact-address')) throw new Error(`Profile styles belong in profile.css: ${name}: ${selector.trim()}`);
if (/\.(?:graduate-student(?:-[\w-]+)?|student-photo-column|student-details-column)\b/.test(selector) && name !== 'css/graduate-students.css' && name !== 'css/diagnostics.css') throw new Error(`Graduate-student styles belong in graduate-students.css: ${name}`);
if (name === 'css/profile.css' && /\.sidebar-group\b/.test(selector)) throw new Error('Generic sidebar rules belong in sidebar.css.');
if (name === 'css/layout.css' && /(?:^|;)\s*(?:font(?:-[\w-]+)?|color|text-align|text-shadow|background(?:-[\w-]+)?|border(?:-[\w-]+)?|box-shadow|outline(?:-[\w-]+)?)\s*:/.test(body)) throw new Error('layout.css is structural only.');
if (name === 'css/typography.css' && /\.(?:unit-|profile-|sidebar-|office-|map-|graduate-|student-)/.test(selector)) throw new Error('typography.css is foundational only.');
}
// Font-face ranges describe supported glyph weights, not applied typography.
let appliedTypography = css.replace(/@font-face\s*\{[^}]*\}/g, '');
// Explicit graphic exceptions only; ordinary footer/404 copy still has the cap.
const graphicException = {
'css/footer.css': ['.site-footer .footer-unit-short-name', '800'],
'css/not-found.css': ['.site-main .not-found-code', '900']
}[name];
if (graphicException) appliedTypography = appliedTypography.replace(/([^{}]+)\{([^{}]*)\}/g, (block, selector, body) => {
if (selector.trim() !== graphicException[0]) return block;
return selector + '{' + body.replace(new RegExp('font-weight\\s*:\\s*' + graphicException[1] + '\\s*;'), '') + '}';
});
for (const [, property, raw] of appliedTypography.matchAll(/(?:^|[;{}])\s*(font-weight|--[\w-]*weight[\w-]*)\s*:\s*([^;{}]+)/g)) {
const value = raw.replace(/\s*!important\s*$/, '').trim();
if (/\b(?:bold|bolder)\b/i.test(value) || [...value.matchAll(/\b\d+(?:\.\d+)?\b/g)].some(m => Number(m[0]) > 600)) throw new Error(`Font weight exceeds the shared maximum 600: ${name}: ${property}: ${value}`);
}
if (/font-variation-settings\s*:/i.test(appliedTypography)) throw new Error(`Use font-weight within the shared 600 maximum, not font-variation-settings: ${name}`);
for (const match of css.matchAll(/var\(\s*(--[\w-]+)\s*\)/g)) {
if (!definedTokens.has(match[1])) throw new Error(`Undefined CSS token without a fallback: ${name}: ${match[1]}`);
}
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
for (const match of template.matchAll(/class="([^"]*)"/g)) {
if (match[1].split(/\s+/).some(name => ['main-content', 'page-section-inner'].includes(name))) throw new Error(`Use content-section for shared content padding: ${name}`);
}
for (const match of template.matchAll(/{%\s*(?:include|extends|from|import)\s+["']([^"']+)["']\s*(?:%}|-%}|import|as)/g)) {
const ref = match[1];
if (![path.join(root, 'includes', ref), path.join(root, ref)].some(p => fs.existsSync(p))) throw new Error(`Missing include: ${name}: ${ref}`);
}
}
count++;
}
// Profile title/role typography has one owner. Reject new competing selectors,
// local shared-CSS overrides, and repeated declarations before they reach sites.
const profileTypographyOwners = new Map([
['.site-main .profile-titles p', 'font-size'],
['.site-main .profile-titles .profile-job-title', 'font-weight'],
['.site-main .profile-titles .profile-admin-title', 'font-weight']
]);
const seenProfileTypography = new Set();
for (const file of sourceFiles.filter(file => file.endsWith('.css') && !file.includes('/_uh-reference/'))) {
const css = fs.readFileSync(file, 'utf8').replace(/\/\*[\s\S]*?\*\//g, '');
for (const [, rawSelector, body] of css.matchAll(/([^{}]+)\{([^{}]*)\}/g)) {
const selector = rawSelector.trim().replace(/\s+/g, ' ');
if (!/\.profile-(?:titles|job-title|admin-title)\b/.test(selector)) continue;
for (const [, property] of body.matchAll(/(?:^|;)\s*(font(?:-size|-weight|-family|-style)?)\s*:/g)) {
if (path.relative(root, file) !== 'css/profile.css' || profileTypographyOwners.get(selector) !== property || seenProfileTypography.has(selector)) throw new Error(`Competing profile typography: ${path.relative(root, file)}: ${selector}: ${property}. Edit the canonical profile.css block instead.`);
seenProfileTypography.add(selector);
}
}
}
if (seenProfileTypography.size !== profileTypographyOwners.size) throw new Error('Missing canonical profile title/role typography rule.');

for (const ref of ['css/common.css', 'css/footer.css', 'data/uh/header.json', 'data/uh/footer.json', 'data/uh/languages.json', 'includes/base.njk', 'includes/layouts/branding/footer/footer.njk', 'media/icons/chevron-right.svg']) {
if (!fs.existsSync(path.join(root, ref))) throw new Error(`Missing shared file: ${ref}`);
}
for (const old of ['_includes', '_data', '_media']) {
if (fs.existsSync(path.join(root, old))) throw new Error(`Retired source directory: ${old}`);
}
const baseTemplate = fs.readFileSync(path.join(root, 'includes/shell.njk'), 'utf8');
if ((baseTemplate.match(/<main\b[^>]*class="site-main"/g) || []).length !== 1) throw new Error('The shared base must have exactly one site-main page-content parent.');
if (baseTemplate.includes('class="container content-section"') || baseTemplate.includes('fullWidthSections') || baseTemplate.includes('singleColumnContent')) throw new Error('The shared shell must leave section/container/column structure to page sources.');
console.log(`Checked ${count} shared files: JSON, source CSS assets, literal include references, structure and line-height rules.`);

// Unit identity/contact data is independent of optional social accounts.
const unitsDirectory = path.join(root, 'data/units');
const standardHeroOverlay = JSON.parse(fs.readFileSync(path.join(unitsDirectory, 'ssri/site-settings.json'), 'utf8')).hero.overlay;
const buildings = JSON.parse(fs.readFileSync(path.join(root, 'data/common/buildings.json'), 'utf8'));
for (const [key, building] of Object.entries(buildings)) {
if (!building.name || !Array.isArray(building.address) || !building.address.length) throw new Error(`Invalid building identity/address: ${key}`);
if (!building.photo?.src?.startsWith('/media/') || !building.photo.alt || !(building.photo.width > 0 && building.photo.height > 0) || !fs.existsSync(path.join(root, building.photo.src.slice(1)))) throw new Error(`Invalid building photo: ${key}`);
const map = new URL(building.mapEmbedUrl);
if (map.origin !== 'https://www.google.com' || !(map.pathname.startsWith('/maps/embed') || (map.pathname === '/maps' && map.searchParams.get('output') === 'embed' && map.searchParams.get('q')))) throw new Error(`Invalid building map: ${key}`);
}
const seenNames = new Set();
let unitsChecked = 0;
for (const entry of fs.readdirSync(unitsDirectory, { withFileTypes: true })) {
// Specimen site: no required unit contacts; JSON/assets/navigation are checked separately.
if (!entry.isDirectory() || entry.name === 'style-guide') continue;
const unitDirectory = path.join(unitsDirectory, entry.name);
const siteFile = path.join(unitDirectory, 'unit-details.json');
if (!fs.existsSync(siteFile)) continue;
const site = JSON.parse(fs.readFileSync(siteFile, 'utf8'));
const fail = message => { throw new Error(`${entry.name}/unit-details.json: ${message}`); };
if (entry.name !== 'geo') {
const overlay = JSON.parse(fs.readFileSync(path.join(unitDirectory, 'site-settings.json'), 'utf8')).hero?.overlay;
if (overlay?.color !== standardHeroOverlay.color || overlay?.opacity !== standardHeroOverlay.opacity) throw new Error(`${entry.name}/site-settings.json: Hero overlay must match SSRI; Geography is the documented exception.`);
}
if (!site.building || !buildings[site.building]) fail('A valid shared building reference is required.');
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
if (!link.label || typeof link.url !== 'string' || (link.url.trim() && !/^https?:\/\/\S+$/.test(link.url.trim()))) fail('Social links require labels and either an empty URL or a web URL.');
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
const searchFile = path.join(dir, 'search.json');
if (fs.existsSync(searchFile)) {
const search = JSON.parse(fs.readFileSync(searchFile, 'utf8'));
if (search.provider === 'google-site-restricted' && (typeof search.domain !== 'string' || !search.domain.trim())) throw new Error(`${entry.name}/search.json: Site-restricted search requires a domain.`);
}
if (fs.existsSync(path.join(dir, 'site.json'))) throw new Error(`Retired data file: ${entry.name}/site.json`);
const navFile = path.join(dir, 'navigation.json');
function checkNav(items) {
for (const item of items) {
if (!item.label || (!item.url && !item.children)) throw new Error('Navigation requires label and destination or children.');
if (/\band\b/i.test(item.label)) throw new Error(`${entry.name}/navigation.json: use & instead of and in navigation label "${item.label}".`);
if (item.icon && !fs.existsSync(path.join(root, 'media/icons', item.icon + '.svg'))) throw new Error(`Unknown navigation icon: ${item.icon}`);
if (item.iconColor && !palette.has(item.iconColor)) throw new Error(`Unknown navigation color: ${item.iconColor}`);
if (item.children) checkNav(item.children);
}
}
if (fs.existsSync(navFile)) checkNav(JSON.parse(fs.readFileSync(navFile, 'utf8')));
const directoryFile = path.join(dir, 'people.json');
if (fs.existsSync(directoryFile)) {
const directory = JSON.parse(fs.readFileSync(directoryFile, 'utf8'));
const groupIds = new Set();
for (const group of directory.directoryGroups || []) {
if (!/^[a-z0-9-]+$/.test(group.id) || !group.title || groupIds.has(group.id) || !Array.isArray(group.members) || new Set(group.members).size !== group.members.length) throw new Error(`Invalid directory group: ${entry.name}/${group.id}`);
groupIds.add(group.id);
for (const member of group.members) {
const person = directory.records[member];
if (!person?.name || !person.title || !person.office || !person.email?.label || !person.email.href?.startsWith('mailto:') || (group.showTelephone && !person.phone?.label)) throw new Error(`Missing directory person/details: ${entry.name}/${member}`);
}
}
for (const groups of Object.values(directory.serviceGroups || {})) {
for (const group of groups) {
if (!group.id || !group.title || groupIds.has(group.id) || !Array.isArray(group.members)) throw new Error(`Invalid service group: ${entry.name}/${group.id}`);
groupIds.add(group.id);
for (const member of group.members) {
if ((!member.vacant && !directory.records[member.person]) || (group.showSupport && !member.support)) throw new Error(`Missing service person/assignment: ${entry.name}/${group.id}`);
}
}
}
}
for (const filename of ['people.json', 'faculty.json', 'staff.json', 'graduate-students.json']) {
const file = path.join(dir, filename);
if (!fs.existsSync(file)) continue;
const people = JSON.parse(fs.readFileSync(file, 'utf8'));
if (!Array.isArray(people)) continue;
if (filename === 'people.json' && (fs.existsSync(path.join(dir, 'faculty.json')) || fs.existsSync(path.join(dir, 'staff.json')))) throw new Error(`Duplicate people data in ${entry.name}`);
const slugs = new Set();
for (const person of people) {
if (!person.name || !person.lastName || !person.slug || slugs.has(person.slug)) throw new Error(`Invalid/duplicate person in ${entry.name}/${filename}`);
slugs.add(person.slug);
}
}
}
console.log('Checked common links, navigation icons/colors, and people records.');
