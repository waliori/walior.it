// Captures the screens behind each product frame, at 1440x900 and 2x, into material/screens/<slot>-<n>.png.
// Needs puppeteer-core reachable: PUPPETEER_PATH=/path/to/node_modules/puppeteer-core CHROME_PATH=$(which google-chrome-stable) node tools/frames.mjs
import { createRequire } from 'node:module';
const require = createRequire(import.meta.url);
const puppeteer = require(process.env.PUPPETEER_PATH || 'puppeteer-core');
const wait = (ms) => new Promise((r) => setTimeout(r, ms));
const b = await puppeteer.launch({ executablePath: process.env.CHROME_PATH, headless: true });
const page = async (dark) => { const p = await b.newPage(); await p.emulateMediaFeatures([{ name: 'prefers-color-scheme', value: dark ? 'dark' : 'light' }]); await p.setViewport({ width: 1440, height: 900, deviceScaleFactor: 2 }); return p; };
const clickText = (p, re, max = 24) => p.evaluate((src, max) => { const re = new RegExp(src); const el = [...document.querySelectorAll('button,a,[role=tab]')].find((e) => re.test(e.textContent.replace(/\s+/g, ' ').trim()) && e.textContent.trim().length <= max); if (el) { el.click(); return true; } return false; }, re.source, max);
const shot = (p, name) => p.screenshot({ path: `material/screens/${name}.png` });

// Sailor's Log: its dark scheme, the tour closed, then five tabs
{
  const p = await page(true);
  await p.goto('https://sail.walior.it/', { waitUntil: 'networkidle2', timeout: 60000 }); await wait(2500);
  await clickText(p, /^×$/); await wait(600);
  let i = 1;
  for (const tab of ['Map', 'Plan', 'Barter', 'Ship', 'Quests']) { const ok = await clickText(p, new RegExp(tab + '$')); await wait(3500); console.log('sail', tab, ok); await shot(p, `sail-${i++}`); }
  await p.close();
}
// The toucan page: three scroll positions of the site, then the trainer
{
  const p = await page(false);
  await p.goto('https://toucan.walior.it/', { waitUntil: 'networkidle2', timeout: 60000 }); await wait(2500);
  let i = 1;
  for (const y of [0, 1700, 3400, 5200]) { await p.evaluate((y) => window.scrollTo(0, y), y); await wait(1200); await shot(p, `toucan-${i++}`); }
  await p.goto('https://toucan.walior.it/trainer/', { waitUntil: 'networkidle2', timeout: 60000 }); await wait(3000); await shot(p, `toucan-${i++}`);
  await p.close();
}
// ayat.network: the welcome card closed, the dark theme, the tour skipped, then the graph and two other views
{
  const p = await page(true);
  await p.goto('https://ayat.network/', { waitUntil: 'networkidle2', timeout: 60000 }); await wait(4000);
  await clickText(p, /^✕$/); await wait(800); await clickText(p, /^☾$/); await wait(1200); await clickText(p, /^تخط/); await wait(2500);
  await shot(p, 'ayat-1');
  let i = 2;
  for (const btn of ['≣', '⊞', '▦', '⚖']) { const ok = await clickText(p, new RegExp('^' + btn + '$')); await wait(3000); console.log('ayat', btn, ok); await shot(p, `ayat-${i++}`); await clickText(p, new RegExp('^' + btn + '$')); await wait(800); }
  await p.close();
}
await b.close();
