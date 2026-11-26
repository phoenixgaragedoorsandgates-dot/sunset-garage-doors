"""Builds the static site into the repo root. Run: python3 _src/build.py"""
import json
import os
import sys
from html import escape as e

sys.path.insert(0, os.path.dirname(__file__))
from data import SITE, BIZ, BRANDS, CITIES, REVIEWS, FAQS, SERVICES, GALLERY  # noqa: E402
from posts import POSTS  # noqa: E402

ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "public")
TEL = BIZ["phone_tel"]
PHONE = BIZ["phone_display"]
BIZ_ID = SITE + "/#business"
ROMAN = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII"]

ICON = {
    "phone": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z"/></svg>',
    "text": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M4 3h16a2 2 0 0 1 2 2v11a2 2 0 0 1-2 2H8l-5 4V5a2 2 0 0 1 1-2z"/></svg>',
    "arrow": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="1.6" d="M4 12h15M13 6l6 6-6 6"/></svg>',
    "star": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="m12 2 3.1 6.3 6.9 1-5 4.9 1.2 6.8L12 17.8 5.8 21l1.2-6.8-5-4.9 6.9-1z"/></svg>',
}

NAV = [("Services", "/services/"), ("Service Areas", "/service-areas/"), ("Reviews", "/#reviews"), ("Blog", "/blog/"), ("FAQ", "/faq/"), ("Contact", "/contact/")]


# ---------- schema ----------
def business_schema():
    return {
        "@context": "https://schema.org",
        "@type": "HomeAndConstructionBusiness",
        "@id": BIZ_ID,
        "name": BIZ["name"],
        "url": SITE + "/",
        "logo": SITE + "/images/logo.png",
        "image": [SITE + "/images/og.jpg", SITE + "/images/door-double-woodgrain.jpg"],
        "telephone": "+1-626-606-9766",
        "description": f"Licensed garage door repair and installation company in Monrovia, CA (license #{BIZ['license']}). Spring replacement, opener repair and installation, off-track repair, one-piece doors, new garage doors and commercial garage doors (20, 22 and 24 gauge steel) across the San Gabriel Valley.",
        "address": {"@type": "PostalAddress", "streetAddress": BIZ["street"], "addressLocality": BIZ["city"], "addressRegion": BIZ["region"], "postalCode": BIZ["zip"], "addressCountry": "US"},
        "geo": {"@type": "GeoCoordinates", "latitude": BIZ["lat"], "longitude": BIZ["lng"]},
        "hasMap": BIZ["google"],
        "sameAs": [BIZ["google"], BIZ["instagram"], BIZ["facebook"], BIZ["yelp"]],
        "areaServed": [{"@type": "City", "name": f"{c}, CA"} for c in CITIES],
        "openingHoursSpecification": [
            {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"], "opens": "07:00", "closes": "22:00"},
            {"@type": "OpeningHoursSpecification", "dayOfWeek": "Friday", "opens": "07:00", "closes": "17:00"},
        ],
        "hasCredential": {"@type": "EducationalOccupationalCredential", "credentialCategory": "license", "name": f"California Contractor License #{BIZ['license']}"},
        "paymentAccepted": "Financing available through Acorn Finance",
        "brand": [{"@type": "Brand", "name": b} for b in BRANDS],
        "hasOfferCatalog": {
            "@type": "OfferCatalog",
            "name": "Garage door services",
            "itemListElement": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": s["name"], "url": f"{SITE}/{s['slug']}/"}} for s in SERVICES],
        },
        "priceRange": "$$",
    }


def faq_schema(faqs):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}


def crumbs_schema(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + u} for i, (n, u) in enumerate(items)]}


def ld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False) + "</script>"


# ---------- layout ----------
def page(path, title, description, body, schemas=(), og_image="og", active=""):
    url = SITE + path
    nav = "".join(f'<a href="{u}"{" aria-current=page" if active == u else ""}>{n}</a>' for n, u in NAV)
    mnav = "".join(f'<a href="{u}">{n}</a>' for n, u in NAV)
    hours = "".join(f"<div>{d}<br>{h}</div>" for d, h in BIZ["hours_text"])
    svc_links = "".join(f'<a href="/{s["slug"]}/">{e(s["name"])}</a>' for s in SERVICES)
    all_schemas = [business_schema()] + list(schemas)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(description)}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#f2f2f2">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Sunset Garage Doors">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(description)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/images/{og_image}.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" href="/favicon.png">
