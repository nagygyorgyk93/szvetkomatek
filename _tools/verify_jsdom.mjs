// Szvetkó matek — oldal-render ellenőrzés jsdom-mal (böngésző nélkül).
// Használat:  node verify_jsdom.mjs <oldal.html> [<oldal.html> ...]
// Kimenet: soronként egy JSON objektum (JSONL), hogy a Python driver olvashassa.
//
// Miért jsdom és nem Playwright: a sandbox nem tud Chromiumot letölteni, viszont a
// jsdom lefuttatja az oldal saját JS-ét (KaTeX auto-render, quiz.js), ami a legtöbb
// valódi hibát megfogja. Ami hiányzik: layout, tehát mobil-túlcsordulás és nyomtatási
// nézet — azt böngészőből kell nézni (lásd a web-verifikacio skill 3. rétegét).

import { createRequire } from 'module';
import path from 'path';

// A jsdom nem függősége a repónak (nincs package.json) — több helyről is elfogadjuk.
// ESM-ben a NODE_PATH nem működik, ezért createRequire-rel oldjuk fel.
function jsdomBetolt() {
  const jeloltek = [
    process.env.JSDOM_DIR,
    '/tmp/vw/node_modules',
    new URL('./node_modules/', import.meta.url).pathname,
    '/tmp/node_modules',
  ].filter(Boolean);
  for (const d of jeloltek) {
    try { return createRequire(d.endsWith('/') ? d : d + '/')('jsdom'); } catch {}
  }
  try { return createRequire(import.meta.url)('jsdom'); } catch {}
  throw new Error('jsdom nem található. Telepítés: npm install jsdom --prefix /tmp/vw');
}
const { JSDOM, VirtualConsole } = jsdomBetolt();

// A jsdom nem ismer néhány böngésző-API-t, amit az effekt.js/ui.js használ.
// Stubolni kell őket, különben minden oldalra hamis hibát jelentenénk.
const STUB = `
  window.IntersectionObserver = class { constructor(cb){this.cb=cb;} observe(){} unobserve(){} disconnect(){} takeRecords(){return [];} };
  window.ResizeObserver = class { observe(){} unobserve(){} disconnect(){} };
  if (!window.matchMedia) window.matchMedia = q => ({matches:false, media:q, addListener(){}, removeListener(){}, addEventListener(){}, removeEventListener(){}});
  if (!window.scrollTo) window.scrollTo = () => {};
`;

async function egyOldal(fajl) {
  const hibak = [];
  const vc = new VirtualConsole();
  vc.on('jsdomError', e => hibak.push('jsdomError: ' + (e && e.message ? e.message : e)));
  vc.on('error', (...a) => hibak.push('console.error: ' + a.map(String).join(' ')));

  let dom;
  try {
    dom = await JSDOM.fromFile(fajl, {
      runScripts: 'dangerously',
      resources: 'usable',
      pretendToBeVisual: true,
      virtualConsole: vc,
      url: 'file://' + path.resolve(fajl),
      beforeParse(win) { win.eval(STUB); },
    });
  } catch (e) {
    return { fajl, betoltes_hiba: String(e && e.message ? e.message : e) };
  }

  await new Promise(r => setTimeout(r, 2500));
  const w = dom.window, d = w.document;

  const katex_db = d.querySelectorAll('.katex').length;
  const katex_hiba = [...d.querySelectorAll('.katex-error')]
    .slice(0, 5).map(e => (e.textContent || '').slice(0, 60));

  // Nyers $ a RENDERELT szövegben: ha a mat() nem futott le valahol, itt kiderül.
  const torzs = d.querySelector('main') || d.body;
  const klon = torzs.cloneNode(true);
  klon.querySelectorAll('.katex, script, style').forEach(e => e.remove());
  const szoveg = klon.textContent || '';
  const nyers_dollar = (szoveg.match(/\$/g) || []).length;
  const nyers_minta = nyers_dollar
    ? (szoveg.match(/.{0,30}\$.{0,30}/) || [''])[0].replace(/\s+/g, ' ')
    : '';

  // Kvíz-interakció. FONTOS: a `data-answer` a helyes opció **0-alapú INDEXE**
  // (nem a válasz szövege) — lásd quiz.js. A helyes gomb `helyes` osztályt kap,
  // és a scope `kviz-helyes` eseményt bocsát ki. A „változatos" kvíznél az
  // egyes `.valtozat` elemek hordozzák a saját data-answer-üket.
  const scope_ok = [];
  for (const k of d.querySelectorAll('.kviz')) {
    const valtozatok = k.querySelectorAll('.valtozat[data-answer]');
    if (valtozatok.length) valtozatok.forEach(v => scope_ok.push(v));
    else scope_ok.push(k);
  }
  let kviz_ok = 0; const kviz_rossz = [];
  for (const scope of scope_ok) {
    const gombok = [...scope.querySelectorAll('button')];
    const idx = parseInt(scope.getAttribute('data-answer'), 10);
    if (!gombok.length) { kviz_rossz.push('nincs gomb'); continue; }
    if (!Number.isInteger(idx) || idx < 0 || idx >= gombok.length) {
      kviz_rossz.push(`data-answer=${scope.getAttribute('data-answer')} nem érvényes index (${gombok.length} gomb)`);
      continue;
    }
    try {
      gombok[idx].dispatchEvent(new w.MouseEvent('click', { bubbles: true }));
      await new Promise(r => setTimeout(r, 30));
      if (gombok[idx].classList.contains('helyes')) kviz_ok++;
      else kviz_rossz.push(`a ${idx}. gomb nem lett „helyes"`);
    } catch (e) { kviz_rossz.push('klikk-hiba: ' + String(e.message || e).slice(0, 40)); }
  }
  const kviz_db = scope_ok.length;

  const out = {
    fajl, katex_db, katex_hiba, nyers_dollar, nyers_minta,
    kviz_db, kviz_ok, kviz_rossz: kviz_rossz.slice(0, 5),
    hibak: [...new Set(hibak)].slice(0, 5),
  };
  dom.window.close();
  return out;
}

