// A still of an HTML file at a given size: node tools/still.mjs <file.html> <out.png> <width> <height>
// Needs PUPPETEER_PATH (a folder holding puppeteer-core) and CHROME_PATH, like tools/frames.mjs.
import { createRequire } from 'node:module';
import { resolve } from 'node:path';
const puppeteer = createRequire(resolve(process.env.PUPPETEER_PATH, 'x.js'))('puppeteer-core');
const [src, out, w, h] = process.argv.slice(2);
const b = await puppeteer.launch({ executablePath: process.env.CHROME_PATH, headless: true });
const p = await b.newPage(); await p.setViewport({ width: +w, height: +h, deviceScaleFactor: 1 });
await p.goto('file://' + resolve(src), { waitUntil: 'networkidle0' }); await p.evaluate(() => document.fonts.ready); await new Promise(r => setTimeout(r, 1200));
await p.screenshot({ path: out }); await b.close();
