# GHL snippet: Starfighter Fitness (starfighterfitness.com)

GHL: sub-account **Starfighter Fitness** → Sites → Funnels/Websites → Starfighter Fitness → Home → the one Custom HTML/Javascript element. It holds only this snippet:

```html
<div id="sf-fit-root" data-v="0"><noscript><p style="font-family:system-ui,sans-serif;font-size:15px;color:#6E7480;padding:24px;text-align:center;">Starfighter Fitness: online longevity coaching, nationwide. Call (928) 549-8006 or email info@starfighterfitness.com to book a strategy call.</p></noscript></div>
<script src="https://mylaunchpartner.github.io/starfighter-fitness/loader.js" data-root="sf-fit-root"></script>
```

The site itself always loads from this repo (it runs in a sandboxed iframe, so there was never crawlable page text to keep in GHL).

## Making a change
1. Edit `site.html` (the readable site).
2. Run `python3 tools/build_embed.py`: it rebuilds the gzip payload in `embed.html` and bumps `version.json`.
3. Commit. Live within ~5 minutes; no GHL re-paste needed (only re-paste if the noscript text changes).
