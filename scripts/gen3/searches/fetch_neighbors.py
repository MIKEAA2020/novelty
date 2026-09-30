#!/usr/bin/env python3
"""Fetch and print the abstracts of the three nearest neighbors, to bound them."""
import re, urllib.request

ARXIV = "https://export.arxiv.org/api/query?id_list=2510.09751"

try:
    with urllib.request.urlopen(ARXIV, timeout=30) as r:
        xml = r.read().decode("utf-8", "ignore")
    t = re.search(r"<title>(.*?)</title>", xml[xml.find("<entry>"):], re.S)
    s = re.search(r"<summary>(.*?)</summary>", xml, re.S)
    print("2510.09751 TITLE:", " ".join(t.group(1).split()))
    print("ABSTRACT:", " ".join(s.group(1).split())[:1400])
except Exception as e:
    print("arxiv fetch error:", e)
