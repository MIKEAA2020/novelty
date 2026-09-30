#!/usr/bin/env python3
"""Gen3 arXiv API sweep — calibration + the memory-cell occupation check."""
import re, time, urllib.request, urllib.parse

BASE = "https://export.arxiv.org/api/query?search_query={}&max_results={}"

def query(q, n=6):
    url = BASE.format(urllib.parse.quote(q), n)
    with urllib.request.urlopen(url, timeout=30) as r:
        xml = r.read().decode("utf-8", "ignore")
    total = re.search(r"totalResults>(\d+)<", xml)
    entries = re.findall(r"<entry>(.*?)</entry>", xml, re.S)
    out = []
    for e in entries:
        t = re.search(r"<title>(.*?)</title>", e, re.S)
        d = re.search(r"<published>(.*?)</published>", e)
        i = re.search(r"<id>(.*?)</id>", e)
        out.append((" ".join(t.group(1).split()) if t else "?",
                    d.group(1)[:10] if d else "?", i.group(1) if i else "?"))
    return int(total.group(1)) if total else -1, out

QUERIES = [
    ("CALIBRATION", 'all:"viscoelastic"'),
    ("CALIBRATION", 'ti:"viscoelastic"'),
    ("cell: loop", 'all:"hysteresis" AND all:"radial acceleration"'),
    ("cell: loop", 'all:"hysteresis" AND all:"galaxy" AND all:"dark matter"'),
    ("cell: path", 'all:"path dependent" AND all:"galaxy" AND all:"scaling relation"'),
    ("cell: viscodM", 'all:"viscoelastic" AND all:"dark matter"'),
    ("cell: viscodM", 'ti:"viscoelastic dark matter"'),
    ("cell: Maxwell", 'all:"Maxwell time" AND all:"dark matter"'),
    ("cell: memory", 'all:"memory" AND all:"radial acceleration relation"'),
    ("cell: lag", 'abs:"response time" AND abs:"radial acceleration relation"'),
    ("cell: phase", 'abs:"phase lag" AND abs:"dark matter" AND abs:"galaxy"'),
]

for tag, q in QUERIES:
    try:
        total, entries = query(q)
        print("[%s] %s  -> total=%d" % (tag, q, total))
        for t, d, i in entries:
            print("   - %s | %s | %s" % (t[:100], d, i.split("/abs/")[-1] if "/abs/" in i else i))
    except Exception as e:
        print("[%s] %s  -> ERROR %s" % (tag, q, e))
    time.sleep(3)
