# Starfighter Fitness website

Source for starfighterfitness.com, which runs from a short snippet in GoHighLevel. Made and maintained by My Launch Partner.

| File | What it is |
|---|---|
| `site.html` | The readable, editable site |
| `embed.html` | GHL embed: `site.html` gzip-packed into a sandboxed iframe (built by `tools/build_embed.py`) |
| `version.json` | Bumped by the build script |
| `loader.js` | Called by the GHL snippet; loads the latest `embed.html` |
| `GHL-SNIPPET.md` | What sits in GHL |
