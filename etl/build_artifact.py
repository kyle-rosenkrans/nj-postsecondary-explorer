#!/usr/bin/env python3
"""Emit the artifact build of the explorer.

A published Artifact supplies its own <!doctype>/<html>/<head>/<body>, so this
strips the document wrapper from app/template.html and emits body-level content
only. <title> is written first so it stays inside the 8KB the publisher scans.

Usage: python3 etl/build_artifact.py [outfile]
"""
import json, pathlib, re, sys

root = pathlib.Path(__file__).resolve().parent.parent
tpl = (root / "app" / "template.html").read_text()

title = re.search(r"<title>(.*?)</title>", tpl, re.S).group(1).strip()
style = re.search(r"<style>(.*?)</style>", tpl, re.S).group(1)
body  = re.search(r"<body>(.*?)</body>", tpl, re.S).group(1).strip()

panel = json.dumps(json.loads((root / "data" / "panel.json").read_text()),
                   separators=(",", ":"), ensure_ascii=False)
panel = panel.replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026")

out = f"<title>{title}</title>\n<style>{style}</style>\n{body}\n".replace("__PANEL_JSON__", panel)

dest = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else root / "artifact_build.html"
dest.write_text(out)
head = out[:8192]
print(f"wrote {dest}  ({dest.stat().st_size/1e6:.2f} MB)")
print(f"  title in first 8KB: {'<title>' in head}")
# match real tags only — <header> must not trip the <head> check
for tag in ("!doctype", "html", "head", "body"):
    hit = re.search(rf"<\s*/?\s*{tag}[\s>]", out, re.I)
    assert not hit, f"document wrapper leaked: {hit.group(0)!r}"
print("  no document wrapper: ok")
