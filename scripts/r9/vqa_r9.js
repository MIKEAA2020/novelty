// Visual QA for the R9 figure via z-ai-web-dev-sdk (glm-5v-turbo).
const fs = require('fs');
async function main() {
  const mkreq = require('module').createRequire('/home/z/.bun/install/global/node_modules/');
  const ZAI = mkreq('z-ai-web-dev-sdk').default || mkreq('z-ai-web-dev-sdk');
  const zai = await ZAI.create();
  const b64 = fs.readFileSync('/home/z/my-project/download/R9_analyticity.png').toString('base64');
  const res = await zai.chat.completions.createVision({
    model: "glm-5v-turbo",
    temperature: 0.1,
    messages: [{ role: 'user', content: [
      { type: 'text', text: 'QA this scientific figure strictly. Check: (1) any overlapping text/labels/markers? (2) any clipped or cut-off text at panel edges? (3) are the three panels — (a) a pole map with a shaded upper half plane, (b) Kramers-Kronig verification curves, (c) a response-time chart with a shaded vertical window — each readable? (4) any empty or broken panel? Answer as a terse checklist with PASS/FAIL per item and one-line reasons.' },
      { type: 'image_url', image_url: { url: `data:image/png;base64,${b64}` } }
    ]}]
  });
  console.log(res.choices[0].message.content);
}
main().catch(e => { console.error('VQA FAIL:', e.message); process.exit(1); });
