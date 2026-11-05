# -*- coding: utf-8 -*-
"""
クリニック清掃サイトのビルドスクリプト
使い方:  python3 _build/build.py   (リポジトリのルートで実行)
  → 各ページの index.html / sitemap.xml / robots.txt / 404.html を生成します。
"""
import json
import os
import sys
from datetime import date

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config import SITE_URL, COMPANY, SITE_NAME  # noqa: E402
from content_areas import AREAS  # noqa: E402
from content_common import SPECIALTY_LIST  # noqa: E402

sys.modules.setdefault("build", sys.modules[__name__])

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSET_VER = "20261105"
PAGES = []  # sitemap 用

C = COMPANY


# ---------------------------------------------------------------------------
# 構造化データ(すべて実際の会社情報のみ)
# ---------------------------------------------------------------------------
def area_served():
    return [{"@type": "AdministrativeArea", "name": n} for n in
            ["東京都", "埼玉県", "神奈川県", "千葉県", "茨城県", "栃木県", "群馬県"]]


def org_node():
    return {
        "@type": "Organization",
        "@id": SITE_URL + "/#organization",
        "name": C["name"],
        "alternateName": C["name_en"],
        "url": SITE_URL + "/",
        "logo": SITE_URL + "/assets/img/logo-tomefuku-biso.webp",
        "telephone": C["tel_mobile_intl"],
        "email": C["email"],
        "founder": {"@type": "Person", "name": C["representative"]},
        "taxID": C["tax_id"],
        "sameAs": [C["instagram"], C["main_site"]],
    }


def localbusiness_node():
    return {
        "@type": "LocalBusiness",
        "@id": SITE_URL + "/#localbusiness",
        "name": C["name"],
        "alternateName": C["name_en"],
        "description": "東京都・埼玉県を中心に関東全域のクリニック・医院・歯科医院向けに、床洗浄・ワックス、床剥離洗浄、定期清掃、ガラス清掃、業務用エアコン洗浄を行う清掃会社です。",
        "url": SITE_URL + "/",
        "image": SITE_URL + "/assets/img/ogp-clinic-cleaning.jpg",
        "logo": SITE_URL + "/assets/img/logo-tomefuku-biso.webp",
        "telephone": C["tel_mobile_intl"],
        "email": C["email"],
        "address": {
            "@type": "PostalAddress",
            "postalCode": C["postal_code"],
            "addressRegion": C["region"],
            "addressLocality": C["locality"],
            "streetAddress": C["street"],
            "addressCountry": "JP",
        },
        "areaServed": area_served(),
        "priceRange": "¥3,300〜",
        "founder": {"@type": "Person", "name": C["representative"]},
        "taxID": C["tax_id"],
        "parentOrganization": {"@id": SITE_URL + "/#organization"},
        "sameAs": [C["instagram"]],
    }


def provider_ref():
    return {"@id": SITE_URL + "/#localbusiness"}


def breadcrumb_node(crumbs):
    items = []
    for i, (name, path) in enumerate(crumbs, 1):
        it = {"@type": "ListItem", "position": i, "name": name}
        if path is not None:
            it["item"] = SITE_URL + "/" + path
        items.append(it)
    return {"@type": "BreadcrumbList", "itemListElement": items}


def service_node(name, desc, path, service_type, area=None, offers=None):
    n = {
        "@type": "Service",
        "name": name,
        "serviceType": service_type,
        "description": desc,
        "url": SITE_URL + "/" + path,
        "provider": provider_ref(),
        "areaServed": area if area else [{"@type": "AdministrativeArea", "name": "東京都"},
                                          {"@type": "AdministrativeArea", "name": "埼玉県"}],
    }
    if offers:
        n["offers"] = offers
    return n


# ---------------------------------------------------------------------------
# レイアウト(tomefuku.jp と同じ部品)
# ---------------------------------------------------------------------------
def header_html(is_top):
    if is_top:
        nav = [("#service", "SERVICE"), ("#price", "PRICE"), ("#works", "WORKS"), ("#faq", "FAQ"),
               ("#message", "ABOUT"), ("#contact", "CONTACT")]
        logo = "#top"
        cta = "#contact"
    else:
        nav = [("@@/#service", "SERVICE"), ("@@/price/", "PRICE"), ("@@/#works", "WORKS"), ("@@/#faq", "FAQ"),
               ("@@/#message", "ABOUT"), ("@@/contact/", "CONTACT")]
        logo = "@@/"
        cta = "@@/contact/"
    nav_html = "\n".join(f'      <a href="{h}">{t}</a>' for h, t in nav)
    mm = [("@@/", "ホーム", ' class="mm-home"'),
          ("@@/#service" if not is_top else "#service", "サービス・料金", ""),
          ("@@/specialty/", "診療科目別", ""),
          ("@@/area/", "対応エリア", ""),
          ("@@/#works" if not is_top else "#works", "施工事例", ""),
          ("@@/column/", "コラム・よくある質問", ""),
          ("@@/#message" if not is_top else "#message", "会社案内", ""),
          (cta, "お問い合わせ", "")]
    if is_top:
        mm[0] = ("#top", "ホーム", ' class="mm-home"')
    mm_html = "\n".join(f'  <a href="{h}"{c}>{t}</a>' for h, t, c in mm)
    return f'''<header>
  <div class="wrap nav-row">
    <a href="{logo}" class="logo-mark">
      <img src="@@/assets/img/logo-turtle-green.webp" alt="留福美装" width="34" height="23" style="width:34px;height:auto;">
      <span>留福美装<br><span class="logo-sub">TOMEFUKU BISOU</span></span>
    </a>
    <nav class="main-nav" aria-label="メインメニュー">
{nav_html}
    </nav>
    <div class="header-cta">
      <a class="tel-link" href="tel:{C["tel_mobile_link"]}">{C["tel_mobile"]}</a>
      <a class="btn" href="{cta}">無料見積もり</a>
    </div>
    <button class="hamburger" id="hamburgerBtn" aria-label="メニューを開く" aria-expanded="false">
      <span></span><span></span><span></span>
    </button>
  </div>
</header>

<div class="mobile-menu" id="mobileMenu">
  <button class="mm-close" id="mobileMenuClose" aria-label="メニューを閉じる">✕</button>
{mm_html}
</div>
'''