<link rel="apple-touch-icon" href="/images/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/styles.css">
{"".join(ld(s) for s in all_schemas)}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap header-inner">
    <a class="brand" href="/" aria-label="Sunset Garage Doors home"><img src="/images/logo-sm.png" alt="" width="72" height="45"><span>Sunset Garage Doors</span></a>
    <nav class="nav" aria-label="Main">{nav}</nav>
    <a class="header-call" href="tel:{TEL}">{ICON["phone"]}<span>{PHONE}</span></a>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="mnav" aria-label="Menu"><span></span><span></span></button>
  </div>
  <nav class="mnav" id="mnav" aria-label="Mobile">{mnav}<a class="btn btn-accent" href="tel:{TEL}">Call {PHONE}</a>{social_links("mnav-social")}</nav>
</header>
<main id="main">
{body}
</main>
<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div class="footer-col">
        <strong>Sunset Garage Doors</strong>
        <div>{e(BIZ["street"])}<br>{BIZ["city"]}, {BIZ["region"]} {BIZ["zip"]}</div>
        <div><a href="tel:{TEL}">{PHONE}</a></div>
        <div>CA License #{BIZ["license"]}</div>
        {social_links()}
      </div>
      <div class="footer-col"><strong>Hours</strong>{hours}</div>
      <div class="footer-col footer-links"><strong>Services</strong>{svc_links}</div>
      <div class="footer-col footer-links"><strong>Company</strong>{mnav}</div>
    </div>
    <div class="footer-base"><span>© <span class="yr">2026</span> Sunset Garage Doors. All rights reserved.</span><span>Garage door repair &amp; installation · Monrovia, CA</span></div>
  </div>
</footer>
<div class="mobile-bar">
  <a class="btn btn-accent" href="tel:{TEL}">{ICON["phone"]}Call Now</a>
  <a class="btn btn-ghost" href="sms:{TEL}">{ICON["text"]}Text Us</a>
</div>
<script src="/site.js" defer></script>
</body>
</html>
"""


SOCIAL_ICONS = {
    "instagram": '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5" fill="none" stroke="currentColor" stroke-width="1.7"/><circle cx="12" cy="12" r="4.2" fill="none" stroke="currentColor" stroke-width="1.7"/><circle cx="17.4" cy="6.6" r="1.1" fill="currentColor"/></svg>',
    "facebook": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M13.5 21v-7.5h2.6l.4-3h-3V8.6c0-.9.3-1.5 1.6-1.5h1.6V4.4c-.3 0-1.2-.1-2.3-.1-2.3 0-3.9 1.4-3.9 4v2.2H8v3h2.5V21z"/></svg>',
    "yelp": '<svg viewBox="0 0 24 24" aria-hidden="true"><g fill="currentColor"><path d="M10.6 2.3c-.9-.2-3.3.5-3.9 1.1-.3.3-.3.7-.1 1l4.1 7.1c.4.7 1.5.4 1.5-.4V3.3c0-.5-.3-.8-.7-.9z"/><path d="M5.5 13.9l3.7-1.1c.8-.2.8-1.3 0-1.6L5.6 9.8c-.4-.2-.9 0-1 .5-.3 1-.3 2.3 0 3.1.1.4.5.6.9.5z"/><path d="M6.9 19.3c.7.7 1.9 1.4 2.8 1.6.4.1.8-.2.8-.6l.2-3.9c0-.8-1-1.2-1.5-.6l-2.4 2.8c-.2.3-.2.5.1.7z"/><path d="M13.6 15.8l2 3.3c.2.4.7.5 1 .2.9-.6 1.7-1.6 2-2.6.1-.4-.1-.8-.5-.9l-3.6-1.2c-.8-.3-1.4.6-.9 1.2z"/><path d="M14.3 12.9l3.7-1c.4-.1.6-.5.5-.9-.3-1-1-2.1-1.8-2.7-.3-.3-.8-.2-1 .1l-2.2 3.2c-.4.7.2 1.5.8 1.3z"/></g></svg>',
    "google": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" d="M19.5 12.2h-7.2M19.5 12.2a7.5 7.5 0 1 1-2.2-5.4"/></svg>',
}
SOCIAL_LABELS = {"instagram": "Instagram", "facebook": "Facebook", "yelp": "Yelp", "google": "Google reviews"}


def social_links(extra_class=""):
    items = "".join(
        f'<a class="social-link" href="{BIZ[k]}" target="_blank" rel="noopener" aria-label="Sunset Garage Doors on {SOCIAL_LABELS[k]}" title="{SOCIAL_LABELS[k]}">{SOCIAL_ICONS[k]}</a>'
        for k in ("instagram", "facebook", "yelp", "google"))
    return f'<div class="social {extra_class}">{items}</div>'


def label(n, text):
    return f'<div class="label"><span>{n}</span>{e(text)}</div>'


def cta_block(heading="Need your garage door fixed?", text="Call or text a photo of the problem. We'll tell you what's likely wrong and get you on the schedule."):
    return f"""
