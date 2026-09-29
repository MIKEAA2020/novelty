#!/usr/bin/env python3
"""Screenshot an HTML element to PNG at 2x device scale (300dpi-equivalent)
for embedding into ReportLab documents as a block-level Image flowable.
Sanctioned by pdf skill SKILL.md 'Diagram Generation Strategy' (Report route:
Playwright+CSS -> PNG -> Image())."""
import sys
from playwright.sync_api import sync_playwright


def shoot(html_path: str, out_png: str, selector: str = ".canvas") -> None:
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(device_scale_factor=2, viewport={"width": 1400, "height": 1200})
        page.goto(f"file://{html_path}")
        page.wait_for_load_state("networkidle")
        page.wait_for_timeout(600)  # let webfonts settle
        el = page.query_selector(selector)
        if el is None:
            raise SystemExit(f"selector {selector} not found in {html_path}")
        el.screenshot(path=out_png)
        browser.close()
    print(f"saved: {out_png}")


if __name__ == "__main__":
    html = sys.argv[1] if len(sys.argv) > 1 else "/home/z/my-project/scripts/diagram.html"
    out = sys.argv[2] if len(sys.argv) > 2 else "/home/z/my-project/scripts/diagram.png"
    sel = sys.argv[3] if len(sys.argv) > 3 else ".canvas"
    shoot(html, out, sel)
