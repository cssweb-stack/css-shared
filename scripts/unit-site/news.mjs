import fs from 'node:fs';

export function configureNews(config, settings) {
if (!settings) return;
config.addCollection('unitNews', api => api.getFilteredByTag('unit-news').sort((a, b) => new Date(b.data.date) - new Date(a.data.date) || b.data.wordpressId - a.data.wordpressId));
config.addFilter('newsDate', value => new Intl.DateTimeFormat('en-US', { dateStyle: 'long', timeZone: 'UTC' }).format(new Date(`${String(value).slice(0, 10)}T12:00:00Z`)));
config.addFilter('newsOpening', inputPath => {
const source = fs.readFileSync(inputPath, 'utf8').replace(/^---[\s\S]*?---\s*/, '');
const paragraph = source.match(/<p\b[^>]*>([\s\S]*?)<\/p>/i)?.[1] || '';
const words = paragraph.replace(/<[^>]*>/g, ' ').replace(/\s+/g, ' ').trim().split(' ');
return words.slice(0, 65).join(' ') + (words.length > 65 ? ' …' : '');
});
}
