import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
const root = fileURLToPath(new URL('../', import.meta.url));
let count = 0;
function clean(dir) {
if (dir !== root && fs.existsSync(path.join(dir, '.git'))) return;
for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
if (entry.isSymbolicLink() || entry.name === '.git' || entry.name === 'node_modules') continue;
const file = path.join(dir, entry.name);
if (entry.isDirectory()) clean(file);
else if (entry.name === '.DS_Store') { fs.unlinkSync(file); count++; }
}
}
clean(root);
console.log(`Removed ${count} .DS_Store files. No directories removed.`);
