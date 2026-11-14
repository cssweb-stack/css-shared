// Bootstrap owns dropdown visibility and aria-expanded for mouse and keyboard.
// Desktop hover uses the same state, so Escape can dismiss a hovered menu too.
(() => {
const desktopHover = window.matchMedia('(min-width: 1200px) and (hover: hover)');
document.querySelectorAll('.unit-nav .dropdown').forEach(dropdown => {
const trigger = dropdown.querySelector('[data-bs-toggle="dropdown"]');
if (!trigger) return;
const controller = () => window.bootstrap?.Dropdown.getOrCreateInstance(trigger);
dropdown.addEventListener('pointerenter', () => {
if (desktopHover.matches) controller()?.show();
});
dropdown.addEventListener('pointerleave', () => {
if (desktopHover.matches && !dropdown.contains(document.activeElement)) controller()?.hide();
});
dropdown.addEventListener('focusout', () => {
setTimeout(() => {
if (!dropdown.contains(document.activeElement)) controller()?.hide();
}, 0);
});
});
document.addEventListener('keydown', event => {
if (event.key !== 'Escape') return;
document.querySelectorAll('.unit-nav .dropdown-menu.show').forEach(menu => {
const trigger = menu.parentElement.querySelector('[data-bs-toggle="dropdown"]');
if (trigger) window.bootstrap?.Dropdown.getOrCreateInstance(trigger).hide();
});
});
})();

// One load-based fade for every framed content photo, including lazy-loaded photos.
// No scroll observer, movement, or hidden state; images work without JavaScript.
(() => {
if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
const images = document.querySelectorAll('img.photo-frame, img.grid-photo');
images.forEach(image => {
const fade = () => {
if (image.naturalWidth > 0) image.classList.add('is-loaded');
};
if (image.complete) fade();
else image.addEventListener('load', fade, { once: true });
});
})();

document.querySelectorAll("[data-copyright-year]").forEach(element => {
element.textContent = new Date().getFullYear();
});

// Keep opted-in page jump headings visible below the responsive sticky header.
(() => {
const header = document.querySelector('.sticky-header');
if (!header || !document.querySelector('.page-jump-target')) return;
const updateOffset = () => {
document.documentElement.style.setProperty('--sticky-header-height', `${header.getBoundingClientRect().height}px`);
};
updateOffset();
if ('ResizeObserver' in window) new ResizeObserver(updateOffset).observe(header);
else window.addEventListener('resize', updateOffset);
// Also correct an incoming bookmark after images and fonts establish page layout.
window.addEventListener('load', () => {
updateOffset();
let id;
try { id = decodeURIComponent(window.location.hash.slice(1)); } catch { return; }
const target = document.getElementById(id);
if (target?.classList.contains('page-jump-target')) target.scrollIntoView({ behavior: 'instant', block: 'start' });
}, { once: true });
})();
