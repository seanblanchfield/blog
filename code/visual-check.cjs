#!/usr/bin/env node
// Visit the local preview, capture screenshots, and fail on broken local resources.
const { chromium } = require(process.env.PLAYWRIGHT_MODULE || 'playwright');
const { mkdir } = require('node:fs/promises');
const path = require('node:path');

const base = process.env.BLOG_PREVIEW_URL || 'http://127.0.0.1:8765';
const output = path.join(__dirname, '..', 'screenshots');
const pages = [
  ['home', '/'],
  ['article', '/2026/08/ai-sovereignty'],
  ['older', '/page/3/'],
  ['about', '/about/'],
];
const viewports = [
  ['desktop', { width: 1440, height: 900 }, false],
  ['mobile', { width: 390, height: 844 }, true],
];

async function checkThemes(browser, failures) {
  for (const [label, viewport, isMobile] of viewports) {
    for (const [mode, expectedBackground] of [['light', 'rgb(250, 248, 244)'], ['dark', 'rgb(16, 27, 37)']]) {
      const context = await browser.newContext({ viewport, isMobile, hasTouch: isMobile, colorScheme: mode });
      const page = await context.newPage();
      const localFailures = [];
      page.on('pageerror', error => localFailures.push(`JS: ${error.message}`));
      await page.goto(new URL('/2024/07/restore-corrupted-ha-database', base).toString());
      const initial = await page.evaluate(() => ({
        theme: document.documentElement.dataset.theme || null,
        background: getComputedStyle(document.body).backgroundColor,
        codeBackground: getComputedStyle(document.querySelector('.article-body pre')).backgroundColor,
        codeToken: getComputedStyle(document.querySelector('.article-body .codehilite span[class]:not(.w)')).color,
        highlighted: document.querySelectorAll('.article-body .codehilite').length,
        label: document.querySelector('#theme-toggle').getAttribute('aria-label'),
        role: document.querySelector('#theme-toggle').getAttribute('role'),
        checked: document.querySelector('#theme-toggle').getAttribute('aria-checked'),
        sun: getComputedStyle(document.querySelector('.theme-toggle__sun')).display,
        moon: getComputedStyle(document.querySelector('.theme-toggle__moon')).display,
        thumbX: getComputedStyle(document.querySelector('.theme-toggle__thumb')).transform,
      }));
      if (initial.theme !== null || initial.background !== expectedBackground || initial.label !== 'Dark mode' ||
          initial.role !== 'switch' || initial.checked !== String(mode === 'dark') || !initial.highlighted || !initial.codeToken ||
          (mode === 'light' ? initial.sun === 'none' || initial.moon !== 'none' : initial.sun !== 'none' || initial.moon === 'none')) {
        localFailures.push(`System ${mode} theme failed: ${JSON.stringify(initial)}`);
      }
      const toggle = page.locator('#theme-toggle');
      await toggle.focus();
      await page.keyboard.press('Enter');
      const chosen = mode === 'light' ? 'dark' : 'light';
      const afterClick = await page.evaluate(() => ({
        theme: document.documentElement.dataset.theme,
        stored: localStorage.getItem('blog-color-theme'),
        checked: document.querySelector('#theme-toggle').getAttribute('aria-checked'),
        sun: getComputedStyle(document.querySelector('.theme-toggle__sun')).display,
        moon: getComputedStyle(document.querySelector('.theme-toggle__moon')).display,
        thumbX: getComputedStyle(document.querySelector('.theme-toggle__thumb')).transform,
        background: getComputedStyle(document.body).backgroundColor,
        codeBackground: getComputedStyle(document.querySelector('.article-body pre')).backgroundColor,
        codeToken: getComputedStyle(document.querySelector('.article-body .codehilite span[class]:not(.w)')).color,
        overflow: document.documentElement.scrollWidth - innerWidth,
      }));
      if (afterClick.theme !== chosen || afterClick.stored !== chosen || afterClick.checked !== String(chosen === 'dark') ||
          (chosen === 'light' ? afterClick.sun === 'none' || afterClick.moon !== 'none' : afterClick.sun !== 'none' || afterClick.moon === 'none') ||
          afterClick.background === initial.background || afterClick.codeBackground === initial.codeBackground ||
          afterClick.codeToken === initial.codeToken || afterClick.overflow > 1) {
        localFailures.push(`Switching from ${mode} failed: ${JSON.stringify(afterClick)}`);
      }
      await page.reload();
      if (await page.evaluate(() => document.documentElement.dataset.theme) !== chosen) {
        localFailures.push(`Choice was not remembered after reload from ${mode}`);
      }
      await page.goto(new URL('/', base).toString());
      if (await page.evaluate(() => document.documentElement.dataset.theme) !== chosen) {
        localFailures.push(`Choice was not remembered across pages from ${mode}`);
      }
      await page.locator('#theme-toggle').focus();
      await page.keyboard.press('Space');
      const keyboard = await page.evaluate(() => ({ theme: document.documentElement.dataset.theme,
        checked: document.querySelector('#theme-toggle').getAttribute('aria-checked') }));
      if (keyboard.theme !== mode || keyboard.checked !== String(mode === 'dark')) {
        localFailures.push(`Space key switch failed from ${chosen}: ${JSON.stringify(keyboard)}`);
      }
      const file = path.join(output, `theme-${mode}-to-${chosen}-${label}.png`);
      await page.screenshot({ path: file, fullPage: true });
      console.log(`${label} system ${mode}, chosen ${chosen} — ${file}`);
      failures.push(...localFailures.map(message => `${label}: ${message}`));
      await context.close();
    }
  }
}

