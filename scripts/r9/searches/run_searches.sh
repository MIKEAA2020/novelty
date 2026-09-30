#!/bin/bash
# R9 literature-pinning searches — queries verbatim as pre-registered.
cd /home/z/my-project/scripts/r9/searches || exit 1
run_q() {
  local n="$1"; local query="$2"; local out="q${n}.json"
  for attempt in 1 2 3; do
    if [ -s "$out" ] && python3 -c "import json,sys; d=json.load(open('$out')); sys.exit(0 if isinstance(d,list) and len(d)>0 else 1)" 2>/dev/null; then
      echo "q${n}: OK ($(python3 -c "import json; print(len(json.load(open('$out'))))" 2>/dev/null) results)"
      return 0
    fi
    z-ai function -n web_search -a "{\"query\": \"${query}\", \"num\": 8}" -o "$out" >/dev/null 2>&1
    sleep 15
  done
  echo "q${n}: DEGRADED — ${query}"
}
run_q 1  "Blanchet dipolar dark matter gravitational polarization internal force equation"
run_q 2  "Blanchet Le Tiec dipolar dark matter weak field limit MOND equivalence"
run_q 3  "dipolar dark matter phoenix model internal force dark energy"
run_q 4  "Berezhiani Khoury superfluid dark matter phonon effective field theory parameters"
run_q 5  "superfluid dark matter sound speed mass eV core radius galaxies"
run_q 6  "Khoury superfluid dark matter phonon baryon coupling MOND force"
run_q 7  "Verlinde emergent gravity apparent dark matter elastic medium displacement equation"
run_q 8  "Verlinde emergent gravity strain elastic modulus a0 8 pi G"
run_q 9  "dipolar dark matter time dependent response stability causal"
run_q 10 "superfluid dark matter causality superluminal speed of sound instability"
run_q 11 "emergent gravity dark matter response time Hubble delay test"
run_q 12 "Kramers-Kronig dispersion relation susceptibility dark matter medium causality"
echo "DONE"
