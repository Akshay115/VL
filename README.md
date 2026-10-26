# VL Dubai — Fashion Photoshoot Website

A static, multi-page website for **VL Dubai**, a fully styled fashion photoshoot experience in Dubai. Built from the Figma design *VL DUBAI — Fashion Photoshoot Website*, using its page layouts, copy and photo assets.

## Pages

| Page | File | Figma frame |
|---|---|---|
| Home | `index.html` | page_01 — Dubai Fashion Photoshoot |
| Experience | `experience.html` | page_02 — Not Just a Photoshoot |
| Locations | `locations.html` | page_03 — Choose Your Dubai |
| Looks | `looks.html` | page_04 — Your Look |
| How It Works | `how-it-works.html` | page_05 — How It Works + client experiences |
| What's Included | `included.html` | page_06 — Included, add-ons, Ready? |
| Stories & FAQ | `stories.html` | page_07 — Client Stories, Good to Know, Your Dubai Story Awaits |

## Structure

```
assets/
  style.css     shared design system (colours, type, layout, responsive)
  main.js       sticky header, mobile menu, scroll reveal
  img/          photo crops exported from Figma
build.py        generates the HTML pages (shared header/footer)
*.html          generated pages
```

- Fonts: Cormorant Garamond (display), Montserrat (body), Mrs Saint Delafield (script). All are loaded from Google Fonts.
- Palette: `#111111` background, `#f3eee7` cream text, `#1d3412` WhatsApp-green CTA.
- Every "Book Your Shoot" button opens WhatsApp. To add a business number, change the `WA` constant in `build.py` (for example `https://wa.me/9715XXXXXXXX?text=...`) and rebuild.

## Development

```bash
python3 build.py              # regenerate the HTML pages after edits
python3 -m http.server 8000   # preview at http://localhost:8000
```

There is no build step for deployment. The site is plain static HTML/CSS/JS.

## Deployment

The site deploys to **Vercel** through the GitHub integration. Every push to `main` triggers a production deployment, and pushes to other branches create preview deployments.