async function main() {
  const url = new URL(base);
  if (!['localhost', '127.0.0.1', '[::1]'].includes(url.hostname)) {
    throw new Error('Preview checks may only visit a loopback server');
  }
  await mkdir(output, { recursive: true });
  const browser = await chromium.launch({ headless: true, args: ['--no-sandbox'] });
  const failures = [];
  try {
    for (const [name, viewport, isMobile] of viewports) {
      const context = await browser.newContext({ viewport, isMobile, hasTouch: isMobile });
      for (const [label, pathname] of pages) {
        const page = await context.newPage();
        const url = new URL(pathname, base).toString();
        const localFailures = [];
        page.on('pageerror', error => localFailures.push(`JS: ${error.message}`));
        page.on('response', response => {
          if (response.url().startsWith(base) && response.status() >= 400) {
            localFailures.push(`HTTP ${response.status()}: ${response.url()}`);
          }
        });
        const response = await page.goto(url, { waitUntil: 'load', timeout: 30000 });
        if (!response || response.status() !== 200) localFailures.push(`Navigation failed: ${url}`);
        // Eagerly load off-screen thumbnails before classifying lazy images as broken.
        await page.evaluate(async () => {
          await Promise.all([...document.images].map(image => {
            image.loading = 'eager';
            return image.decode().catch(() => null);
          }));
        });
        const state = await page.evaluate(() => ({
          title: document.title,
          contentType: document.contentType,
          overflow: document.documentElement.scrollWidth - innerWidth,
          switchBox: document.querySelector('#theme-toggle').getBoundingClientRect().toJSON(),
          navBox: document.querySelector('.site-nav').getBoundingClientRect().toJSON(),
          headerBox: document.querySelector('.site-header').getBoundingClientRect().toJSON(),
          brokenImages: [...document.images].filter(image => !image.complete || !image.naturalWidth).map(image => image.src),
        }));
        if (state.contentType !== 'text/html') localFailures.push(`Wrong content type: ${state.contentType}`);
        if (state.overflow > 1) localFailures.push(`Horizontal overflow: ${state.overflow}px`);
        if (state.switchBox.bottom > state.navBox.top || state.switchBox.top < state.headerBox.top ||
            state.switchBox.right > state.headerBox.right || state.switchBox.left < state.headerBox.left) {
          localFailures.push(`Theme switch not above navigation inside header: ${JSON.stringify(state)}`);
        }
        for (const image of state.brokenImages) localFailures.push(`Broken image: ${image}`);
        const file = path.join(output, `${label}-${name}.png`);
        await page.screenshot({ path: file, fullPage: true });
        console.log(`${name} ${label}: ${state.title} — ${file}`);
        failures.push(...localFailures.map(message => `${name} ${label}: ${message}`));
        await page.close();
      }
      await context.close();
    }
    await checkThemes(browser, failures);
  } finally {
    await browser.close();
  }
  const [markdownResponse, indexResponse] = await Promise.all([
    fetch(new URL('/2026/08/ai-sovereignty.md', base)),
    fetch(new URL('/llms.txt', base)),
  ]);
  if (!markdownResponse.ok || !markdownResponse.headers.get('content-type')?.startsWith('text/markdown')) {
    failures.push('Local article Markdown endpoint failed or has the wrong content type');
  }
  if (!indexResponse.ok || !(await indexResponse.text()).includes('/2026/08/ai-sovereignty.md')) {
    failures.push('Local llms.txt is missing a same-site Markdown link');
  }
  if (failures.length) {
    console.error(failures.join('\n'));
    process.exitCode = 1;
  } else {
    console.log('Browser check passed: 12 screenshots, both colour modes with saved preference, Markdown and llms.txt endpoints, no broken loaded local resources or horizontal overflow.');
  }
}

main().catch(error => { console.error(error); process.exitCode = 1; });
