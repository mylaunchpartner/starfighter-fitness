# Starfighter Fitness website

Source for starfighterfitness.com, which runs from a short snippet in GoHighLevel. Made and maintained by My Launch Partner.

| File | What it is |
|---|---|
| `site.html` | The readable, editable site |
| `embed.html` | GHL embed: `site.html` gzip-packed into a sandboxed iframe (built by `tools/build_embed.py`) |
| `macro-calculator.html` | The /macro-calculator page (calorie and macro calculator) |
| `version.json` | `v` = home page (bumped by the build script), `macro` = calculator (bump by hand) |
| `loader.js` | Called by the GHL snippet; loads the latest `embed.html` |
| `seo-copy.html` | Crawlable text copy of the site (built by `tools/build_seo.py`) |
| `ghl-snippet.html` | Exactly what goes in the GHL Custom Code element on the home page |
| `GHL-SNIPPET.md` | What sits in GHL and when to re-paste it |
