import os, sys
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))
WA = "https://wa.me/?text=Hi%20VL%20Dubai%2C%20I%27d%20like%20to%20book%20a%20fashion%20photoshoot."

PAGES = [
    ("index.html", "Home"),
    ("experience.html", "Experience"),
    ("locations.html", "Locations"),
    ("looks.html", "Looks"),
    ("how-it-works.html", "How It Works"),
    ("included.html", "What's Included"),
    ("stories.html", "Stories & FAQ"),
]

ICON = {
 "hanger": '<svg viewBox="0 0 48 48"><path d="M24 14a4 4 0 1 1 4 4c-2 0-4 1.5-4 3.5v1L5 34h38L24 22.5"/></svg>',
 "dress": '<svg viewBox="0 0 48 48"><path d="M24 4v4M18 8h12l-2 10 6 22H14l6-22-2-10z"/><path d="M20 18h8"/></svg>',
 "pin": '<svg viewBox="0 0 48 48"><path d="M24 44s14-14 14-25a14 14 0 0 0-28 0c0 11 14 25 14 25z"/><circle cx="24" cy="19" r="5"/></svg>',
 "camera": '<svg viewBox="0 0 48 48"><rect x="5" y="13" width="38" height="26" rx="3"/><path d="M17 13l3-5h8l3 5"/><circle cx="24" cy="26" r="8"/><circle cx="37" cy="18" r="1"/></svg>',
 "wa": '<svg viewBox="0 0 48 48"><path d="M24 4a20 20 0 0 0-17.3 30L4 44l10.3-2.7A20 20 0 1 0 24 4z"/><path d="M17 15c-1 0-3 2-2 6 1.5 5 7 11 12 12 4 1 6-1 6-2.5l-.5-2-4-2-2 2c-3-1-6-4-7-7l2-2-2-4z"/></svg>',
 "brush": '<svg viewBox="0 0 48 48"><path d="M30 6l12 12-16 10-6-6zM20 22l-12 14 4 4 14-12"/></svg>',
 "car": '<svg viewBox="0 0 48 48"><path d="M4 30v-6l6-2 6-6h16l8 6 4 2v6H4z"/><circle cx="13" cy="31" r="3"/><circle cx="35" cy="31" r="3"/></svg>',
 "play": '<svg viewBox="0 0 48 48"><circle cx="24" cy="24" r="18"/><path d="M20 16l12 8-12 8z"/></svg>',
 "glass": '<svg viewBox="0 0 48 48"><path d="M10 8h28L24 24zM24 24v16M16 40h16M30 4l6 6"/></svg>',
 "gem": '<svg viewBox="0 0 48 48"><path d="M6 18l8-10h20l8 10-18 22z"/><path d="M6 18h36M18 8l-4 10 10 22 10-22-4-10"/></svg>',
 "star": '<svg viewBox="0 0 48 48"><path d="M24 4l6 13 14 1.5-10.5 9.5 3 14L24 35l-12.5 7 3-14L4 18.5 18 17z"/></svg>',
 "shield": '<svg viewBox="0 0 48 48"><path d="M24 4l16 6v12c0 10-7 18-16 22C15 40 8 32 8 22V10z"/><path d="M17 24l5 5 9-10"/></svg>',
 "infinity": '<svg viewBox="0 0 48 48"><path d="M24 24c-4-5-7-8-11-8a8 8 0 0 0 0 16c4 0 7-3 11-8s7-8 11-8a8 8 0 0 1 0 16c-4 0-7-3-11-8z"/></svg>',
}

def img(name, alt):
    return f'<img src="assets/img/{name}.png" alt="{alt}" loading="lazy">'

def cta(align="", note=True):
    n = '<p class="cta-note">Via WhatsApp &nbsp;·&nbsp; Fast &amp; Easy</p>' if note else ""
    return f'''<div class="cta-block {align}">
  <a class="btn" href="{WA}" target="_blank" rel="noopener">{ICON["wa"].replace("<svg", '<svg fill="none" stroke="currentColor" stroke-width="2.4"')}<span>Book Your Shoot</span><span class="arrow">→</span></a>
  {n}
</div>'''

