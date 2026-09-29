const fs = require('fs');
const mkreq = require('module').createRequire('/home/z/.bun/install/global/node_modules/');
const ZAI = mkreq('z-ai-web-dev-sdk').default || mkreq('z-ai-web-dev-sdk');
async function main() {
  const zai = await ZAI.create();
  const prompt = ('These are two report pages rendered at 200 dpi, containing dense coding-matrix ' +
    'tables. Answer these questions PRECISELY for each image, one line each:\n' +
    'Q1: Is any table cell text CLIPPED/TRUNCATED (letters missing)? yes/no\n' +
    'Q2: Does any table extend past the printed page margin into the margin zone? yes/no\n' +
    'Q3: Are the column codes (S, P, F, S then D) fully readable? yes/no\n' +
    'Format: "Image N: Q1 yes/no, Q2 yes/no, Q3 yes/no - comment"');
  const content = [{ type: 'text', text: prompt }];
  for (const f of ['hi_t3.png', 'hi_t4.png']) {
    const b64 = fs.readFileSync('/home/z/my-project/scripts/qa9/' + f).toString('base64');
    content.push({ type: 'image_url', image_url: { url: 'data:image/png;base64,' + b64 } });
  }
  const res = await zai.chat.completions.createVision({ model: 'glm-5v-turbo', messages: [{ role: 'user', content }], temperature: 0.1 });
  console.log(res.choices[0].message.content);
}
main().catch(e => { console.error(e); process.exit(1); });
