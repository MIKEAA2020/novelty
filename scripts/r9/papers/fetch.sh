#!/bin/bash
cd /home/z/my-project/scripts/r9/papers || exit 1
fetch() {
  local id="$1" name="$2"
  local out="${name}.json"
  if [ -s "$out" ] && python3 -c "import json;d=json.load(open('$out'));h=d.get('data',{}).get('html','');exit(0 if len(h)>50000 else 1)" 2>/dev/null; then echo "$name: cached"; return; fi
  for a in 1 2 3; do
    timeout 120 z-ai function -n page_reader -a "{\"url\": \"https://ar5iv.labs.arxiv.org/html/${id}\"}" -o "$out" >/dev/null 2>&1
    if [ -s "$out" ] && python3 -c "import json;d=json.load(open('$out'));h=d.get('data',{}).get('html','');exit(0 if len(h)>50000 else 1)" 2>/dev/null; then echo "$name: OK ($(python3 -c "import json;print(len(json.load(open('$out'))['data']['html']))" 2>/dev/null) chars)"; return; fi
    sleep 20
  done
  echo "$name: FAILED"
}
fetch 2105.02241 hertzberg_acausality
fetch 1507.01019 bk_superfluid_theory
fetch 0901.3114  blanchet_letiec_2009
fetch 1611.02269 verlinde_emergent
fetch 1701.07747 ddm_eft
fetch 2302.02690 no_polarization_bimetric
fetch 1506.07877 bk_galactic_dynamics
fetch 1909.05710 mistele_chemical_potential
fetch 2009.03003 mistele_three_problems
echo "FETCH ALL DONE"
