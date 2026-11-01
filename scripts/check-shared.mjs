import fs from 'node:fs';
import path from 'node:path';
const root = path.resolve('src');
let count = 0;
function check(dir) {
for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
const file = path.join(dir, entry.name);
if (entry.isSymbolicLink()) throw new Error(`Unexpected symbolic link: ${file}`);
if (entry.isDirectory()) check(file);
else { if (entry.name.endsWith('.json')) JSON.parse(fs.readFileSync(file, 'utf8')); if (!fs.statSync(file).size) throw new Error(`Empty shared file: ${file}`); count++; }
}
}
check(root);
for (const file of ['common.css', 'shell.css', '_data/university.json', '_includes/layouts/base.njk', '_includes/components/footer.njk']) if (!fs.existsSync(path.join(root, file))) throw new Error(`Missing shared file: ${file}`);
console.log(`Checked ${count} shared files.`);
