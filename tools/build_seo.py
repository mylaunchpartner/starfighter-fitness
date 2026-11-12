"""Build seo-copy.html: a plain, crawlable copy of site.html's text and links.
It goes inside <noscript> in the GHL snippet so search engines and AI crawlers
that don't run JavaScript can read the page. Visitors never see it.
Usage: python3 tools/build_seo.py"""
import pathlib, re
root = pathlib.Path(__file__).resolve().parent.parent
s = (root / "site.html").read_text()
title = re.search(r"<title>(.*?)</title>", s, re.S).group(1).strip()
body = re.search(r"<body[^>]*>(.*)</body>", s, re.S).group(1)
for t in ["script", "style", "svg", "noscript", "template", "button", "iframe"]:
    body = re.sub(r"<%s\b[\s\S]*?</%s>" % (t, t), "", body)
body = re.sub(r"<!--[\s\S]*?-->", "", body)
body = re.sub(r"<(input|img)\b[^>]*>", "", body)
body = re.sub(r"</?(div|span)\b[^>]*>", " ", body)
KEEP = ("href", "id", "target", "rel", "aria-label")
def clean(m):
    tag, rest = m.group(1), m.group(2) or ""
    kept = "".join(mm.group(0) for a in KEEP for mm in [re.search(r'\s%s="[^"]*"' % a, rest)] if mm)
    return "<%s%s>" % (tag, kept)
body = re.sub(r"<([a-zA-Z][a-zA-Z0-9]*)(\s[^>]*?)?/?>", clean, body)
body = re.sub(r"[ \t]+", " ", body)
body = re.sub(r"\s*\n\s*", "\n", body).strip()
for _ in range(3):
    body = re.sub(r"<(p|li|ul|ol|a|section|header|footer|nav|main|h\d|strong|em|b|small|sub|dl|dt|dd)\b[^>]*>\s*</\1>", "", body)
out = "<noscript><main>\n<!-- " + title + " -->\n" + body + "\n</main></noscript>\n"
(root / "seo-copy.html").write_text(out)
print("seo-copy.html:", len(out), "bytes")
