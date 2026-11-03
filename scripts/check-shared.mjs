import fs from 'node:fs';
import path from 'node:path';
const root = path.resolve('src');
let count = 0;
function checkLineHeights(file) {
const css = fs.readFileSync(file, 'utf8').replace(/\/\*[\s\S]*?\*\//g, '');
for (const match of css.matchAll(/(?:^|[;{}])\s*(line-height|--[\w-]*(?:line-height|leading)[\w-]*|font)\s*:\s*([^;{}]+)/g)) {
const [, property, raw] = match;
const value = raw.replace(/\s*!important\s*$/, '').trim();
if (property === 'font') {
if (value === 'inherit') continue;
throw new Error(`Use explicit font properties with a checked line-height in ${file}: ${value}`);
}
if (value === 'inherit' || /^var\(--[\w-]+\)$/.test(value)) continue;
if (!/^\d*\.?\d+$/.test(value) || Number(value) < 1.5) throw new Error(`Line-height must be unitless and at least 1.5 in ${file}: ${value}`);
}
}
function check(dir) {
for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
const file = path.join(dir, entry.name);
if (entry.isSymbolicLink()) throw new Error(`Unexpected symbolic link: ${file}`);
if (entry.isDirectory()) check(file);
else { if (entry.name.endsWith('.json')) JSON.parse(fs.readFileSync(file, 'utf8')); if (entry.name.endsWith('.css')) checkLineHeights(file); if (!fs.statSync(file).size) throw new Error(`Empty shared file: ${file}`); count++; }
}
}
check(root);
for (const file of ['colors.css', 'common.css', 'callouts.css', 'shell.css', '_data/university.json', '_includes/layouts/base.njk', '_includes/components/footer.njk']) if (!fs.existsSync(path.join(root, file))) throw new Error(`Missing shared file: ${file}`);
console.log(`Checked ${count} shared files.`);
