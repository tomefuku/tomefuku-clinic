# -*- coding: utf-8 -*-
"""対応エリアページ(/area/)"""
from content_areas import AREAS, AREA_BY_SLUG, OTHER_TOKYO, OTHER_SAITAMA
from content_common import WORKS, SPECIALTY_LIST, SERVICES
from parts import section, prose, strength, link_cards, cta_banner, works_grid


def build(write_page, sub_hero):
    from build import service_node

    sai = [a for a in AREAS if a["pref"] == "埼玉県"]
    tok = [a for a in AREAS if a["pref"] == "東京都"]

    def area_links(lst, main=False):
        cls = "area-list main" if main else "area-list"
        return f'<div class="{cls}">' + "".join(f'<a href="@@/area/{a["slug"]}/">{a["name"]}</a>' for a in lst) + "</div>"

    # ---- 一覧
    inner = f'''      <div class="area-pref">
        <div class="area-block-label">埼玉県(重点エリア)</div>
        {area_links(sai, main=True)}
      </div>
      <div class="area-pref">
        <div class="area-block-label">東京都(重点エリア)</div>
        {area_links(tok, main=True)}
      </div>
      <div class="area-pref">
        <div class="area-block-label">そのほかのご相談可能エリア</div>
        <p class="area-note">東京都:{"・".join(OTHER_TOKYO)}<br>埼玉県:{"・".join(OTHER_SAITAMA)} など<br>上記以外の地域も、医院の場所・ご依頼内容によって対応できる場合があります。お気軽にご相談ください。</p>
      </div>'''
    body = section("AREA", "クリニック清掃の対応エリア一覧。", inner,
                   desc="留福美装はさいたま市大宮区に拠点を置き、埼玉県南部・東部と東京都内のクリニック・医院・歯科医院の床清掃・定期清掃・業務用エアコン洗浄に伺っています。市区町村は現在の正式名称で掲載しています。")
    body += section("NOTE", "地域ごとのページについて。", prose('''
        <p>同じ「クリニックの床清掃」でも、駅前のテナントビルに入る医院と、駐車場のある郊外の戸建て型の医院とでは、作業できる時間帯や機材の搬入経路、汚れ方が大きく異なります。各エリアのページでは、その地域の医療機関の立地や建物の傾向と、留福美装が現地で確認していること・作業の段取りをご紹介しています。</p>
        <p>分院が複数の市区にまたがる場合も、まとめて日程を組むことができます。</p>
'''), band=True)
    body += cta_banner()
    write_page("area/",
               "対応エリア一覧｜東京都・埼玉県のクリニック清掃・床清掃｜留福美装",
               "留福美装のクリニック清掃の対応エリア。埼玉県(川口市・蕨市・戸田市・さいたま市・越谷市・草加市など)と東京都(足立区・北区・板橋区・豊島区・新宿区・渋谷区など)の医院・歯科医院の床清掃・定期清掃に対応します。",
               body, crumbs=[("対応エリア", None)],
               hero=sub_hero("AREA", "クリニック清掃の<br>対応エリア",
                             "さいたま市大宮区の拠点から、埼玉県南部・東部と東京都内の医院・歯科医院へ。地域ごとの建物の傾向に合わせて作業の段取りを組みます。"),
               priority="0.8")

    # ---- 各エリア
    for a in AREAS:
        path = f"area/{a['slug']}/"
        nm, sh = a["name"], a["short"]
        ctx = "\n".join(f"        <p>{p}</p>" for p in a["context"])
        stations = "".join(f"<span>{s}</span>" for s in a["stations"])
        body = section("ABOUT", f"{nm}のクリニック・医院の清掃について。", prose(f'''
        <p>{a["intro"]}</p>
{ctx}
''') + f'''
      <div style="margin-top:8px;">
        <div class="area-block-label">{nm}の主な対応エリア(駅周辺)</div>
        <div class="area-list">{stations}</div>
        <p class="area-note" style="margin-top:12px;">上記の駅周辺に限らず、{nm}内全域のクリニック・医院・歯科医院からのご相談を承ります。</p>
      </div>''')
        pts = list(a["points"]) + [("check", "料金と範囲を事前に明確に", "作業前に金額と作業範囲をお伝えします。お見積もりは無料です。")]
        body += section("POINT", f"{nm}で作業するときに確認していること。", strength(pts), band=True)
        svc = [(f"@@/{p}", f"{sh}の{n}" if p != "price/" else "料金", d) for p, n, d in SERVICES]
        body += section("SERVICE", f"{nm}で対応している清掃メニュー。", link_cards(svc))
        spc = "".join(f'<a href="@@/specialty/{s}/">{sh}の{n}</a>' for s, n, _ in SPECIALTY_LIST)
        body += section("CLINIC", f"{sh}の歯科医院・眼科・各種クリニックの方へ。",
                        f'''      <div class="prose"><p>{nm}の歯科医院・眼科・内科・皮膚科・整形外科・美容クリニック・小児科・耳鼻咽喉科・婦人科・心療内科など、診療科目ごとの清掃のポイントは以下のページでご紹介しています。</p></div>
      <div class="tag-list">{spc}</div>''', band=True)
        band = False
        if a.get("works"):
            body += section("WORKS", f"{nm}での施工事例。", works_grid([WORKS[k] for k in a["works"]]))
            band = True
        nb = [AREA_BY_SLUG[s] for s in a["neighbors"] if s in AREA_BY_SLUG]
        body += section("NEARBY", "近隣の対応エリア。", area_links(nb) +
                        '\n      <p class="area-note" style="margin-top:18px;"><a href="@@/area/" style="color:var(--gold);">対応エリア一覧を見る →</a></p>', band=band)
        body += cta_banner(h2=f"{nm}のクリニック清掃、まずはご相談ください。",
                           p=f"{nm}内の医院の場所・面積・気になる床の状態をお知らせください。現地確認のうえ、無料でお見積もりをご案内します。")
        title = f"{nm}のクリニック定期清掃・床清掃｜歯科医院・医院の清掃業者｜留福美装"
        desc = (f"{a['pref']}{nm}のクリニック・医院・歯科医院の定期清掃、床洗浄・ワックス、剥離洗浄、業務用エアコン洗浄。"
                f"{'・'.join(a['stations'][:3])}周辺など{nm}全域に対応。{a['points'][0][1]}など、地域の建物に合わせて作業します。")
        area_node = [{"@type": "City", "name": a["pref"] + nm}]
        write_page(path, title, desc, body,
                   crumbs=[("対応エリア", "area/"), (nm, None)],
                   graph=[service_node(f"{nm}のクリニック清掃", desc, path, "クリニック定期清掃・床清掃", area=area_node)],
                   hero=sub_hero(f"AREA — {a['pref']}", f"{nm}の<br>クリニック清掃・床清掃",
                                 f"{nm}のクリニック・医院・歯科医院の床洗浄・ワックス、剥離洗浄、定期清掃、業務用エアコン洗浄。地域の建物の特徴に合わせて、診療に影響しない時間帯に作業します。"),
                   priority="0.7")