def icons(items, n=None):
    n = n or len(items)
    cells = "".join(f'<div class="reveal">{ICON[i]}<h4>{t}</h4><p>{d}</p></div>' for i, t, d in items)
    return f'<div class="icons" style="--n:{n}">{cells}</div>'

def kicker(num, label):
    return f'<p class="kicker"><span>{num}</span><i></i><span>{label}</span></p>'

def page(fname, title, desc, body, light=False):
    nav = "".join(f'<li><a href="{f}"{" class=active" if f == fname else ""}>{t}</a></li>' for f, t in PAGES)
    foot_nav = "".join(f'<a href="{f}">{t}</a>' for f, t in PAGES)
    html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — VL Dubai Fashion Photoshoot</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;1,400&family=Montserrat:wght@300;400;500&family=Mrs+Saint+Delafield&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css">
</head>
<body class="{"light-hero" if light else ""}">
<header class="site-header">
  <div class="wrap">
    <a class="logo" href="index.html" aria-label="VL Dubai home"><b>VL</b><small>DUBAI</small></a>
    <button class="menu-btn" aria-label="Toggle menu">MENU</button>
    <ul class="nav">{nav}</ul>
  </div>
</header>
<main>
{body}
</main>
<footer class="site-footer">
  <div class="wrap">
    <div class="foot-top">
      <div class="foot-gallery">{img("p04_bold","Bold look")}{img("p04_accessories","VL Dubai accessories")}</div>
      <div class="foot-brand"><a class="logo" href="index.html"><b>VL</b><small>DUBAI</small></a><p>A private fashion archive<br>for extraordinary moments.</p></div>
      <div class="foot-gallery">{img("p03_night_dubai","Night Dubai")}{img("p03_downtown","Downtown Dubai")}</div>
    </div>
    <nav class="foot-nav">{foot_nav}</nav>
    <div class="foot-bottom"><span>Dubai<br>Fashion<br>Photoshoot</span><i></i><span>Access the look. Not the commitment.</span><i></i><span>By appointment only</span></div>
  </div>
</footer>
<script src="assets/main.js"></script>
</body>
</html>
'''
    open(os.path.join(OUT, fname), "w").write(html)

# ---------- 01 HOME ----------
page("index.html", "Home", "A fully styled photoshoot experience in Dubai. We create your look, choose the location and turn your photoshoot into a complete fashion experience.", f'''
<section class="hero hero-home">
  <div class="hero-media">{img("p01_hero_model","Model in black gown with the Burj Khalifa")}</div>
  <div class="wrap">
    <p class="side-note" style="color:#111">Styling &nbsp;×&nbsp; Photoshoot &nbsp;×&nbsp; Experience</p>
    <p class="eyebrow">A fully styled<br>photoshoot experience</p>
    <h1 class="display">Dubai<small>Fashion<br>Photoshoot</small></h1>
    <p class="lead">You don’t need to know<br>what to wear.<br><em>That’s our job.</em></p>
    <p class="body">We create your look, choose the right location and turn your photoshoot into a complete fashion experience.</p>
    {cta("left")}
  </div>
  <div class="pillars"><div>Iconic Locations</div><div>Exclusive Outfits</div><div>Unforgettable You</div></div>
</section>
<section>
  <div class="wrap">
    {kicker("02","The Experience")}
    <div class="split" style="margin-top:40px">
      <div class="reveal"><h2 class="display sm">Not just<br>a photoshoot.</h2><p class="lead" style="margin:24px 0"><em>We create the whole image.</em></p><a class="eyebrow" href="experience.html" style="border-bottom:1px solid">Discover the experience →</a></div>
      <div class="cards" style="--n:2">
        <a class="card reveal" href="locations.html"><div class="ph">{img("p03_desert","Desert")}</div><div class="cap"><h3>Locations</h3><p>Same city. Different stories.</p></div></a>
        <a class="card reveal" href="looks.html"><div class="ph">{img("p04_elegant","Elegant look")}</div><div class="cap"><h3>Looks</h3><p>Choose your mood — we create the look.</p></div></a>
      </div>
    </div>
  </div>