<section class="section cta-band">
  <div class="wrap two-col">
    <h2 class="h-lg">{e(heading)}</h2>
    <div>
      <p class="lead">{e(text)}</p>
      <div class="btn-row">
        <a class="btn btn-accent" href="tel:{TEL}">{ICON["phone"]}Call {PHONE}</a>
        <a class="btn btn-dark" href="sms:{TEL}">{ICON["text"]}Text Us</a>
      </div>
    </div>
  </div>
</section>"""


def faq_list(faqs, dark=True, n="", heading="Frequently Asked Questions"):
    items = "".join(f'<details><summary>{e(q)}<span class="plus" aria-hidden="true"></span></summary><p>{e(a)}</p></details>' for q, a in faqs)
    cls = "section section-dark" if dark else "section"
    lab = label(n, "FAQ") if n else ""
    return f"""
<section class="{cls}" id="faq">
  <div class="wrap">
    {lab}
    <div class="two-col">
      <h2 class="h-lg">{e(heading)}</h2>
      <div class="faq">{items}</div>
    </div>
  </div>
</section>"""


def reviews_block(n):
    cards = "".join(f"""
      <figure class="review">
        <div class="review-stars" aria-label="5 out of 5 stars">{ICON["star"] * 5}</div>
        <blockquote>“{e(t)}”</blockquote>
        <figcaption><strong>{e(name)}</strong><span>{e(job)} · Google</span></figcaption>
      </figure>""" for name, job, t in REVIEWS)
    return f"""
<section class="section" id="reviews">
  <div class="wrap">
    {label(n, "Reviews")}
    <div class="reviews-head">
      <h2 class="h-lg">What our customers say</h2>
      <div class="carousel-controls">
        <button class="carousel-btn" type="button" data-dir="-1" aria-label="Previous reviews"><svg viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-width="1.6" d="M20 12H5M11 6l-6 6 6 6"/></svg></button>
        <button class="carousel-btn" type="button" data-dir="1" aria-label="Next reviews">{ICON["arrow"]}</button>
      </div>
    </div>
    <div class="carousel" tabindex="0" aria-label="Customer reviews">{cards}
    </div>
    <a class="link-arrow" href="{BIZ["google"]}" target="_blank" rel="noopener">See all reviews on Google {ICON["arrow"]}</a>
  </div>
</section>"""


def service_rows(services):
    return '<ol class="rows">' + "".join(
        f'<li><a href="/{s["slug"]}/"><span class="row-num">{i + 1:02d}</span><span class="row-title">{e(s["name"])}</span><span class="row-desc">{e(s["summary"])}</span><span class="row-arrow">{ICON["arrow"]}</span></a></li>'
        for i, s in enumerate(services)) + "</ol>"


BRAND_LOGOS = [
    ("liftmaster", "LiftMaster"), ("chamberlain", "Chamberlain"), ("elegant", "Elegant Custom Garage Doors & Gates"),
    ("instock", "Instock Garage Doors"), ("chi", "CHI Overhead Doors"),
]


def brand_marquee():
    def tiles(hidden):
        out = []
        for img, name in BRAND_LOGOS:
            inner = f'<img src="/images/brands/{img}.png" alt="{"" if hidden else e(name)}" decoding="async">' if img else f'<span class="brand-word">{e(name)}</span>'
            out.append(f'<li class="brand-tile">{inner}</li>')
        return "".join(out)
    return (f'<div class="marquee-wrap"><div class="marquee" aria-label="Brands we install">'
            f'<ul class="marquee-track" aria-hidden="true">{tiles(True)}</ul>'
            f'<ul class="marquee-track">{tiles(False)}</ul>'
            f'<ul class="marquee-track" aria-hidden="true">{tiles(True)}</ul></div></div>')


def city_list():
    return '<ul class="cities">' + "".join(f"<li>{e(c)}</li>" for c in CITIES) + "</ul>"


def write(path, html):
    out = os.path.join(ROOT, path.strip("/"), "index.html") if path != "/404" else os.path.join(ROOT, "404.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w") as f:
        f.write(html)


# ---------- pages ----------
def home():
    from PIL import Image as _Im
    def _ratio(img):
        with _Im.open(os.path.join(ROOT, "images", img + ".jpg")) as im:
            return im.width / im.height, im.width, im.height
    gallery = ""
    for k in range(0, len(GALLERY), 3):
        row = ""
        for img, alt, cap in GALLERY[k:k + 3]:
            r, w, h = _ratio(img)
            row += f'<figure style="flex: {r:.3f} 1 0"><figcaption>{e(cap)}</figcaption><img src="/images/{img}.jpg" alt="{e(alt)}" loading="lazy" width="{w}" height="{h}"></figure>'
        gallery += f'<div class="gallery-row">{row}</div>'

    hours = "".join(f"<li><span>{d}</span><span>{h}</span></li>" for d, h in BIZ["hours_text"])
    body = f"""
