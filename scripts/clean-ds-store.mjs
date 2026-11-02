import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

// Only prune directories that become empty because this traversal removed metadata.
export function cleanDSStore(root) {
  const result = { files: 0, directories: 0 };
  function visit(directory) {
    let changed = false;
    for (const entry of fs.readdirSync(directory, { withFileTypes: true })) {
      if (entry.name === '.git' || entry.isSymbolicLink()) continue;
      const target = path.join(directory, entry.name);
      if (entry.isFile() && entry.name === '.DS_Store') {
        fs.unlinkSync(target);
        result.files++;
        changed = true;
      } else if (entry.isDirectory() && !fs.existsSync(path.join(target, '.git'))) {
        const childChanged = visit(target);
        if (childChanged && fs.readdirSync(target).length === 0) {
          fs.rmdirSync(target);
          result.directories++;
        }
        changed = changed || childChanged;
      }
    }
    return changed;
  }
  visit(root);
  return result;
}

const script = fileURLToPath(import.meta.url);
if (process.argv[1] && path.resolve(process.argv[1]) === script) {
  const root = path.resolve(path.dirname(script), '..');
  const result = cleanDSStore(root);
  console.log(`Removed ${result.files} .DS_Store files and ${result.directories} newly empty directories from ${root}.`);
}
