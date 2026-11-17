// Remove template whitespace without changing embedded code or preformatted text.
export function formatGeneratedHtml(html) {
const preserved = [];
const masked = html.replace(/<(script|style|pre|textarea)\b[^>]*>[\s\S]*?<\/\1\s*>/gi, block => {
const index = preserved.push(block) - 1;
return `\uE000${index}\uE001`;
});
return masked.split(/\r?\n/).filter(line => /\S/.test(line)).join('\n').replace(/\uE000(\d+)\uE001/g, (_, index) => preserved[Number(index)]) + '\n';
}
