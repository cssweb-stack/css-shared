// Read the real layout after CSS resolves; do not supply layout or gap rules here.
const stages = [...document.querySelectorAll('[data-grid-id]')];
function describe(stage) {
const grid = stage.querySelector(stage.dataset.gridSelector);
const reading = document.querySelector(`[data-grid-reading="${stage.dataset.gridId}"]`);
if (!grid || !reading || !stage.getClientRects().length) return;
const style = getComputedStyle(grid);
const layout = grid.matches('.course-resources') ? grid.firstElementChild : grid;
const layoutStyle = getComputedStyle(layout);
const children = [...layout.children].filter(child => getComputedStyle(child).display !== 'none');
const firstTop = children[0]?.getBoundingClientRect().top;
const firstRow = children.filter(child => Math.abs(child.getBoundingClientRect().top - firstTop) < 2);
const width = layout.getBoundingClientRect().width;
const standardSidebar = ['left', 'right'].some(side => ['sm', 'med', 'large'].some(size => layout.classList.contains(`sidebar-${side}-${size}`)));
const trackWidth = standardSidebar ? width - (parseFloat(layoutStyle.columnGap) || 0) * Math.max(firstRow.length - 1, 0) : width;
let columns = firstRow.map(child => `${Math.round(child.getBoundingClientRect().width / trackWidth * 100)}%`).join(' / ');
let horizontal = layoutStyle.columnGap;
let vertical = layoutStyle.rowGap;
if (layout.classList.contains('row')) {
horizontal = layoutStyle.getPropertyValue('--bs-gutter-x').trim();
vertical = layoutStyle.getPropertyValue('--bs-gutter-y').trim();
}
if (layout.classList.contains('list-columns-two')) {
columns = `${style.columnCount === 'auto' ? 1 : style.columnCount} flowing column(s)`;
vertical = 'list spacing';
}
if (layout.classList.contains('grid-five')) columns = `${firstRow.length} tiles across`;
if (layout.classList.contains('portrait-card-grid')) columns = `${firstRow.length} cards across`;
const pixels = value => value.endsWith('rem') ? `${parseFloat(value) * parseFloat(getComputedStyle(document.documentElement).fontSize)}px` : value;
reading.textContent = `${innerWidth}px viewport · ${columns || 'Stacked'} · gap H ${pixels(horizontal)}, V ${pixels(vertical)}`;
}
let frame;
function update() {
cancelAnimationFrame(frame);
frame = requestAnimationFrame(() => stages.forEach(describe));
}
new ResizeObserver(update).observe(document.documentElement);
window.addEventListener('resize', update);
document.fonts.ready.then(update);
update();

// Progressive enhancement: without JavaScript every group remains visible.
const tablist = document.querySelector('.review-grid-tabs');
const tabs = [...document.querySelectorAll('.review-grid-tabs [role="tab"]')];
const panels = [...document.querySelectorAll('[data-grid-panel]')];
function activate(tab, remember = true) {
for (const item of tabs) {
const selected = item === tab;
item.setAttribute('aria-selected', String(selected));
item.tabIndex = selected ? 0 : -1;
const panel = document.getElementById(item.getAttribute('aria-controls'));
panel.hidden = !selected;
panel.setAttribute('role', 'tabpanel');
}
if (remember) history.replaceState(null, '', `#${tab.getAttribute('aria-controls')}`);
update();
}
if (tablist && tabs.length) {
tablist.hidden = false;
for (const tab of tabs) {
tab.addEventListener('click', () => activate(tab));
tab.addEventListener('keydown', event => {
const index = tabs.indexOf(tab);
const next = {ArrowRight: (index + 1) % tabs.length, ArrowLeft: (index + tabs.length - 1) % tabs.length, Home: 0, End: tabs.length - 1}[event.key];
if (next === undefined) return;
event.preventDefault();
tabs[next].focus();
activate(tabs[next]);
});
}
function restorePanel() {
const target = document.getElementById(location.hash.slice(1));
const panel = target?.closest('[data-grid-panel]');
activate(tabs.find(tab => tab.getAttribute('aria-controls') === panel?.id) || tabs[0], false);
}
window.addEventListener('hashchange', restorePanel);
restorePanel();
}