</section>
''', light=True)

# ---------- 02 EXPERIENCE ----------
page("experience.html", "Experience", "Not just a photoshoot. Styling, outfits, location and photography — everything comes together around you.", f'''
<section class="hero">
  <div class="hero-media">{img("p02_hero_model","Model at sunset facing the Burj Khalifa")}</div>
  <div class="wrap">
    {kicker("02","The Experience")}
    <h1 class="display">Not just<br>a photoshoot.</h1>
    <p class="lead"><em>We create the whole image.</em></p>
    <p class="body">You come with an idea — or with no idea at all. We help you choose the mood, location and outfit from our private fashion archive. Everything comes together around you.</p>
    <div style="max-width:620px;margin-top:20px">{icons([("hanger","Styling","Personal styling by fashion experts"),("dress","Outfits","Unique pieces from our archive"),("pin","Location","Iconic spots across Dubai"),("camera","Photoshoot","Professional photos &amp; guidance")])}</div>
  </div>
</section>
<section style="padding-top:0">
  <div class="wrap">
    <div class="cards">
      <div class="card center reveal"><div class="ph">{img("p02_styling","Stylist dressing a model")}</div><div class="cap"><h3>Styling</h3><p>We style you<br>for your story.</p></div></div>
      <div class="card center reveal"><div class="ph">{img("p02_outfits","Outfits from the archive")}</div><div class="cap"><h3>Outfits</h3><p>Access our private<br>fashion archive.</p></div></div>
      <div class="card center reveal"><div class="ph">{img("p02_location","Model on Downtown terrace")}</div><div class="cap"><h3>Location</h3><p>We choose the perfect<br>backdrop for your look.</p></div></div>
      <div class="card center reveal"><div class="ph">{img("p02_photography","Photographer shooting a model")}</div><div class="cap"><h3>Photoshoot</h3><p>Professional photos<br>and full guidance.</p></div></div>
    </div>
    <div style="margin-top:70px">{cta()}</div>
  </div>
</section>
''')

# ---------- 03 LOCATIONS ----------
loc = lambda n, t, d: f'<div class="card reveal"><div class="ph">{img(n,t)}</div><div class="cap"><h3>{t}</h3><p>{d}</p></div></div>'
page("locations.html", "Locations", "Choose your Dubai — Downtown, Desert, Beach, Old Dubai and Night Dubai.", f'''
<section class="hero" style="min-height:80vh">
  <div class="hero-media">{img("p03_night_dubai","Night Dubai")}</div>
  <div class="wrap">
    <p class="side-note">Different scenes.<br>Same you.<br>Just bolder.</p>
    {kicker("03","Iconic Locations")}
    <h1 class="display">Choose<br>your Dubai</h1>
    <p class="body">From futuristic skylines to endless deserts – we help you pick the perfect location that brings your look to life.</p>
    <p class="script" style="position:static;margin:20px 0 0 30%">Same City<br>Different<br>Stories</p>
  </div>
</section>
<section style="padding-top:0">
  <div class="wrap">
    <div class="cards" style="--n:3;--ar:1/1">{loc("p03_downtown","Downtown","Modern. Iconic. Powerful.")}{loc("p03_desert","Desert","Cinematic. Bold. Unforgetable.")}{loc("p03_beach","Beach","Effortless. Sensual. Beautiful.")}</div>
    <div class="cards" style="--n:2;--ar:3/2;margin-top:24px">{loc("p03_old_dubai","Old Dubai","Artistic. Authentic. Editorial.")}{loc("p03_night_dubai","Night Dubai","Glamorous. Edgy. Rockstar.")}</div>
    <div style="margin-top:70px">{cta()}</div>
  </div>
