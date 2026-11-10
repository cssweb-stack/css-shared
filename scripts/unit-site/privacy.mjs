import fs from 'node:fs';
import path from 'node:path';

// One policy source, rendered with each consuming site's shared layout and identity.
export function configurePrivacy(eleventyConfig, project = process.cwd()) {
// Retire earlier local policies so they cannot compete with the shared outputs.
eleventyConfig.ignores.add('src/privacy/**');
// Local HTML pages own their metadata while retaining the shared policy content.
if (fs.existsSync(path.join(project, 'src/privacy.html'))) return;
const data = {
layout: 'shell.njk',
hidePageTitle: true,
title: 'Privacy Policy',
description: 'How College of Social Sciences websites use Google Analytics and visitor information, and how to manage your privacy choices.'
};
const content = '{% include "pages/privacy.njk" %}';
eleventyConfig.addTemplate('shared-privacy.njk', content, { ...data, permalink: '/privacy.html' });
}
