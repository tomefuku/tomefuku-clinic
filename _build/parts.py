# -*- coding: utf-8 -*-
"""ページ部品(既存サイトのクラスをそのまま使ってHTMLを組み立てる)
   リンクの "@@/" はビルド時に各ページからの相対パスに置き換わります。"""
import html as _html
import re

esc = _html.escape

ICONS = {
    "lines": '<path d="M4 12h16M4 6h10M4 18h13"/>',
    "chart": '<path d="M4 17l6-6 4 4 6-8"/>',
    "box": '<rect x="4" y="5" width="16" height="14" rx="1"/><path d="M4 10h16"/>',
    "clock": '<circle cx="12" cy="12" r="8"/><path d="M12 8v4l3 2"/>',
    "moon": '<path d="M19 14.5A7.5 7.5 0 0 1 9.5 5a7.5 7.5 0 1 0 9.5 9.5z"/>',
    "drop": '<path d="M12 3s6 6.5 6 11a6 6 0 0 1-12 0c0-4.5 6-11 6-11z"/>',
    "shield": '<path d="M12 3l7 3v5c0 4.5-3 8-7 10-4-2-7-5.5-7-10V6z"/>',
    "check": '<circle cx="12" cy="12" r="8"/><path d="M8.5 12.5l2.5 2.5 4.5-5"/>',
    "wind": '<path d="M3 9h11a3 3 0 1 0-3-3M3 15h15a3 3 0 1 1-3 3"/>',
    "people": '<circle cx="9" cy="8" r="3"/><path d="M3.5 19c.8-3.2 3-5 5.5-5s4.7 1.8 5.5 5"/><circle cx="17" cy="9" r="2.3"/><path d="M15.5 14.2c2.3.2 4 1.8 4.6 4.8"/>',
    "layers": '<path d="M12 4l8 4-8 4-8-4z"/><path d="M4 12l8 4 8-4M4 16l8 4 8-4"/>',
    "pin": '<path d="M12 21s-6-6.2-6-11a6 6 0 0 1 12 0c0 4.8-6 11-6 11z"/><circle cx="12" cy="10" r="2.2"/>',
}


def icon(name):
    return ('<div class="mark"><svg viewBox="0 0 24 24" fill="none" stroke="#1f3d2e" stroke-width="1.6">'
            + ICONS[name] + '</svg></div>')


def section(kicker, h2, inner, desc=None, band=False, sid=None, h2_id=None):
    cls = "section-pad band" if band else "section-pad"
    id_attr = f' id="{sid}"' if sid else ""
    h2_attr = f' id="{h2_id}"' if h2_id else ""
    d = f'\n        <p class="desc">{desc}</p>' if desc else ""
    return f'''
  <section class="{cls}"{id_attr}>
    <div class="wrap">
      <div class="sec-head reveal">
        <span class="kicker">{kicker}</span>
        <h2{h2_attr}>{h2}</h2>{d}
      </div>
{inner}
    </div>
  </section>
'''


def prose(html_text):
    return f'      <div class="prose">\n{html_text}\n      </div>'


def strength(items):
    """items: [(icon, h3, p)]"""
    out = ['      <div class="strength-grid">']
    for ic, h, p in items:
        out.append(f'''        <div class="strength-item">
          {icon(ic)}
          <h3>{h}</h3>
          <p>{p}</p>
        </div>''')
    out.append('      </div>')
    return "\n".join(out)


def link_cards(items):
    """items: [(href, name, note)]"""
    out = ['      <div class="link-grid">']
    for href, name, note in items:
        out.append(f'''        <a class="price-card" href="{href}">
          <div class="name">{name}</div>
          <div class="note">{note}</div>
          <div class="more">詳しく見る</div>
        </a>''')
    out.append('      </div>')
    return "\n".join(out)


def tags(items, heading=None):
    h = f'<h3>{heading}</h3>' if heading else ""
    links = "".join(f'<a href="{href}">{label}</a>' for href, label in items)
    return f'        <div class="fb-col">{h}<div class="tag-list">{links}</div></div>'


