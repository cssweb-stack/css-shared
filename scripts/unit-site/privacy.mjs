// One policy source, rendered with each consuming site's shared layout and identity.
export function configurePrivacy(eleventyConfig) {
// Retire earlier local policies so they cannot compete with the shared outputs.
eleventyConfig.ignores.add('src/privacy.html');
eleventyConfig.ignores.add('src/privacy/**');
const data = {
layout: 'base.njk',
title: 'Privacy Policy',
description: 'How College of Social Sciences websites use Google Analytics and visitor information, and how to manage your privacy choices.'
};
const content = '{% include "pages/privacy.njk" %}';
eleventyConfig.addTemplate('shared-privacy.njk', content, { ...data, permalink: '/privacy.html' });
// Preserve existing bookmarks and links to the previous directory-style URL.
eleventyConfig.addTemplate('shared-privacy-legacy.njk', content, { ...data, permalink: '/privacy/index.html' });
}