<section class="hero">
  <div class="wrap">
    <p class="kicker">Garage door repair &amp; installation · Monrovia, California</p>
    <h1 class="h-xl">Garage door repair in Monrovia, done right the first time.</h1>
    <div class="hero-sub">
      <p class="lead">Broken springs, off-track doors, openers and new garage doors for homes and businesses across the San Gabriel Valley. Licensed, local, and backed by a written warranty on every job.</p>
      <div class="btn-row">
        <a class="btn btn-accent" href="tel:{TEL}">{ICON["phone"]}Call {PHONE}</a>
        <a class="btn btn-dark" href="sms:{TEL}">{ICON["text"]}Text Us</a>
      </div>
    </div>
  </div>
  <div class="hero-media"><img src="/images/hero-home.jpg" srcset="/images/hero-home-1200.jpg 1200w, /images/hero-home.jpg 2400w" sizes="100vw" alt="Modern home with black full-view glass garage doors at sunset" width="2400" height="1152" fetchpriority="high"></div>
  <div class="wrap facts">
    <div><span class="fact-k">Licensed &amp; insured</span><span class="fact-v">#{BIZ["license"]}</span></div>
    <div><span class="fact-k">In business</span><span class="fact-v">{BIZ["years"]} years</span></div>
    <div><span class="fact-k">Repair warranty</span><span class="fact-v">1 year</span></div>
    <div><span class="fact-k">Install warranty</span><span class="fact-v">3 years</span></div>
  </div>
</section>

<section class="section" id="services">
  <div class="wrap">
    {label("I", "Services")}
    <div class="two-col head-row"><h2 class="h-lg">Every garage door service, one call away.</h2><a class="link-arrow" href="/services/">All services {ICON["arrow"]}</a></div>
    {service_rows(SERVICES)}
  </div>
</section>

<section class="section">
  <div class="wrap">
    {label("II", "About")}
    <div class="two-col">
      <div class="about-media">
        <h2 class="h-md">Local to Monrovia</h2>
        <img src="/images/white-garage-door-home.jpg" alt="White raised-panel garage door on a gray stucco home with lantern lights" loading="lazy" width="1500" height="1000">
      </div>
      <div class="prose-lg">
        <p>Sunset Garage Doors has fixed and installed garage doors across the San Gabriel Valley for {BIZ["years"]} years, from our shop on Foothill Blvd in Monrovia.</p>
        <p>We explain exactly what's wrong, fix it properly, and put our warranty in writing: one year on every repair, three years on every installation.</p>
        <p>When something goes wrong later, you're calling a local, licensed contractor you can reach, not a call center.</p>
      </div>
    </div>
  </div>
</section>

<section class="section" id="work">
  <div class="wrap">
    {label("III", "Recent Work")}
    <div class="gallery-rows">{gallery}</div>
  </div>
</section>

{reviews_block("IV")}

<section class="feature-band" aria-label="Modern full-view glass garage door">
  <img src="/images/modern-home-glass-door.jpg" srcset="/images/modern-home-glass-door-1200.jpg 1200w, /images/modern-home-glass-door.jpg 2400w" sizes="100vw" alt="Modern home at dusk with a lit full-view glass garage door" loading="lazy" width="2400" height="1599">
</section>


