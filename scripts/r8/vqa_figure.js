const ZAI = require('z-ai-web-dev-sdk').default;
const fs = require('fs');

async function main() {
  const zai = await ZAI.create();
  const b64 = fs.readFileSync('/home/z/my-project/download/R8_residual_census.png').toString('base64');
  const completion = await zai.chat.completions.create({
    messages: [
      {
        role: 'user',
        content: [
          { type: 'text', text: 'QA check this scientific figure. Answer in <=8 bullet points: (1) any cut-off or overlapping text/labels? (2) do all 3 panels show data correctly (scatter+curve, scatter+trendline, horizontal bars)? (3) are the red dashed floor lines visible in panel c? (4) any rendering artifacts or blank areas? Be strict and specific.' },
          { type: 'image_url', image_url: { url: `data:image/png;base64,${b64}` } }
        ]
      }
    ],
    thinking: { type: 'disabled' }
  });
  console.log(completion.choices[0]?.message?.content);
}
main().catch(e => { console.error('ERR', e.message); process.exit(1); });
