// Visual QA for Amendment A4d pages via z-ai-web-dev-sdk (glm-5v-turbo).
const fs = require('fs');
const path = require('path');

async function main() {
  const mkreq = require('module').createRequire('/home/z/.bun/install/global/node_modules/');
  const ZAI = mkreq('z-ai-web-dev-sdk').default || mkreq('z-ai-web-dev-sdk');
  const zai = await ZAI.create();
  const dir = '/home/z/my-project/scripts/qa9';
  const files = fs.readdirSync(dir).filter(f => f.endsWith('.png')).sort();
  const prompt = (
    'You are a strict PDF layout QA reviewer. For each page image, check: ' +
    '(1) text overlapping other text or rules/lines; (2) content cut off at ' +
    'page edges; (3) tables overflowing their margins or colliding with ' +
    'body text; (4) large meaningless blank areas (>40% of the page empty ' +
    'mid-document); (5) garbled or tofu characters. Answer per image, ' +
    'exactly one line each: "Image N: PASS" or "Image N: FAIL - reason".');
  const out = [];
  for (let b = 0; b < Math.ceil(files.length / 4); b++) {
    const batch = files.slice(b * 4, b * 4 + 4);
    const content = [{ type: 'text', text: prompt + ' (' + batch.length + ' images)' }];
    for (const f of batch) {
      const b64 = fs.readFileSync(path.join(dir, f)).toString('base64');
      content.push({ type: 'image_url', image_url: { url: 'data:image/png;base64,' + b64 } });
    }
    const res = await zai.chat.completions.createVision({
      model: 'glm-5v-turbo',
      messages: [{ role: 'user', content }],
      temperature: 0.1,
    });
    const txt = res.choices[0].message.content;
    console.log(`--- batch ${b + 1} (${batch[0]}..${batch[batch.length - 1]}) ---`);
    console.log(txt);
    out.push({ batch: b + 1, files: batch, response: txt });
  }
  fs.writeFileSync('/home/z/my-project/scripts/qa9/vqa.json', JSON.stringify(out, null, 2));
  console.log('saved vqa.json');
}
main().catch(e => { console.error(e); process.exit(1); });