</section>
''')

# ---------- 04 LOOKS ----------
look = lambda n, t, d: f'<div class="card center reveal"><div class="ph">{img(n,t+" look")}</div><div class="cap"><h3>{t}</h3><p>{d}</p></div></div>'
page("looks.html", "Looks", "A wardrobe for every story. Elegant, Bold, Sexy, Avant-Garde, Romantic, Rockstar.", f'''
<section class="hero">
  <div class="hero-media">{img("p02_outfits","Fashion archive")}</div>
  <div class="wrap">
    <p class="side-note">Same city.<br>Different<br>you.</p>
    {kicker("04","The Looks")}
    <p class="eyebrow">A wardrobe for<br>every story</p>
    <h1 class="display">Your<br>Look</h1>
    <p class="lead">Choose your mood —<br>we create the look.</p>
    <p class="body">From statement dresses to avant-garde pieces, we style you with looks from our private fashion archive. Each outfit is carefully selected to match your personality, location and the story you want to tell.</p>
  </div>
</section>
<section style="padding-top:0">
  <div class="wrap">
    <div class="cards" style="--n:6">{look("p04_elegant","Elegant","Timeless. Refined.<br>Unforgetable.")}{look("p04_bold","Bold","Strong. Confident.<br>Different.")}{look("p04_sexy","Sexy","All eyes on you.")}{look("p04_avant_garde","Avant-Garde","Art. Fashion.<br>No limits.")}{look("p04_romantic","Romantic","Soft. Dreamy.<br>Cinematic.")}{look("p04_rockstar","Rockstar","Rebel. Iconic.<br>Your rules.")}</div>
  </div>
</section>
<section class="band" style="padding:110px 0">
  <div class="band-bg">{img("p04_accessories","Shoes and jewellery")}</div>
  <div class="wrap" style="display:flex;justify-content:flex-end">
    <div class="reveal" style="max-width:320px"><p class="eyebrow">More than clothes.</p><p style="margin:14px 0 30px">Accessories. Shoes. Headpieces.<br>Details that complete your look.</p><i style="display:block;width:70px;height:1px;background:var(--cream)"></i><p class="eyebrow" style="margin-top:30px">It’s all in the details.</p></div>
  </div>
</section>
<section>{cta()}</section>
''')

# ---------- 05 HOW IT WORKS ----------
client = lambda n, q, c: f'<div class="card reveal"><div class="ph" style="--ar:6/7;aspect-ratio:6/7">{img(n,c)}</div><p class="quote">{q}<cite>— {c}</cite></p></div>'
step = lambda num, ic, t, d: f'<div class="reveal" style="text-align:left">{kicker(num,"")}<h4 style="margin-top:16px;min-height:40px">{t}</h4>{ICON[ic]}<p>{d}</p></div>'
page("how-it-works.html", "How It Works", "Simple process. Extraordinary results. Message us, we create your look, fitting, shoot Dubai.", f'''
<section class="hero">
  <div class="hero-media" style="--pos:left center">{img("p06_car_scene","Model stepping out of a car")}</div>
  <div class="wrap">
    <p class="side-note">From<br>idea<br>to iconic<br>photos.</p>
    {kicker("05","How It Works")}
    <p class="eyebrow">Simple process.<br>Extraordinary results.</p>
    <h1 class="display">How it<br>works</h1>
    <p class="lead">You enjoy the experience.<br>We take care of the rest.</p>
    <div class="icons" style="--n:4;max-width:700px;margin-top:20px">
      {step("01","wa","Message us","Tell us your date, vision or mood.")}
      {step("02","dress","We create your look","We suggest outfits, styling and locations based on your style.")}
      {step("03","hanger","Fitting","Try your selected looks and adjust the details.")}
      {step("04","camera","Shoot Dubai","We create your fashion story in the most iconic locations.")}
    </div>
    <p class="script">Effortless<br>Iconic<br>You</p>
  </div>