<section class="section">
  <div class="wrap">
    {label("V", "Brands & Financing")}
    <div class="two-col head-row"><h2 class="h-md">Brands we install</h2><p class="body-note brands-note">Garage door openers from LiftMaster and Chamberlain, and doors from Elegant, Instock and CHI Overhead Doors. We also repair most other brands.</p></div>
  </div>
  {brand_marquee()}
  <div class="wrap">
    <div class="two-col finance-row">
      <div></div>
      <div class="finance-note">
        <h3>Financing available</h3>
        <p>Pay over time for a new door or opener with Acorn Finance. Call us to get started.</p>
        <a class="link-arrow" href="tel:{TEL}">Ask about financing {ICON["arrow"]}</a>
      </div>
    </div>
  </div>
</section>

<section class="section" id="areas">
  <div class="wrap">
    {label("VI", "Service Area")}
    <div class="two-col head-row"><h2 class="h-md">Monrovia and about 20 miles around</h2><a class="link-arrow" href="/service-areas/">Service areas {ICON["arrow"]}</a></div>
    {city_list()}
  </div>
</section>

{faq_list(FAQS, dark=True, n="VII")}

<section class="section" id="contact">
  <div class="wrap">
    {label("VIII", "Contact")}
    <div class="two-col">
      <h2 class="h-lg">Call or text<br><a class="phone-big" href="tel:{TEL}">{PHONE}</a></h2>
      <div class="contact-cols">
        <div><h3>Address</h3><p>{e(BIZ["street"])}<br>{BIZ["city"]}, {BIZ["region"]} {BIZ["zip"]}</p><a class="link-arrow" href="{BIZ["google"]}" target="_blank" rel="noopener">Directions {ICON["arrow"]}</a></div>
        <div><h3>Hours</h3><ul class="hours">{hours}</ul></div>
      </div>
    </div>
  </div>
</section>
"""
    faqs = faq_schema(FAQS)
    return page("/", "Garage Door Repair & Installation in Monrovia, CA | Sunset Garage Doors",
                f"Licensed garage door repair, spring replacement, opener repair and new garage door installation in Monrovia and the San Gabriel Valley. 1-year repair and 3-year install warranty. Call {PHONE}.",
                body, schemas=[faqs])


def services_index():
    body = f"""
<section class="page-head">
  <div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> / Services</nav>
    <h1 class="h-xl">Garage door services</h1>
    <p class="lead">Repairs, springs, openers and new garage doors for homes in Monrovia and across the San Gabriel Valley. 1-year warranty on repairs, 3-year warranty on installations.</p>
  </div>
</section>
<section class="section"><div class="wrap">{service_rows(SERVICES)}</div></section>
{cta_block()}"""
    return page("/services/", "Garage Door Services in Monrovia, CA | Sunset Garage Doors",
                "Garage door repair, spring replacement, off-track repair, opener repair and installation, new doors, one-piece doors and more in Monrovia, CA.",
                body, schemas=[crumbs_schema([("Home", "/"), ("Services", "/services/")])], active="/services/")


def service_page(s):
    others = [o for o in SERVICES if o["slug"] != s["slug"]][:5]
    intro = "".join(f"<p>{e(p)}</p>" for p in s["intro"])
    signs = "".join(f"<li>{e(x)}</li>" for x in s["signs"])
    posts = [p for p in POSTS if p.get("related") == s["slug"]]
    post_html = ""
    if posts:
        post_html = '<div class="related-posts"><h3>From the blog</h3>' + "".join(f'<a class="link-arrow" href="/blog/{p["slug"]}/">{e(p["title"])} {ICON["arrow"]}</a>' for p in posts) + "</div>"
    gallery_html = ""
    extra = [g for g in s.get("gallery", []) if g[0] != s["image"]]
    if extra:
        figs = "".join(f'<figure><figcaption>{e(cap)}</figcaption><img src="/images/{img}.jpg" alt="{e(alt)}" loading="lazy"></figure>' for img, alt, cap in extra)
        gallery_html = f'''<section class="section"><div class="wrap">{label("", s.get("gallery_title") or "Our " + s["name"].lower() + " work")}<div class="gallery gallery-{3 if len(extra) in (5, 6) else min(len(extra), 4)}">{figs}</div></div></section>
'''
    body = f"""
<section class="page-head">
  <div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> / <a href="/services/">Services</a> / {e(s["name"])}</nav>
    <h1 class="h-xl">{e(s["title"])}</h1>
    <div class="btn-row">
      <a class="btn btn-accent" href="tel:{TEL}">{ICON["phone"]}Call {PHONE}</a>
      <a class="btn btn-dark" href="sms:{TEL}">{ICON["text"]}Text Us</a>
    </div>
  </div>
