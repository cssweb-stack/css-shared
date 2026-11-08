import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const sharedRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const [unit, targetArgument, port = '8083'] = process.argv.slice(2);
if (!/^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(unit || '') || !targetArgument || !/^\d+$/.test(port)) {
throw new Error('Usage: node scripts/create-unit.mjs <unit> <destination> [port]');
}
const target = path.resolve(targetArgument);
const unitData = path.join(sharedRoot, 'src/data/units', unit);
const identity = JSON.parse(fs.readFileSync(path.join(unitData, 'unit-details.json'), 'utf8'));
const navigation = JSON.parse(fs.readFileSync(path.join(unitData, 'navigation.json'), 'utf8'));
const pages = new Map();
function collect(items) {
for (const item of items) {
if (item.url?.startsWith('/') && !item.url.startsWith('//') && !/[?#]/.test(item.url)) {
if (!pages.has(item.url)) pages.set(item.url, item.label);
}
if (item.children) collect(item.children);
}
}
collect(navigation);
if (!pages.has('/')) pages.set('/', 'Home');
// Privacy pages are generated centrally by configureUnitSite.
pages.delete('/privacy/');
pages.delete('/privacy.html');
const files = new Map();
const json = value => JSON.stringify(value, null, 2) + '\n';
files.set('shared.config.json', json({ repository: 'cssweb-stack/css-shared', ref: 'main', localPath: '../css-shared', unit }));
files.set('package.json', json({
name: unit, version: '1.0.0', private: true, type: 'module',
scripts: { dev: `eleventy --serve --port=${port}`, build: 'eleventy', clean: `node -e "import('node:fs').then(fs=>fs.rmSync('_site',{recursive:true,force:true}))"`, 'shared:check': 'node scripts/shared-source.mjs' },
devDependencies: { '@11ty/eleventy': '^3.1.2', esbuild: '^0.28.2', nunjucks: 'npm:@11ty/nunjucks@^3.3.0' },
overrides: { '@11ty/chokidar-with-glob-support': 'npm:chokidar@3.6.0' }
}));
files.set('.gitignore', 'node_modules/\n_site/\n.shared-source/\n.shared-state.json\n.DS_Store\n');
files.set('README.md', `# ${identity.name}\n\nWebsite for the ${identity.name}, College of Social Sciences, University of Hawaiʻi at Mānoa.\n`);
const bootstrap = `import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
export const project = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
export const settings = JSON.parse(fs.readFileSync(path.join(project, 'shared.config.json'), 'utf8'));
export const sharedRoot = path.resolve(project, process.env.SHARED_SOURCE || settings.localPath);
export const sharedModule = relative => pathToFileURL(path.join(sharedRoot, relative)).href;
`;
files.set('scripts/shared-bootstrap.mjs', bootstrap);
files.set('eleventy.config.js', `import { project, sharedModule } from './scripts/shared-bootstrap.mjs';
const { configureUnitSite } = await import(sharedModule('scripts/unit-site/eleventy.mjs'));
export default config => configureUnitSite(config, project);
`);
files.set('scripts/shared-settings.mjs', `import { settings } from './shared-bootstrap.mjs';
console.log('repository=' + settings.repository);
console.log('ref=' + settings.ref);
`);
files.set('scripts/shared-source.mjs', `import { project, sharedModule } from './shared-bootstrap.mjs';
const { createSharedSource } = await import(sharedModule('scripts/unit-site/shared-source.mjs'));
console.log('Shared source ready: ' + createSharedSource(project).checkShared());
`);
const intro = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.';
const paragraphs = [
'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer vitae libero ac risus egestas placerat. Vestibulum commodo felis quis tortor. Ut aliquam sollicitudin leo. Cras iaculis ultricies nulla, donec quis dui at dolor tempor interdum.',
'Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium. Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat facere possimus.',
'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
];
const escape = text => text.replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;');
for (const [url, title] of pages) {
const relative = url === '/' ? 'index.html' : url.replace(/^\//, '').replace(/\/$/, '.html');
if (!relative.endsWith('.html') || relative.split('/').some(part => part === '..' || part === '.')) throw new Error(`Unsupported page URL: ${url}`);
const contact = /^\/contact(?:\/|\.html)$/.test(url) && identity.building ? '{% include "layouts/content/unit-contact.njk" %}\n' : '';
files.set('src/' + relative, `---\nlayout: base.njk\ntitle: ${JSON.stringify(title)}\nhidePageTitle: true\npermalink: ${JSON.stringify(url)}\n---\n<h1>${escape(title)}</h1>\n<p class="tagline">Lorem ipsum dolor sit amet.</p>\n<p class="intro">${intro}</p>\n${contact}${paragraphs.map(text => `<p>${text}</p>`).join('\n')}\n`);
}
let workflow = fs.readFileSync(path.join(sharedRoot, 'scripts/unit-site/deploy.yml'), 'utf8');
workflow = workflow.replace('Build and publish GEO', `Build and publish ${identity.shortName}`).replaceAll('/geo/', `/${unit}/`);
files.set('.github/workflows/deploy.yml', workflow);
// Refuse overwrites before writing anything; reruns never replace edited pages.
for (const name of files.keys()) if (fs.existsSync(path.join(target, name))) throw new Error(`Already exists: ${name}`);
for (const [name, contents] of files) {
const output = path.join(target, name);
fs.mkdirSync(path.dirname(output), { recursive: true });
fs.writeFileSync(output, contents);
}
console.log(`Created ${identity.shortName} in ${target}: ${pages.size} starter pages.`);