</section>
<section style="padding-top:20px">
  <div class="wrap">
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:34px"><p class="eyebrow">Real people. Unforgettable stories.</p><p class="kicker"><i></i><span style="font-family:var(--sans);font-size:11px">Client experiences</span></p></div>
    <div class="cards" style="--n:5">
      {client("p05_client_anna","“I felt like a movie character. Everything was perfect!”","Anna, Russia")}
      {client("p05_client_maria","“The styling, the location, the photos — beyond my expectations.”","Maria, UAE")}
      {client("p05_client_jessica","“Professional, creative and so easy to work with. Highly recommend!”","Jessica, UK")}
      {client("p05_client_alina","“I’ve never seen myself like this. It was more than a photoshoot.”","Alina, Kazakhstan")}
      {client("p05_client_sara","“A unique experience in Dubai. Worth every moment.”","Sara, France")}
    </div>
    <div style="margin:80px 0">{icons([("gem","Exclusive<br>Fashion Archive",""),("pin","Iconic<br>Dubai Locations",""),("star","Personal<br>Styling Experts",""),("shield","Professional<br>Photography",""),("infinity","A One-of-a-Kind<br>Experience","")])}</div>
    {cta()}
    <p class="eyebrow" style="text-align:center;margin-top:60px">Dubai looks better on you</p>
  </div>
</section>
''')

# ---------- 06 INCLUDED ----------
page("included.html", "What's Included", "Styling, designer outfits, location planning, professional shoot, beauty touch-ups and transport — plus optional add-ons.", f'''
<section class="hero">
  <div class="hero-media">{img("p06_hero_model","Model with the Burj Khalifa at sunset")}</div>
  <div class="wrap">
    {kicker("06","What’s Included")}
    <h1 class="display">What’s<br>included</h1>
    <p class="lead">You just show up — we handle everything else.</p>
    <div style="max-width:560px;margin-top:20px">{icons([("hanger","Styling","Personal styling by fashion experts"),("dress","Designer Outfits","Access to our exclusive archive"),("pin","Location Planning","We choose the best spots for your look"),("camera","Professional Shoot","Guided posing and direction"),("brush","Beauty Touch-ups","Hair &amp; makeup upon request"),("car","Transport Options","With driver upon request")], 3)}</div>
  </div>
</section>
<section class="band cream-band" style="padding:90px 0">
  <div class="band-bg" style="left:45%">{img("p06_car_scene","Chauffeured arrival")}</div>
  <div class="band-bg" style="background:linear-gradient(90deg,var(--cream) 45%,rgba(243,238,231,.85) 55%,transparent 75%)"></div>
  <div class="wrap">
    <p class="eyebrow">Optional add-ons</p>
    <h2 class="display sm" style="margin:24px 0">Make it<br>even more you</h2>
    <p class="body" style="margin-bottom:34px">From luxury transfers to video content — we can tailor the experience to your needs.</p>
    <div style="max-width:620px">{icons([("car","Private Driver","Comfort and style"),("play","Reels &amp; Video","Short-form content for your social media"),("glass","Champagne Setup","For special occasions"),("gem","Custom Look","Bespoke pieces upon request")])}</div>
  </div>
</section>
<section class="band" style="padding:140px 0">
  <div class="band-bg">{img("p06_closing_scene","Model silhouetted against the skyline")}</div>
  <div class="wrap" style="display:flex;justify-content:flex-end">
    <div class="reveal">
      {kicker("07","Ready?")}
      <h2 class="display sm" style="margin:30px 0 16px">Ready for<br>your photoshoot?</h2>
      <p style="margin-bottom:30px">Let’s create something unforgettable.</p>
      {cta("left")}
    </div>
  </div>