</section>
<section class="section section-tight">
  <div class="wrap two-col">
    <figure class="side-img"><img src="/images/{s["image"]}.jpg" alt="{e(s["name"])} by Sunset Garage Doors in Monrovia, CA" loading="lazy"></figure>
    <div class="prose-lg">{intro}</div>
  </div>
</section>
{gallery_html}<section class="section">
  <div class="wrap">
    {label("I", "Signs you need this")}
    <div class="two-col">
      <h2 class="h-md">When to call us</h2>
      <div><ul class="checks">{signs}</ul><p class="body-note">{e(s["what"])}</p>{post_html}</div>
    </div>
  </div>
</section>
<section class="section">
  <div class="wrap">
    {label("II", "Why Sunset")}
    <div class="facts facts-inline">
      <div><span class="fact-k">Licensed &amp; insured</span><span class="fact-v">#{BIZ["license"]}</span></div>
      <div><span class="fact-k">In business</span><span class="fact-v">{BIZ["years"]} years</span></div>
      <div><span class="fact-k">Repair warranty</span><span class="fact-v">1 year</span></div>
      <div><span class="fact-k">Install warranty</span><span class="fact-v">3 years</span></div>
    </div>
  </div>
</section>
{faq_list(s["faqs"], dark=True, heading=s["name"] + " FAQ")}
<section class="section">
  <div class="wrap">
    {label("III", "Service area")}
    <div class="two-col"><h2 class="h-md">{e(s["name"])} near you</h2><div><p class="lead">We provide {e(s["name"].lower())} in Monrovia and about 20 miles around, including:</p>{city_list()}</div></div>
  </div>
</section>
<section class="section">
  <div class="wrap">
    {label("IV", "Other services")}
    {service_rows(others)}
  </div>
</section>
{cta_block()}"""
    svc = {
        "@context": "https://schema.org", "@type": "Service", "name": s["title"].replace(" in Monrovia, CA", ""),
        "serviceType": s["name"], "url": f"{SITE}/{s['slug']}/", "description": s["intro"][0],
        "provider": {"@id": BIZ_ID}, "areaServed": [{"@type": "City", "name": f"{c}, CA"} for c in CITIES],
    }
    return page(f"/{s['slug']}/", f"{s['title']} | Sunset Garage Doors",
                f"{s['summary']} Licensed (#{BIZ['license']}), 1-year repair and 3-year install warranty. Serving Monrovia & the San Gabriel Valley. Call {PHONE}.",
                body, schemas=[svc, faq_schema(s["faqs"]), crumbs_schema([("Home", "/"), ("Services", "/services/"), (s["name"], f"/{s['slug']}/")])],
                og_image=s["image"], active="/services/")


def areas_page():
    body = f"""
<section class="page-head">
  <div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> / Service Areas</nav>
    <h1 class="h-xl">Garage door service in the San Gabriel Valley</h1>
    <p class="lead">Sunset Garage Doors is based at {e(BIZ["street"])} in Monrovia. We serve homes within about 20 miles of our shop.</p>
  </div>
</section>
<section class="section section-tight">
  <div class="wrap">
    {label("I", "Cities we serve")}
    {city_list()}
    <p class="body-note">Don't see your city? Call {PHONE}. If you're close by, we'll come to you.</p>
  </div>
</section>
<section class="section">
  <div class="wrap">
    {label("II", "Services in every city")}
    {service_rows(SERVICES)}
  </div>
</section>
<section class="map-wrap"><iframe title="Map of Sunset Garage Doors in Monrovia, CA" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://maps.google.com/maps?q=Sunset%20Garage%20Doors%2C%20507%20W%20Foothill%20Blvd%20Unit%20B%2C%20Monrovia%2C%20CA%2091016&z=11&output=embed"></iframe></section>
{cta_block()}"""
    return page("/service-areas/", "Service Areas: Monrovia, Arcadia, Pasadena & More | Sunset Garage Doors",
                "Garage door repair and installation in Monrovia, Arcadia, Duarte, Sierra Madre, Pasadena, Azusa, Glendora, Temple City, El Monte and across the San Gabriel Valley.",
                body, schemas=[crumbs_schema([("Home", "/"), ("Service Areas", "/service-areas/")])], active="/service-areas/")


def faq_page():
    allfaq = FAQS + [q for s in SERVICES for q in s["faqs"]]
    body = f"""
