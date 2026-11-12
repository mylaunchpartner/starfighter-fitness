# GHL snippet: Starfighter Fitness (starfighterfitness.com)

GHL: sub-account **Starfighter Fitness** → Sites → Funnels/Websites → Starfighter Fitness → Home → the one Custom HTML/Javascript element. It holds the contents of `ghl-snippet.html`:

- a `<noscript>` copy of the page text and links (`seo-copy.html`), so search engines and AI crawlers that don't run JavaScript can read the whole page. Visitors never see it.
- the loader, which pulls the live site (`embed.html`) from this repo.

The site itself runs in a sandboxed iframe, so the crawlable copy has to live in GHL.

## Macro Calculator page (/macro-calculator)
Same sub-account → Starfighter Fitness → **Macro Calculator** page → its one Custom HTML/Javascript element:

```html
<div id="sf-macro-root" data-v="0"></div>
<script src="https://mylaunchpartner.github.io/starfighter-fitness/loader.js" data-root="sf-macro-root" data-file="macro-calculator.html" data-vkey="macro"></script>
```
Edit `macro-calculator.html`, bump `macro` in `version.json`, commit.

## Making a change (home page)
1. Edit `site.html` (the readable site).
2. Run `python3 tools/build_embed.py`: it rebuilds the gzip payload in `embed.html` and bumps `version.json`.
3. Run `python3 tools/build_seo.py` and rebuild `ghl-snippet.html` (wrap `seo-copy.html` as in the current file).
4. Commit. Visitors get the change within ~5 minutes. If the text, headings, links or contact details changed, re-paste `ghl-snippet.html` into GHL and Publish so crawlers see it too.