</section>
''')

# ---------- 07 STORIES + FAQ ----------
story = lambda n, q, c: f'<div class="card reveal"><div class="ph" style="aspect-ratio:3/5">{img(n,c)}</div><p class="quote">{q}<cite>— {c}</cite></p></div>'
faqs = [
 ("Do I need to know what to wear?", "Not at all. Our stylists select looks from our private archive based on your mood, body and location — you simply try them on."),
 ("Can I choose the location?", "Yes. Pick from Downtown, Desert, Beach, Old Dubai or Night Dubai — or tell us your idea and we will plan it."),
 ("How far in advance should I book?", "We recommend booking at least 3–5 days ahead so we can prepare your looks and fitting. Last-minute requests are possible on availability."),
 ("Is a fitting included?", "Yes. Every shoot includes a fitting to try your selected looks and adjust the details."),
 ("Do you offer hair & makeup?", "Beauty touch-ups — hair and makeup — are available upon request."),
 ("Can I get videos too?", "Yes. Reels and short-form video are available as an add-on."),
 ("Do you work with couples or groups?", "Absolutely. Message us with the number of people and we will tailor the experience."),
 ("What is the price?", "Every shoot is tailored. Message us on WhatsApp with your date and ideas and we will send you a personal quote."),
]
faq_html = "".join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in faqs)
page("stories.html", "Stories & FAQ", "Client stories and frequently asked questions about VL Dubai fashion photoshoots.", f'''
<section style="padding-top:150px">
  <div class="wrap">
    <div style="display:flex;justify-content:space-between;margin-bottom:40px">{kicker("08","Real people. Real stories.")}<p class="eyebrow" style="font-size:11px">Dubai looks better on you</p></div>
    <div style="display:grid;grid-template-columns:1fr 3fr;gap:30px" class="split">
      <div class="reveal"><h1 class="display sm">Client<br>stories</h1><p class="lead" style="margin:18px 0 40px">Different people.<br>Same feeling.</p><p class="eyebrow" style="font-size:11px;line-height:2">Travelers.<br>Creators.<br>Artists.<br>Dubai lovers.</p></div>
      <div class="cards">
        {story("p07_anna","“It felt like a movie character. Everything was perfect!”","Anna, Russia")}
        {story("p07_maria","“The styling, the location, the photos — beyond my expectations.”","Maria, UAE")}
        {story("p07_james","“Professional, creative and so easy to work with. Highly recommend!”","James, UK")}
        {story("p07_alina","“I’ve never seen myself like this. It was more than a photoshoot.”","Alina, Kazakhstan")}
      </div>
    </div>
  </div>
</section>
<section style="padding:0;border-top:1px solid var(--line)">
  <div class="split" style="gap:0;align-items:stretch">
    <div style="position:relative;min-height:520px">{img("p07_faq_photo","Model with flowing black cape").replace("<img","<img style=\"position:absolute;inset:0;object-position:center 75%\"")}</div>
    <div style="padding:60px 6%">
      <div style="display:flex;justify-content:space-between;gap:20px">{kicker("09","FAQ")}<p class="side-note">Simple<br>answers<br>so you can<br>just enjoy<br>the experience.</p></div>
      <h2 class="display sm" style="margin:10px 0 30px">Good to know</h2>
      <div class="faq">{faq_html}</div>
    </div>
  </div>
</section>
<section class="band" style="padding:160px 0 120px">
  <div class="band-bg">{img("p06_closing_scene","Dubai skyline at sunset")}</div>
  <div class="wrap">
    <p class="eyebrow" style="font-size:11px;margin-bottom:80px">More than<br>a photoshoot.</p>
    <div style="display:flex;justify-content:space-between;align-items:flex-end;flex-wrap:wrap;gap:40px">
      <div class="reveal"><h2 class="display sm">Your<br>Dubai story<br>awaits.</h2><p class="lead" style="font-size:22px;margin-top:14px">Let’s create something unforgettable.</p></div>
      {cta()}
    </div>
  </div>
</section>
''')
print("built", len(PAGES), "pages")
