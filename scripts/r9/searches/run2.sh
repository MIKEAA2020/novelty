#!/bin/bash
cd /home/z/my-project/scripts/r9/searches || exit 1
declare -A Q
Q[2]="Blanchet Le Tiec dipolar dark matter weak field limit MOND"
Q[3]="dipolar dark matter phoenix model internal force dark energy"
Q[4]="Berezhiani Khoury superfluid dark matter phonon effective field theory"
Q[5]="superfluid dark matter sound speed mass eV core radius galaxies"
Q[6]="Khoury superfluid dark matter phonon baryon coupling MOND"
Q[7]="Verlinde emergent gravity apparent dark matter elastic medium displacement"
Q[8]="Verlinde emergent gravity strain elastic modulus dark matter medium"
Q[9]="dipolar dark matter time dependent response stability"
Q[10]="superfluid dark matter causality superluminal speed of sound"
Q[11]="emergent gravity dark matter response time delay test"
Q[12]="Kramers-Kronig dispersion relation dark matter medium causal susceptibility"
for n in 2 3 4 5 6 7 8 9 10 11 12; do
  out="q${n}.json"
  if [ -s "$out" ] && python3 -c "import json,sys;d=json.load(open('$out'));sys.exit(0 if isinstance(d,list) and len(d)>0 else 1)" 2>/dev/null; then echo "q${n}: cached"; continue; fi
  ok=0
  for attempt in 1 2 3 4 5; do
    timeout 90 z-ai function -n web_search -a "{\"query\": \"${Q[$n]}\", \"num\": 8}" -o "$out" >/dev/null 2>&1
    if [ -s "$out" ] && python3 -c "import json,sys;d=json.load(open('$out'));sys.exit(0 if isinstance(d,list) and len(d)>0 else 1)" 2>/dev/null; then ok=1; break; fi
    sleep 25
  done
  if [ $ok -eq 1 ]; then echo "q${n}: OK ($(python3 -c "import json;print(len(json.load(open('$out'))))" 2>/dev/null) results)"; else echo "q${n}: DEGRADED"; fi
done
echo "ALL DONE"