// --- Szöveg-mód: a RENDERELT szöveg kiírása, ahogy a diák látja -------------
// A friss szemű tesztnél (web-verifikacio skill 3. rétege) a kontextus nélküli
// agentnek pontosan ezt kell megkapnia — HTML nélkül, KaTeX-szel renderelve.
// `--kulcs-nelkul`: a .vegeredmeny lenyílók kihagyva, a kulcsok külön a végén.
async function szovegMod(fajl, kulcsNelkul) {
  const vc = new VirtualConsole();
  const dom = await JSDOM.fromFile(fajl, {
    runScripts: 'dangerously', resources: 'usable', pretendToBeVisual: true,
    virtualConsole: vc, url: 'file://' + path.resolve(fajl),
    beforeParse(win) { win.eval(STUB); },
  });
  await new Promise(r => setTimeout(r, 2500));
  const d = dom.window.document;
  const torzs = d.querySelector('main') || d.body;
  const klon = torzs.cloneNode(true);
  // A .katex-mathml a KaTeX MathML-annotációja: ugyanazt a képletet még egyszer
  // tartalmazza, ezért a szövegben duplázódna („eˊs\text{és}eˊs"). Csak a
  // .katex-html vizuális változatot hagyjuk meg.
  klon.querySelectorAll('script, style, .lapozo, .lablec, #toc, .toc, .katex-mathml')
      .forEach(e => e.remove());
  const kulcsok = [];
  if (kulcsNelkul) {
    klon.querySelectorAll('.vegeredmeny').forEach(e => {
      const kartya = e.closest('[id]');
      kulcsok.push({ id: kartya ? kartya.id : '?', kulcs: (e.textContent || '').trim().replace(/\s+/g, ' ') });
      e.remove();
    });
  }
  // blokk-elemek után sortörés, hogy olvasható maradjon
  klon.querySelectorAll('h1,h2,h3,h4,p,li,tr,article,div.doboz,div.kviz,details').forEach(e => {
    e.insertAdjacentText('beforebegin', '\n');
  });
  const szoveg = (klon.textContent || '')
    .replace(/[ \t]+/g, ' ').replace(/\n\s*\n\s*\n+/g, '\n\n').trim();
  console.log('===== ' + fajl + ' =====');
  console.log(szoveg);
  if (kulcsNelkul && kulcsok.length) {
    console.log('\n===== VÉGEREDMÉNYEK (a friss szemű agentnek NEM adandó át) =====');
    for (const k of kulcsok) console.log(`#${k.id}: ${k.kulcs}`);
  }
  dom.window.close();
}

const argv = process.argv.slice(2);
const szoveg = argv.includes('--szoveg');
const kulcsNelkul = argv.includes('--kulcs-nelkul');
const fajlok = argv.filter(a => !a.startsWith('--'));

for (const f of fajlok) {
  try {
    if (szoveg) await szovegMod(f, kulcsNelkul);
    else console.log(JSON.stringify(await egyOldal(f)));
  } catch (e) {
    const h = String(e && e.message ? e.message : e);
    if (szoveg) console.error(`HIBA ${f}: ${h}`);
    else console.log(JSON.stringify({ fajl: f, betoltes_hiba: h }));
  }
}