def table(headers, rows, wide=False):
    cls = "sd-table wide" if wide else "sd-table"
    th = "".join(f"<th>{h}</th>" for h in headers)
    trs = "\n".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<div class="table-scroll"><table class="{cls}"><thead><tr>{th}</tr></thead><tbody>\n{trs}\n</tbody></table></div>'


def faq_details(faqs):
    out = []
    for q, a in faqs:
        out.append(f'''      <details class="sd-item">
        <summary>{q} <span class="plus">+</span></summary>
        <div class="sd-body"><div>
          <p style="font-size:13.5px;color:var(--ink-soft);">{a}</p>
        </div></div>
      </details>''')
    return "\n".join(out)


def strip_tags(s):
    return re.sub(r"<[^>]+>", "", s)


def faq_jsonld(faqs):
    return {
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": strip_tags(q),
             "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}}
            for q, a in faqs
        ],
    }


def cta_banner(h2="まずはお気軽にご相談ください。",
               p="床の状態・面積・ご希望の清掃頻度をお聞かせください。現地確認のうえ、無料でお見積もりをご案内します。",
               label="無料見積もりを依頼する", href="@@/contact/"):
    return f'''
  <section class="section-pad cta-banner">
    <div class="wrap">
      <h2>{h2}</h2>
      <p>{p}</p>
      <a class="btn" href="{href}">{label}</a>
    </div>
  </section>
'''


def ba_card(cat, data_cat, before, after, alt_b, alt_a, h3, desc="", badge="", link=None):
    """施工事例カード(ビフォーアフター横並び)"""
    b = f'<div class="wm-badge">{badge}</div>' if badge else ""
    d = f'<p class="wm-desc">{desc}</p>' if desc else ""
    l = f'<a class="wm-link" href="{link[0]}">{link[1]}</a>' if link else ""
    return f'''        <div class="work-card" data-cat="{data_cat}">
          <div class="ph work-photo">
            <div class="ba-split">
              <img src="@@/assets/img/{before}.webp" alt="{alt_b}" loading="lazy" decoding="async">
              <img src="@@/assets/img/{after}.webp" alt="{alt_a}" loading="lazy" decoding="async">
            </div>
            <span class="ba-label before">BEFORE</span><span class="ba-label after">AFTER</span>
          </div>
          <div class="work-meta">
            <div class="cat">{cat}</div>
            <h3>{h3}</h3>
            {b}{d}{l}
          </div>
        </div>'''


def stack_card(cat, data_cat, imgs, h3, desc="", badge="", link=None):
    """施工事例カード(縦に写真を並べる)  imgs: [(file, alt)]"""
    b = f'<div class="wm-badge">{badge}</div>' if badge else ""
    d = f'<p class="wm-desc">{desc}</p>' if desc else ""
    l = f'<a class="wm-link" href="{link[0]}">{link[1]}</a>' if link else ""
    ims = "\n".join(f'            <img src="@@/assets/img/{f}.webp" alt="{a}" loading="lazy" decoding="async">' for f, a in imgs)
    return f'''        <div class="work-card" data-cat="{data_cat}">
          <div class="work-photo-stack">
{ims}
          </div>
          <div class="work-meta">
            <div class="cat">{cat}</div>
            <h3>{h3}</h3>
            {b}{d}{l}
          </div>
        </div>'''


def single_card(cat, data_cat, img, alt, h3, desc="", link=None):
    d = f'<p class="wm-desc">{desc}</p>' if desc else ""
    l = f'<a class="wm-link" href="{link[0]}">{link[1]}</a>' if link else ""
    return f'''        <div class="work-card" data-cat="{data_cat}">
          <div class="ph work-photo">
            <img src="@@/assets/img/{img}.webp" alt="{alt}" loading="lazy" decoding="async" style="width:100%;height:100%;object-fit:cover;display:block;">
          </div>
          <div class="work-meta">
            <div class="cat">{cat}</div>
            <h3>{h3}</h3>
            {d}{l}
          </div>
        </div>'''


def works_grid(cards):
    return '      <div class="works-grid">\n' + "\n".join(cards) + '\n      </div>'