def footer_html(is_top):
    from content_common import SERVICES
    svc = "".join(f'<li><a href="@@/{p}">{n}</a></li>' for p, n, _ in SERVICES)
    spc = "".join(f'<li><a href="@@/specialty/{s}/">{n}</a></li>' for s, n, _ in SPECIALTY_LIST)
    from content_areas import AREA_BY_SLUG
    from content_prefs import PREFS
    sai = "".join(f'<li><a href="@@/area/{s}/">{AREA_BY_SLUG[s]["name"]}</a></li>' for s in ["saitama", "kawaguchi", "toda", "warabi", "koshigaya", "kasukabe", "tokorozawa", "kawagoe"])
    sai += '<li><a href="@@/area/#saitama">埼玉県の全市町村 →</a></li>'
    tok = "".join(f'<li><a href="@@/area/{s}/">{AREA_BY_SLUG[s]["name"]}</a></li>' for s in ["shinjuku", "shibuya", "minato", "toshima", "setagaya", "adachi", "hachioji", "machida"])
    tok += '<li><a href="@@/area/#tokyo">東京都の全市区町村 →</a></li>'
    tok += "".join(f'<li><a href="@@/area/{p["slug"]}/">{p["name"]}</a></li>' for p in PREFS)
    contact = "#contact" if is_top else "@@/contact/"
    return f'''<footer>
  <div class="wrap">
    <div class="footer-links">
      <div><div class="fl-head">SERVICE</div><ul>{svc}<li><a href="@@/column/">コラム・よくあるご質問</a></li><li><a href="{contact}">お問い合わせ</a></li></ul></div>
      <div><div class="fl-head">CLINIC</div><ul><li><a href="@@/specialty/">診療科目別のご案内</a></li>{spc}</ul></div>
      <div><div class="fl-head">AREA SAITAMA</div><ul><li><a href="@@/area/">対応エリア一覧</a></li>{sai}</ul></div>
      <div><div class="fl-head">AREA TOKYO</div><ul>{tok}</ul></div>
      <div><div class="fl-head">COMPANY</div><ul><li><a href="@@/#message">代表挨拶・会社案内</a></li><li><a href="{C["main_site"]}" target="_blank" rel="noopener">留福美装 公式サイト</a></li><li><a href="{C["instagram"]}" target="_blank" rel="noopener">Instagram</a></li></ul></div>
    </div>
  </div>
  <div class="wrap footer-row">
    <div style="display:flex;align-items:center;gap:16px;">
      <img src="@@/assets/img/logo-tomefuku-biso.webp" alt="留福美装 TOMEFUKU BISOU" width="64" height="67" loading="lazy" style="width:64px;height:auto;">
      <div>
        <div style="font-weight:700;color:var(--ink);">留福美装</div>
        〒{C["postal_code"]} {C["region"]}{C["locality"]}{C["street"]}<br>
        TEL {C["tel_mobile"]} / {C["tel_fixed"]}　登録番号 {C["tax_id"]}
      </div>
    </div>
    <div class="footer-nav">
      <a href="{"#service" if is_top else "@@/#service"}">SERVICE</a>
      <a href="{"#works" if is_top else "@@/#works"}">WORKS</a>
      <a href="{"#message" if is_top else "@@/#message"}">ABOUT</a>
      <a href="{contact}">CONTACT</a>
    </div>
  </div>
</footer>

<div class="fixed-cta">
  <a class="call" href="tel:{C["tel_mobile_link"]}">電話で相談</a>
  <a class="quote" href="{contact}">無料見積もり</a>
</div>
'''


