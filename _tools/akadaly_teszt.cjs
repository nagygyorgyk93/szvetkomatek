/* Szvetkó matek — axe-core ellenőrzés helyi Playwright-böngészőben.
   Előfeltétel: playwright és axe-core Node-csomag, szükség esetén NODE_PATH;
   CHROMIUM_PATH: a telepített Chromium/Edge elérési útja.
   Használat a repó gyökeréből:
     node _tools/akadaly_teszt.cjs
     node _tools/akadaly_teszt.cjs 3e/ --szelessegek=390,1280 --json=C:/QA/akadaly.json
   A külső kéréseket blokkolja; az axe WCAG 2.1 A/AA és best-practice szabályait futtatja.
   Nem helyettesít valódi képernyőolvasós, tartalmi vagy teljes kontrasztvizsgálatot.
   Kilépési kód: 0 tiszta, 1 jelzés, 2 eszköz-/betöltési hiba. */
'use strict';
const fs = require('fs'), path = require('path'), http = require('http');
let chromium, axePath, axeVersion;
try {
  ({ chromium } = require('playwright'));
  axePath = require.resolve('axe-core/axe.min.js');
  axeVersion = require('axe-core/package.json').version;
} catch(e) {
  console.error('Hiányzó Playwright vagy axe-core. Telepítsd a csomagokat, vagy állítsd be a NODE_PATH-ot.');
  process.exit(2);
}
const repo = path.resolve(__dirname, '..');
const skip = new Set(['_tools','_sablonok','_docs','_layout','assets','node_modules','.git','.github','.claude']);
function walk(dir) {
  return fs.readdirSync(dir, {withFileTypes:true}).flatMap(e => {
    const p = path.join(dir,e.name);
    return e.isDirectory() ? (skip.has(e.name) ? [] : walk(p)) : e.name.endsWith('.html') ? [path.relative(repo,p).replaceAll('\\','/')] : [];
  });
}
const args = process.argv.slice(2);
const widths = (args.find(x=>x.startsWith('--szelessegek='))?.split('=')[1] || '390,1280').split(',').map(Number);
const patterns = args.filter(x=>!x.startsWith('--'));
const pages = walk(repo).sort().filter(p=>!patterns.length || patterns.some(s=>s==='.' || p===s || p.startsWith(s.replaceAll('\\','/').replace(/\/$/,'')+'/')));
const out = args.find(x=>x.startsWith('--json='))?.slice(7);
if(!pages.length || widths.some(w=>!Number.isInteger(w)||w<240)) {console.error('Érvénytelen lapminta vagy szélesség.');process.exit(2);}
const mime = {'.html':'text/html; charset=utf-8','.js':'text/javascript','.css':'text/css','.json':'application/json','.woff2':'font/woff2','.svg':'image/svg+xml','.webp':'image/webp','.mp4':'video/mp4','.webm':'video/webm'};
const server = http.createServer((req,res) => {
  let p;
  try {p=path.resolve(repo, '.'+decodeURIComponent(new URL(req.url,'http://localhost').pathname));}
  catch(e) {res.writeHead(400);res.end();return;}
  if(!p.startsWith(repo+path.sep)){res.writeHead(403);res.end();return;}
  fs.readFile(p,(err,data)=>{if(err){res.writeHead(404);res.end();return;}res.setHeader('Content-Type',mime[path.extname(p)]||'application/octet-stream');res.end(data);});
});
function rovid(v) {
  return {id:v.id,impact:v.impact,tags:v.tags,help:v.help,helpUrl:v.helpUrl,
    nodes:v.nodes.map(n=>({target:n.target,html:n.html,failureSummary:n.failureSummary,
      checks:[...n.any,...n.all,...n.none].map(c=>({id:c.id,message:c.message,data:c.data}))}))};
}
(async()=>{
  let browser;
  const results=[];
  try {
    await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));
    const base='http://127.0.0.1:'+server.address().port+'/';
    browser=await chromium.launch(process.env.CHROMIUM_PATH ? {executablePath:process.env.CHROMIUM_PATH} : {});
    const jobs=pages.flatMap(page=>widths.map(width=>({page,width})));let next=0;
    async function worker() {
      const context=await browser.newContext();
      await context.route('**/*',r=>r.request().url().startsWith(base)?r.continue():r.abort());
      const page=await context.newPage();
      while(next<jobs.length) {
        const job=jobs[next++];
        try {
          await page.setViewportSize({width:job.width,height:900});
          await page.goto(base+job.page,{waitUntil:'load'});
          await page.waitForTimeout(3200);
          await page.addScriptTag({path:axePath});
          const run=await page.evaluate(async()=>{
            const r=await axe.run({runOnly:{type:'tag',values:['wcag2a','wcag2aa','wcag21a','wcag21aa','best-practice']}});
            const names=Array.from(document.querySelectorAll('.opciok button[aria-label],th[aria-label]')).map(el=>({
              tex:Array.from(el.querySelectorAll('annotation[encoding="application/x-tex"]')).map(x=>x.textContent).join(' ; '),name:el.getAttribute('aria-label')}));
            return {violations:r.violations,incomplete:r.incomplete,passes:r.passes.map(x=>x.id),names};
          });
          results.push({...job,violations:run.violations.map(rovid),incomplete:run.incomplete.map(rovid),passes:run.passes,names:run.names});
        } catch(e) {results.push({...job,error:String(e)});}
        if(results.length%40===0) console.log('Ellenőrizve: '+results.length+'/'+jobs.length);
      }
      await context.close();
    }
    await Promise.all([worker(),worker(),worker(),worker()]);
    const rules={};
    for(const r of results) for(const v of r.violations||[]) {
      const s=rules[v.id] ||= {scenarios:0,nodes:0,impact:v.impact,examplePage:r.page};
      s.scenarios++;s.nodes+=v.nodes.length;
    }
    const errors=results.filter(x=>x.error);
    const summary={pages:pages.length,widths,scenarios:results.length,errors,rules};
    if(out)fs.writeFileSync(path.resolve(out),JSON.stringify({date:new Date().toISOString(),axeVersion,summary,results},null,2));
    console.log(JSON.stringify(summary,null,2));
    process.exitCode=errors.length?2:Object.keys(rules).length?1:0;
  } catch(e) {console.error(String(e));process.exitCode=2;}
  finally {if(browser)await browser.close();server.close();}
})();