<section class="page-head">
  <div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> / FAQ</nav>
    <h1 class="h-xl">Garage door questions, answered</h1>
  </div>
</section>
{faq_list(FAQS, dark=True, heading="About Sunset Garage Doors")}
{faq_list([q for s in SERVICES for q in s["faqs"]], dark=False, heading="Garage door repair questions")}
{cta_block("Still have a question?", "Call or text us. We're happy to help, even if it's just advice.")}"""
    return page("/faq/", "Garage Door FAQ | Sunset Garage Doors, Monrovia CA",
                "Answers about garage door springs, openers, off-track doors, warranties, financing, hours and service areas from Sunset Garage Doors in Monrovia, CA.",
                body, schemas=[faq_schema(allfaq), crumbs_schema([("Home", "/"), ("FAQ", "/faq/")])], active="/faq/")


def contact_page():
    hours = "".join(f"<li><span>{d}</span><span>{h}</span></li>" for d, h in BIZ["hours_text"])
    body = f"""
<section class="page-head">
  <div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> / Contact</nav>
    <h1 class="h-xl">Contact Sunset Garage Doors</h1>
  </div>
</section>
<section class="section section-tight">
  <div class="wrap two-col">
    <div>
      <p class="kicker">Call or text</p>
      <a class="phone-big" href="tel:{TEL}">{PHONE}</a>
      <p class="lead">Texting a photo or short video of the problem helps us tell you what's likely wrong and bring the right parts.</p>
      <div class="btn-row"><a class="btn btn-accent" href="tel:{TEL}">{ICON["phone"]}Call Now</a><a class="btn btn-dark" href="sms:{TEL}">{ICON["text"]}Text Us</a></div>
    </div>
    <div class="contact-cols">
      <div><h3>Address</h3><p>{e(BIZ["street"])}<br>{BIZ["city"]}, {BIZ["region"]} {BIZ["zip"]}</p></div>
      <div><h3>Hours</h3><ul class="hours">{hours}</ul></div>
      <div><h3>License</h3><p>California Contractor #{BIZ["license"]}</p></div>
      <div><h3>Follow &amp; review us</h3>{social_links()}</div>
    </div>
  </div>
</section>
<section class="map-wrap"><iframe title="Map to Sunset Garage Doors, 507 W Foothill Blvd, Monrovia" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://maps.google.com/maps?q=Sunset%20Garage%20Doors%2C%20507%20W%20Foothill%20Blvd%20Unit%20B%2C%20Monrovia%2C%20CA%2091016&z=14&output=embed"></iframe></section>"""
    return page("/contact/", "Contact | Sunset Garage Doors, Monrovia CA",
                f"Call or text Sunset Garage Doors at {PHONE}. 507 W Foothill Blvd, Unit B, Monrovia, CA 91016. Open Sunday–Thursday 7am–10pm, Friday 7am–5pm.",
                body, schemas=[crumbs_schema([("Home", "/"), ("Contact", "/contact/")])], active="/contact/")


def fmt_date(d):
    import datetime
    return datetime.date.fromisoformat(d).strftime("%B %-d, %Y")


def blog_index():
    items = "".join(f"""
<a class="post-card" href="/blog/{p["slug"]}/">
  <img src="/images/{p["image"]}.jpg" alt="" loading="lazy">
  <span class="post-date">{fmt_date(p["date"])}</span>
  <span class="post-title">{e(p["title"])}</span>
  <span class="post-desc">{e(p["description"])}</span>
</a>""" for p in POSTS)
    body = f"""
<section class="page-head">
  <div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> / Blog</nav>
    <h1 class="h-xl">Garage door guides</h1>
    <p class="lead">Practical advice from the Sunset Garage Doors team.</p>
  </div>
</section>
<section class="section section-tight"><div class="wrap post-grid">{items}</div></section>"""
    return page("/blog/", "Garage Door Tips & Guides | Sunset Garage Doors Blog",
                "Garage door repair tips, spring and opener guides, and advice for homeowners in Monrovia and the San Gabriel Valley.",
                body, schemas=[crumbs_schema([("Home", "/"), ("Blog", "/blog/")])], active="/blog/")


