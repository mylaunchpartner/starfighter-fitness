"""Rebuild embed.html from site.html (the readable site), then bump version.json.
Usage: python3 tools/build_embed.py"""
import base64, gzip, io, json, pathlib, re
root = pathlib.Path(__file__).resolve().parent.parent
doc = (root / "site.html").read_text()
buf = io.BytesIO()
with gzip.GzipFile(fileobj=buf, mode="wb", mtime=0) as g:
    g.write(doc.encode())
payload = base64.b64encode(buf.getvalue()).decode()
emb = root / "embed.html"
html = re.sub(r'var PAYLOAD = "[^"]+"', lambda m: 'var PAYLOAD = "' + payload + '"', emb.read_text(), count=1)
emb.write_text(html)
vf = root / "version.json"
data = json.loads(vf.read_text())
v = data["v"] = data["v"] + 1
vf.write_text(json.dumps(data) + "\n")
print("embed.html rebuilt, version", v)
