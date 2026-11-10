import { createRequire } from 'node:module';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { createSharedSource } from './shared-source.mjs';
import { configurePrivacy } from './privacy.mjs';
import { resolveFacultyPerson } from './faculty-profiles.mjs';
export function configureUnitSite(eleventyConfig, project) {
const require = createRequire(path.join(project, 'package.json'));
const { build } = require('esbuild');
const nunjucks = require('nunjucks');
const { checkShared, loadUnit, loadUH, loadCommon } = createSharedSource(project);
const sourceDir = path.join(project, 'src');
const settings = loadUnit().site;
const stylesheet = settings.stylesheet || '/unit.css';
if (!/^\/[a-z0-9-]+\.css$/.test(stylesheet)) throw new Error('Unit stylesheet must be a root-level CSS filename.');
eleventyConfig.setServerOptions({ domDiff: false });
if (['serve', 'watch'].includes(process.env.ELEVENTY_RUN_MODE)) eleventyConfig.setUseTemplateCache(false);
const sharedRoot = checkShared();
const sharedDir = path.join(sharedRoot, 'src');
const sharedIncludes = path.join(sharedDir, 'includes');
const environment = new nunjucks.Environment(new nunjucks.FileSystemLoader([sharedIncludes, sharedDir, path.join(sourceDir, 'includes')], { noCache: true }), { autoescape: false });
eleventyConfig.setLibrary('njk', environment);
configurePrivacy(eleventyConfig, project);
const eventDate = createRequire(import.meta.url)(path.join(sharedIncludes, 'layouts/events/event-date.cjs'));
eleventyConfig.addFilter('eventDate', eventDate);
eleventyConfig.addFilter('contactFaculty', people => people.filter(person => person.contactOrder).sort((a, b) => a.contactOrder - b.contactOrder));
eleventyConfig.addFilter('telephone', value => String(value || '').replace(/[^\d+]/g, ''));
eleventyConfig.addFilter('navIconColor', name => {
const palette = { blue: 'var(--color-blue)', gold: 'var(--color-gold)', teal: 'var(--color-teal)', purple: 'var(--color-purple)', gray: 'var(--mid-gray)' };
if (!palette[name]) throw new Error(`Unknown navigation icon color: ${name}`);
return palette[name];
});
eleventyConfig.addFilter('url', value => {
const url = String(value || '');
const prefix = (process.env.SITE_PATH_PREFIX || '/').replace(/\/$/, '');
return url.startsWith('/') && !url.startsWith('//') ? prefix + url : url;
});
// Social images must use the current deployment's public host and path prefix.
eleventyConfig.addFilter('socialUrl', value => {
const origin = (process.env.SITE_ORIGIN || loadUnit().site.url || '').replace(/\/$/, '');
const prefix = (process.env.SITE_PATH_PREFIX || '/').replace(/\/$/, '');
return origin + prefix + String(value || '');
});
eleventyConfig.addGlobalData('common', () => loadCommon());
eleventyConfig.addGlobalData('uh', () => loadUH());
eleventyConfig.addGlobalData('eleventyComputed', {
person: resolveFacultyPerson,
canonicalUrl: data => (data.site.canonicalSections || []).some(prefix => data.page.url.startsWith(prefix)) ? data.site.url + data.page.url : undefined
});
for (const key of Object.keys(loadUnit())) eleventyConfig.addGlobalData(key, () => key === 'site' ? { ...loadUnit().site, stylesheet } : loadUnit()[key]);
// Preserve established page variable names while filenames become descriptive.
eleventyConfig.addGlobalData('students', () => loadUnit().graduate_students);
eleventyConfig.addGlobalData('lectures', () => loadUnit().events);
eleventyConfig.setUseGitIgnore(false);
eleventyConfig.addWatchTarget(path.relative(project, sharedDir).split(path.sep).join('/'), { resetConfig: true });
eleventyConfig.addWatchTarget('src/**/*.css');
eleventyConfig.on('eleventy.before', async () => {
checkShared();
// Resolve source-relative assets to copied public paths, including project-prefix-safe CSS URLs.
await build({
absWorkingDir: project,
stdin: {
contents: `@import ${JSON.stringify(path.join(sharedDir, 'css/common.css'))};` + (fs.existsSync(path.join(sourceDir, 'css/unit.css')) ? '\n@import "./css/unit.css";' : ''),
resolveDir: sourceDir,
sourcefile: 'department-bundle.css',
loader: 'css'
},
outfile: path.join(project, '_site', stylesheet.slice(1)),
bundle: true,
minify: true,
charset: 'utf8',
logLevel: 'info',
plugins: [{
name: 'copied-public-assets',
setup(builder) {
// Units may disable layout guides without changing the shared diagnostic import.
builder.onResolve({ filter: /(?:^|\/)diagnostics\.css$/ }, args => {
if (loadUnit().site.layoutGuides === false) return { path: args.path, namespace: 'disabled-layout-guides' };
});
builder.onLoad({ filter: /.*/, namespace: 'disabled-layout-guides' }, () => ({ contents: '', loader: 'css' }));
builder.onResolve({ filter: /.*/ }, args => {
if (args.kind !== 'url-token') return;
if (/^(?:[a-z][a-z\d+.-]*:|\/|#)/i.test(args.path)) return { path: args.path, external: true };
const split = args.path.search(/[?#]/);
const assetPath = split < 0 ? args.path : args.path.slice(0, split);
const suffix = split < 0 ? '' : args.path.slice(split);
const absolute = path.resolve(args.resolveDir, assetPath);
if (!fs.existsSync(absolute) || !fs.statSync(absolute).isFile()) throw new Error(`Missing CSS asset: ${absolute}`);
const owner = [sharedDir, sourceDir].find(root => absolute.startsWith(root + path.sep));
if (!owner) throw new Error(`CSS asset is outside shared and department source: ${absolute}`);
const relative = path.relative(owner, absolute).split(path.sep).join('/');
if (!/^(?:assets|media)\//.test(relative)) throw new Error(`CSS assets must live under assets or media: ${relative}`);
return { path: './' + relative + suffix, external: true };
});
}
}]
});
});
// Publish images/fonts/scripts only; JSON, templates and helper modules stay private to the build.
for (const root of [sharedDir, sourceDir]) {
for (const folder of ['assets', 'media']) {
if (fs.existsSync(path.join(root, folder))) eleventyConfig.addPassthroughCopy({ [path.relative(project, path.join(root, folder)).split(path.sep).join('/')]: folder }, { filter: relative => !/(?:^|[\\/])(?:\.DS_Store|\._[^/]*|README\.md)$/.test(relative) });
}
}
return {
pathPrefix: process.env.SITE_PATH_PREFIX || '/',
dir: { input: 'src', includes: 'includes', layouts: path.relative(sourceDir, sharedIncludes).split(path.sep).join('/'), data: 'data', output: '_site' },
htmlTemplateEngine: 'njk',
markdownTemplateEngine: 'njk',
templateFormats: ['html', 'njk', 'md']
};
}
