#!/bin/bash
# Gen3 (third generation) occupation searches — the eight queries verbatim as
# pre-registered in worklog Task 18 (commit f5c6c3e), run AFTER the derivations.
cd /home/z/my-project/scripts/gen3/searches || exit 1
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
run_q 1  "hysteresis radial acceleration relation galaxies dark matter"
run_q 2  "path dependent memory galaxy scaling relations dark matter"
run_q 3  "viscoelastic dark matter"
run_q 4  "Maxwell time relaxation creep dark matter halo"
run_q 5  "post starburst galaxies rotation curves offset radial acceleration"
run_q 6  "time varying baryonic potential feedback halo response radial acceleration relation scatter origin"
run_q 7  "phase lag dissipation dark matter medium response galaxies"
run_q 8  "fine tuning naturalness slow response dark matter halo relaxation time"
echo "DONE"