def sub_hero(eyebrow, h1, sub, img="clinic-carpet-cleaning-hero", alt="クリニックの院内カーペットを洗浄する作業風景",
             actions=None):
    if actions is None:
        actions = [("@@/contact/", "無料見積もりを依頼する", ""), ("@@/price/", "料金を見る", " outline")]
    acts = "\n".join(f'        <a class="btn{c}" href="{h}">{t}</a>' for h, t, c in actions)
    return f'''  <section class="hero hero--sub">
    <div class="ph dark hero-photo">
      <img src="@@/assets/img/{img}.webp" alt="{alt}" fetchpriority="high" decoding="async" style="width:100%;height:100%;object-fit:cover;display:block;">
    </div>
    <div class="hero-watermark" aria-hidden="true"><img src="@@/assets/img/logo-turtle-white.webp" alt=""></div>
    <div class="wrap hero-inner">
      <span class="hero-eyebrow wordmark">{eyebrow}</span>
      <h1>{h1}</h1>
      <p class="hero-sub">{sub}</p>
      <div class="hero-actions">
{acts}
      </div>
    </div>
  </section>
'''


def breadcrumb_html(crumbs):
    lis = []
    for name, path in crumbs:
        if path is None:
            lis.append(f'<li aria-current="page">{name}</li>')
        else:
            lis.append(f'<li><a href="@@/{path}">{name}</a></li>')
    return f'  <nav class="breadcrumb wrap" aria-label="パンくずリスト"><ol>{"".join(lis)}</ol></nav>\n'


def write_page(path, title, desc, body, crumbs=None, graph=None, is_top=False, og_type="website",
               changefreq="monthly", priority="0.7", og_image="assets/img/ogp-clinic-cleaning.jpg", hero=""):
    """path: "" (トップ) / "floor-wax/" / "area/kawaguchi/" など"""
    depth = path.count("/")
    prefix = "../" * depth if depth else "./"
    url = SITE_URL + "/" + path
    nodes = [localbusiness_node()]
    if is_top:
        nodes.insert(0, org_node())
        nodes.append({"@type": "WebSite", "@id": SITE_URL + "/#website", "url": SITE_URL + "/", "name": SITE_NAME,
                      "inLanguage": "ja", "publisher": {"@id": SITE_URL + "/#organization"}})
    full_crumbs = None
    if crumbs:
        full_crumbs = [("ホーム", "")] + crumbs
        nodes.append(breadcrumb_node([(n, p) for n, p in full_crumbs]))
    nodes.append({"@type": "WebPage", "@id": url + "#webpage", "url": url, "name": title, "description": desc,
                  "inLanguage": "ja", "isPartOf": {"@type": "WebSite", "url": SITE_URL + "/", "name": SITE_NAME}})
    if graph:
        nodes.extend(graph)
    ld = json.dumps({"@context": "https://schema.org", "@graph": nodes}, ensure_ascii=False, indent=1)

    intro = ""
    if is_top:
        intro = '''<div id="introScreen" class="intro-screen" style="background:#122820;">
  <div class="intro-inner">
    <div class="intro-glow"></div>
    <img src="@@/assets/img/logo-turtle-white.webp" alt="留福美装" class="intro-logo">
    <div class="intro-line"></div>
    <div class="intro-word">TOMEFUKU BISOU</div>
  </div>
</div>
'''
    bc = breadcrumb_html(full_crumbs) if full_crumbs else ""
    html = f'''<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="index,follow,max-image-preview:large">
<link rel="canonical" href="{url}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="留福美装">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE_URL}/{og_image}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="ja_JP">
<meta name="twitter:card" content="summary_large_image">
<meta name="format-detection" content="telephone=no">
<meta name="theme-color" content="#122820">
<link rel="icon" href="@@/assets/img/logo-turtle-green.webp" type="image/webp">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Zen+Kaku+Gothic+New:wght@400;500;700;900&family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600&family=Shippori+Mincho:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="@@/assets/css/style.css?v={ASSET_VER}">
<script type="application/ld+json">
{ld}
</script>
</head>
<body>

{intro}{header_html(is_top)}
<main id="top">
{hero}{bc}{body}
</main>

{footer_html(is_top)}
<script src="@@/assets/js/main.js?v={ASSET_VER}" defer></script>
</body>
</html>
'''
    html = html.replace("@@/", prefix)
    out = os.path.join(ROOT, path, "index.html") if path else os.path.join(ROOT, "index.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    PAGES.append((path, changefreq, priority))


def write_sitemap():
    today = date.today().isoformat()
    urls = "\n".join(
        f"  <url><loc>{SITE_URL}/{p}</loc><lastmod>{today}</lastmod><changefreq>{cf}</changefreq><priority>{pr}</priority></url>"
        for p, cf, pr in PAGES)
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>\n')
    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(f"User-agent: *\nAllow: /\nDisallow: /_build/\n\nSitemap: {SITE_URL}/sitemap.xml\n")


def main():
    import pages_top
    import pages_service
    import pages_specialty
    import pages_area
    import pages_column
    pages_top.build(write_page)
    pages_service.build(write_page, sub_hero)
    pages_specialty.build(write_page, sub_hero)
    pages_area.build(write_page, sub_hero)
    pages_column.build(write_page, sub_hero)
    write_sitemap()
    print(f"{len(PAGES)} pages built")


if __name__ == "__main__":
    main()