def post_page(p):
    rel = next((s for s in SERVICES if s["slug"] == p.get("related")), None)
    rel_html = f'<a class="link-arrow" href="/{rel["slug"]}/">Our {e(rel["name"].lower())} service {ICON["arrow"]}</a>' if rel else ""
    body = f"""
<article>
<section class="page-head">
  <div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> / <a href="/blog/">Blog</a></nav>
    <p class="kicker">{fmt_date(p["date"])} · Sunset Garage Doors</p>
    <h1 class="h-xl">{e(p["title"])}</h1>
  </div>
</section>
<section class="section section-tight">
  <div class="wrap two-col">
    <aside class="post-aside">
      <img src="/images/{p["image"]}.jpg" alt="" loading="lazy">
      {rel_html}
    </aside>
    <div class="article">{p["body"]}</div>
  </div>
</section>
</article>
{cta_block()}"""
    art = {
        "@context": "https://schema.org", "@type": "BlogPosting", "headline": p["title"], "description": p["description"],
        "datePublished": p["date"], "dateModified": p["date"], "image": f"{SITE}/images/{p['image']}.jpg",
        "mainEntityOfPage": f"{SITE}/blog/{p['slug']}/", "author": {"@id": BIZ_ID}, "publisher": {"@id": BIZ_ID},
    }
    return page(f"/blog/{p['slug']}/", f"{p['title']} | Sunset Garage Doors", p["description"], body,
                schemas=[art, crumbs_schema([("Home", "/"), ("Blog", "/blog/"), (p["title"], f"/blog/{p['slug']}/")])],
                og_image=p["image"], active="/blog/")


def not_found():
    body = f"""
<section class="page-head">
  <div class="wrap">
    <h1 class="h-xl">Page not found</h1>
    <p class="lead">That page doesn't exist. Try the <a href="/">home page</a> or call us at <a href="tel:{TEL}">{PHONE}</a>.</p>
  </div>
</section>
<section class="section"><div class="wrap">{service_rows(SERVICES)}</div></section>"""
    return page("/404", "Page Not Found | Sunset Garage Doors", "Page not found.", body)


def llms_txt():
    hours = "; ".join(f"{d}: {h}" for d, h in BIZ["hours_text"])
    lines = [
        "# Sunset Garage Doors",
        "",
        f"> Licensed garage door repair and installation company in Monrovia, California (CA contractor license #{BIZ['license']}), in business {BIZ['years']} years, serving homes within about 20 miles across the San Gabriel Valley.",
        "",
        f"- Phone (call or text): {PHONE}",
        f"- Address: {BIZ['street']}, {BIZ['city']}, {BIZ['region']} {BIZ['zip']}",
        f"- Hours: {hours}",
        "- Warranty: 1 year on all repairs, 3 years on all installations",
        "- Financing: available through Acorn Finance",
        f"- Brands installed: {', '.join(BRANDS)}",
        f"- Cities served: {', '.join(CITIES)}",
        f"- Google reviews: {BIZ['google']}",
        f"- Instagram: {BIZ['instagram']}",
        f"- Facebook: {BIZ['facebook']}",
        f"- Yelp: {BIZ['yelp']}",
        "",
        "## Services",
        "",
    ] + [f"- [{s['name']}]({SITE}/{s['slug']}/): {s['summary']}" for s in SERVICES] + [
        "",
        "## Guides",
        "",
    ] + [f"- [{p['title']}]({SITE}/blog/{p['slug']}/): {p['description']}" for p in POSTS] + [
        "",
        "## Other pages",
        "",
        f"- [Service areas]({SITE}/service-areas/)",
        f"- [FAQ]({SITE}/faq/)",
        f"- [Contact]({SITE}/contact/)",
        "",
    ]
    return "\n".join(lines)


def main():
    urls = ["/"]
    write("/", home())
    write("/services/", services_index()); urls.append("/services/")
    for s in SERVICES:
        write(f"/{s['slug']}/", service_page(s)); urls.append(f"/{s['slug']}/")
    write("/service-areas/", areas_page()); urls.append("/service-areas/")
    write("/faq/", faq_page()); urls.append("/faq/")
    write("/contact/", contact_page()); urls.append("/contact/")
    write("/blog/", blog_index()); urls.append("/blog/")
    for p in POSTS:
        write(f"/blog/{p['slug']}/", post_page(p)); urls.append(f"/blog/{p['slug']}/")
    write("/404", not_found())
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(
        f"  <url><loc>{SITE}{u}</loc></url>\n" for u in urls) + "</urlset>\n"
    open(os.path.join(ROOT, "sitemap.xml"), "w").write(sm)
    open(os.path.join(ROOT, "llms.txt"), "w").write(llms_txt())
    open(os.path.join(ROOT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
    print(f"built {len(urls)} pages")


if __name__ == "__main__":
    main()
