# -*- coding: utf-8 -*-
"""診療科目別ページ(/specialty/)"""
from content_specialty import SPECIALTIES
from content_areas import AREAS, AREA_BY_SLUG
from content_common import WORKS
from parts import section, prose, strength, link_cards, faq_details, faq_jsonld, cta_banner, works_grid

# 診療科目ページで紹介する重点エリア(地域×診療科目の検索に対応する内部リンク)
FOCUS = ["kawaguchi", "warabi", "toda", "saitama", "koshigaya", "soka", "adachi", "kita", "itabashi", "toshima",
         "shinjuku", "shibuya", "minato", "bunkyo", "nerima"]

SPEC_WORKS = {
    "beauty-clinic": ["beauty_floor", "beauty_carpet", "azabu_drain", "azabu_work", "beauty_aircon"],
    "ophthalmology": ["office_drain", "office_hex"],
    "dental": ["kawaguchi_floor", "beauty_floor"],
}


def build(write_page, sub_hero):
    from build import service_node

    # ---- 一覧ページ
    cards = [(f"@@/specialty/{s['slug']}/", s["h1"], s["lead"][:58] + "…") for s in SPECIALTIES]
    body = section("CLINIC", "診療科目から探す。", link_cards(cards),
                   desc="同じクリニックでも、診療科目によって院内のつくりや床の汚れ方、作業のときに気をつけることは大きく変わります。科目ごとの清掃のポイントと、おすすめの清掃メニューをまとめました。")
    body += section("COMMON", "どの診療科目でも共通して大切にしていること。", strength([
        ("moon", "診療を止めない", "休診日・診療終了後・夜間に作業し、乾燥時間まで含めて翌日の診療に影響を出しません。"),
        ("shield", "医療機器は動かさない", "機器のまわりは養生し、手作業で仕上げます。"),
        ("lines", "院内ルールの尊重", "立ち入りできる部屋や清掃の順番など、医院様のルールに沿って作業します。"),
        ("check", "料金と範囲を事前に明確に", "作業前に金額と範囲をお伝えし、追加料金が発生する場合は必ず事前にご説明します。"),
    ]), band=True)
    body += cta_banner()
    write_page("specialty/",
               "診療科目別のクリニック清掃｜歯科・眼科・内科・皮膚科など｜東京・埼玉 留福美装",
               "歯科医院・眼科・内科・皮膚科・整形外科・美容クリニック・小児科・耳鼻咽喉科・婦人科・心療内科の床清掃・定期清掃。診療科目ごとの汚れ方と作業上の配慮をご紹介します。東京都・埼玉県対応。",
               body, crumbs=[("診療科目別のご案内", None)],
               hero=sub_hero("BY SPECIALTY", "診療科目別の<br>クリニック清掃",
                             "歯科医院・眼科・内科・皮膚科・整形外科・美容クリニック・小児科・耳鼻咽喉科・婦人科・心療内科。科目ごとの床の汚れ方と、清掃で気をつけることをご紹介します。"),
               priority="0.8")

    # ---- 各診療科目
    for s in SPECIALTIES:
        path = f"specialty/{s['slug']}/"
        intro = "\n".join(f"        <p>{p}</p>" for p in s["intro"])
        body = section("ABOUT", f"{s['short']}の清掃で大切なこと。", prose(intro))
        body += section("POINT", f"{s['short']}の清掃で配慮していること。", strength(s["points"]), band=True)
        body += section("MENU", f"{s['short']}におすすめの清掃メニュー。",
                        link_cards([(f"@@/{p}", n, d) for p, n, d in s["menus"]]))
        body += section("FREQUENCY", "清掃の頻度の目安。", prose(
            f"        <p>{s['freq']}</p>\n        <p>頻度の考え方は<a href=\"@@/column/floor-cleaning-frequency/\">クリニックの床清掃はどのくらいの頻度が必要？</a>、費用については<a href=\"@@/price/\">料金ページ</a>もあわせてご覧ください。</p>"),
            band=True)
        if s["slug"] in SPEC_WORKS:
            body += section("WORKS", "関連する施工事例。", works_grid([WORKS[k] for k in SPEC_WORKS[s["slug"]]]))
        # 地域 × 診療科目
        area_links = "".join(f'<a href="@@/area/{a}/">{AREA_BY_SLUG[a]["short"]}の{s["short"]}</a>' for a in FOCUS)
        body += section("AREA", f"{s['short']}の清掃 対応エリア。", f'''      <div class="prose"><p>埼玉県(川口・蕨・戸田・浦和・大宮・越谷・草加など)と東京都(足立区・北区・板橋区・豊島区・新宿区・渋谷区など)の{s['short']}に伺います。地域ごとの建物の傾向や作業の段取りは、各エリアのページをご覧ください。</p></div>
      <div class="tag-list">{area_links}<a href="@@/area/">対応エリア一覧</a></div>''',
                        band=s["slug"] not in SPEC_WORKS)
        body += section("FAQ", f"{s['short']}の清掃 よくあるご質問。", faq_details(s["faqs"]),
                        band=s["slug"] in SPEC_WORKS)
        others = [(f"@@/specialty/{o['slug']}/", o["h1"], o["lead"][:44] + "…") for o in SPECIALTIES if o["slug"] != s["slug"]][:6]
        body += section("OTHER", "ほかの診療科目のご案内。", link_cards(others) +
                        '\n      <p style="margin-top:22px;font-size:13px;"><a href="@@/specialty/" style="color:var(--gold);">診療科目別のご案内 一覧 →</a></p>',
                        band=s["slug"] not in SPEC_WORKS)
        body += cta_banner(h2=f"{s['short']}の清掃、まずはご相談ください。")
        write_page(path, s["title"], s["desc"], body,
                   crumbs=[("診療科目別のご案内", "specialty/"), (s["h1"], None)],
                   graph=[service_node(s["h1"], s["desc"], path, f"{s['short']}の清掃"), faq_jsonld(s["faqs"])],
                   hero=sub_hero("CLINIC CLEANING", s["h1"].replace("の定期清掃", "の<br>定期清掃").replace("の清掃・", "の<br>清掃・").replace("の清掃業者", "の<br>清掃業者"),
                                 s["lead"]),
                   priority="0.8")
