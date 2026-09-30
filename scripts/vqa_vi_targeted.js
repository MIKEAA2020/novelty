// Targeted visual QA for the changed final pages (18-19) of Volume VI.
const fs = require('fs');
async function main() {
  const mkreq = require('module').createRequire('/home/z/.bun/install/global/node_modules/');
  const ZAI = mkreq('z-ai-web-dev-sdk').default || mkreq('z-ai-web-dev-sdk');
  const zai = await ZAI.create();
  const files = ['qa15/p18.png', 'qa15/p19.png'];
  const prompt = (
    'You are a strict PDF layout QA reviewer. For each page image, check: ' +
    '(1) text overlapping other text or rules/lines; (2) content cut off at ' +
    'page edges; (3) tables overflowing their margins; (4) garbled or tofu ' +
    'characters. Answer per image, exactly one line each: "Image N: PASS" ' +
    'or "Image N: FAIL - reason".');
  const content = [{ type: 'text', text: prompt + ' (2 images)' }];
  for (const f of files) {
    const b64 = fs.readFileSync('/home/z/my-project/novelty/scripts/' + f).toString('base64');
    content.push({ type: 'image_url', image_url: { url: 'data:image/png;base64,' + b64 } });
  }
  const res = await zai.chat.completions.createVision({
    model: 'glm-5v-turbo', messages: [{ role: 'user', content }], temperature: 0.1 });
  console.log(res.choices[0].message.content);
}
main().catch(e => { console.error(e); process.exit(1); });
