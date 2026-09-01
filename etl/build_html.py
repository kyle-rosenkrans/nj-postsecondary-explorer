#!/usr/bin/env python3
"""Inject data/panel.json into app/template.html -> Postsecondary_Explorer.html."""
import json, pathlib

root = pathlib.Path(__file__).resolve().parent.parent
tpl = (root / "app" / "template.html").read_text()
panel = json.loads((root / "data" / "panel.json").read_text())

# Compact, and neutralise anything that could close the host <script> tag.
blob = json.dumps(panel, separators=(",", ":"), ensure_ascii=False)
blob = blob.replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026")

out = tpl.replace("__PANEL_JSON__", blob)
dest = root / "Postsecondary_Explorer.html"
dest.write_text(out)
print(f"wrote {dest.name}  ({dest.stat().st_size/1e6:.2f} MB)")
