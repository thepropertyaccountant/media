from playwright.sync_api import sync_playwright
import sys, pathlib
src = pathlib.Path(sys.argv[1]).resolve()
prefix = sys.argv[2]
n = int(sys.argv[3])
with sync_playwright() as p:
    b = p.chromium.launch(args=["--font-render-hinting=none"])
    pg = b.new_page(viewport={"width":1080,"height":1350}, device_scale_factor=1)
    pg.goto(f"file://{src}")
    pg.wait_for_timeout(1500)
    for i in range(1, n+1):
        el = pg.query_selector(f"#s{i}")
        out = f"{prefix}-{i:02d}.png"
        el.screenshot(path=out)
        print("wrote", out)
    b.close()
