// Targeted diagram inspection: 3 full-resolution bands.
const fs = require('fs');
const path = require('path');
const mkreq = require('module').createRequire('/home/z/.bun/install/global/node_modules/');
const ZAI = mkreq('z-ai-web-dev-sdk').default || mkreq('z-ai-web-dev-sdk');

async function main() {
  const zai = await ZAI.create();
  const dir = '/home/z/my-project/scripts/qa9';
  const bands = ['diag_band1.png', 'diag_band2.png', 'diag_band3.png'];
  const prompt = (
    'This is one horizontal band of a process diagram at full resolution. ' +
    'Check carefully: does ANY text overlap other text, cross a box border, ' +
    'or get cut off at a box edge? Are all boxes and arrows intact? ' +
    'Answer: "BAND: OK" or "BAND: PROBLEM - <precise description>".');
  const content = [{ type: 'text', text: prompt + ' (3 bands)' }];
  for (const f of bands) {
    const b64 = fs.readFileSync(path.join(dir, f)).toString('base64');
    content.push({ type: 'image_url', image_url: { url: 'data:image/png;base64,' + b64 } });
  }
  const res = await zai.chat.completions.createVision({
    model: 'glm-5v-turbo',
    messages: [{ role: 'user', content }],
    temperature: 0.1,
  });
  console.log(res.choices[0].message.content);
}
main().catch(e => { console.error(e); process.exit(1); });
