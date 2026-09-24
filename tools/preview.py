# Generated asset builder. Run from the repository root: python3 tools/preview.py
import json, re, subprocess, pathlib
md = open("README.md", encoding="utf-8").read()
out = subprocess.run(["gh", "api", "/markdown", "--input", "-"],
                     input=json.dumps({"text": md, "mode": "gfm", "context": "anggastudio/anggastudio"}),
                     capture_output=True, text=True)
html = out.stdout

def inline(m):
    src = m.group(1)
    p = pathlib.Path(src)
    if not p.exists():
        return m.group(0)
    svg = p.read_text(encoding="utf-8")
    svg = re.sub(r'\swidth="\d+"\s', ' ', svg, count=1)
    return svg.replace("<svg ", '<svg style="max-width:100%;height:auto;display:block;margin:0 auto" ', 1)

# GitHub rewrites relative srcs to camo/raw urls; map them back to local files
html = re.sub(r'<picture>.*?</picture>', lambda m: m.group(0), html, flags=re.S)
html = re.sub(r'<img[^>]*?src="[^"]*?(assets/[a-z\-]+\.svg)"[^>]*>', inline, html)
html = re.sub(r'<source[^>]*>', '', html)
page = """<!doctype html><meta charset="utf-8">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/github-markdown-css@5/github-markdown.min.css">
<style>body{margin:0;background:#fff}.markdown-body{box-sizing:border-box;max-width:900px;margin:0 auto;padding:28px}
.markdown-body p[align=center] svg{display:inline-block!important;margin:2px}</style>
<article class="markdown-body">%s</article>""" % html
open("preview.html", "w", encoding="utf-8").write(page)
print("rc", out.returncode, "inlined svgs:", html.count("<svg"))
