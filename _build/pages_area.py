# -*- coding: utf-8 -*-
"""対応エリアページ(/area/)  埼玉県・東京都は市区町村ごと、関東の他5県は県ごと"""
from content_areas import AREAS, AREA_BY_SLUG
from content_prefs import PREFS
from content_common import WORKS, SPECIALTY_LIST, SERVICES
from parts import section, prose, strength, link_cards, cta_banner, works_grid

MAIN_SAITAMA = ["kawaguchi", "toda", "warabi", "saitama"]


def _links(lst, main=False):
    cls = "area-list main" if main else "area-list"
    return f'<div class="{cls}">' + "".join(f'<a href="@@/area/{a["slug"]}/">{a["name"]}</a>' for a in lst) + "</div>"


def _block(label, lst, main=False):
    if not lst:
        return ""
    return f'''      <div class="area-pref">
        <div class="area-block-label">{label}</div>
        {_links(lst, main)}
      </div>'''


def build(write_page, sub_hero):
    from build import service_node

    sai = [a for a in AREAS if a["pref"] == "埼玉県"]
    tok = [a for a in AREAS if a["pref"] == "東京都"]
    sai_city = [a for a in sai if a["name"].endswith("市")]
    sai_town = [a for a in sai if not a["name"].endswith("市")]
    tok_ku = [a for a in tok if a["name"].endswith("区")]
    tok_city = [a for a in tok if a["name"].endswith("市")]
    tok_town = [a for a in tok if not a["name"].endswith(("区", "市")) and a.get("type") != "island"]
    tok_island = [a for a in tok if a.get("type") == "island"]
    main = [AREA_BY_SLUG[s] for s in MAIN_SAITAMA]

    # ---- 一覧
    pref_links = "".join(f'<a href="@@/area/{p["slug"]}/">{p["name"]}</a>' for p in PREFS)
    inner = f'''      <h3 class="sol-h3" id="saitama">埼玉県(全63市町村)</h3>
{_block("メインエリア(拠点から近い地域)", main, True)}
{_block("市", [a for a in sai_city if a["slug"] not in MAIN_SAITAMA])}
{_block("町・村", sai_town)}
      <h3 class="sol-h3" id="tokyo" style="margin-top:40px;">東京都(全62市区町村)</h3>
{_block("東京23区", tok_ku, True)}
{_block("多摩地域の市", tok_city)}
{_block("町・村", tok_town)}
{_block("島しょ部", tok_island)}
      <h3 class="sol-h3" id="kanto" style="margin-top:40px;">関東のその他の県</h3>
      <div class="area-pref"><div class="area-list main">{pref_links}</div>
        <p class="area-note" style="margin-top:12px;">各県のページに、対応している全市町村の名前を掲載しています。</p></div>'''
    body = section("AREA", "クリニック清掃の対応エリア一覧。", inner,
                   desc="留福美装はさいたま市大宮区に拠点を置き、埼玉県・東京都を中心に、神奈川県・千葉県・茨城県・栃木県・群馬県まで関東全域のクリニック・医院・歯科医院に伺います。市区町村は現在の正式名称で掲載しています。遠方の場合は、別途出張費をいただくことがあります。")
    body += section("NOTE", "地域ごとのページについて。", prose('''
        <p>同じ「クリニックの床清掃」でも、駅前のテナントビルに入る医院と、駐車場のある郊外の戸建て型の医院とでは、作業できる時間帯や機材の搬入経路、汚れ方が大きく異なります。各エリアのページでは、その地域の駅や立地、医療機関の建物の傾向と、留福美装が現地で確認していること・作業の段取りをご紹介しています。</p>
        <p>分院が複数の市区町村や県にまたがる場合も、まとめて日程を組むことができます。出張費が必要な地域では、金額をお見積もりの段階で必ずご案内します。</p>
'''), band=True)
    body += cta_banner()
    write_page("area/",
               "対応エリア一覧｜埼玉県・東京都・関東全域のクリニック清掃・床清掃｜留福美装",
               "留福美装のクリニック清掃の対応エリア。埼玉県の全63市町村、東京都の全62市区町村に加え、神奈川県・千葉県・茨城県・栃木県・群馬県まで関東全域の医院・歯科医院の床清掃・定期清掃・業務用エアコン洗浄に対応します。",
               body, crumbs=[("対応エリア", None)],
               hero=sub_hero("AREA", "クリニック清掃の<br>対応エリア",
                             "さいたま市大宮区の拠点から、埼玉県・東京都を中心に関東全域の医院・歯科医院へ。地域ごとの建物の傾向に合わせて作業の段取りを組みます。"),
               priority="0.8")

    # ---- 各市区町村
    for a in AREAS:
        path = f"area/{a['slug']}/"
        nm, sh = a["name"], a["short"]
        ctx = "\n".join(f"        <p>{p}</p>" for p in a["context"])
        if a["stations"]:
            stations = "".join(f"<span>{s}</span>" for s in a["stations"])
            st_block = f'''
      <div style="margin-top:8px;">
        <div class="area-block-label">{nm}の主な対応エリア(駅周辺)</div>
        <div class="area-list">{stations}</div>
        <p class="area-note" style="margin-top:12px;">上記の駅周辺に限らず、{nm}内全域のクリニック・医院・歯科医院からのご相談を承ります。</p>
      </div>'''
        else:
            st_block = f'''
      <p class="area-note" style="margin-top:8px;">{nm}内全域のクリニック・医院・歯科医院・診療所からのご相談を承ります。</p>'''
        body = section("ABOUT", f"{nm}のクリニック・医院の清掃について。", prose(f'''
        <p>{a["intro"]}</p>
{ctx}
''') + st_block)
        if a.get("extra"):
            body += section("AZABU-JUBAN", a["extra_h2"], prose("\n".join(f"        <p>{p}</p>" for p in a["extra"])), band=True)
        pts = list(a["points"]) + [("check", "料金と範囲を事前に明確に", "作業前に金額と作業範囲をお伝えします。お見積もりは無料です。")]
        body += section("POINT", f"{nm}で作業するときに確認していること。", strength(pts), band=not a.get("extra"))
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
        nb = [AREA_BY_SLUG[s] for s in a["neighbors"] if s in AREA_BY_SLUG and s != a["slug"]]
        pref_anchor = "saitama" if a["pref"] == "埼玉県" else "tokyo"
        body += section("NEARBY", "近隣の対応エリア。", (_links(nb) if nb else "") +
                        f'\n      <p class="area-note" style="margin-top:18px;"><a href="@@/area/#{pref_anchor}" style="color:var(--gold);">{a["pref"]}の対応エリア一覧を見る →</a></p>', band=band)
        body += cta_banner(h2=f"{nm}のクリニック清掃、まずはご相談ください。",
                           p=f"{nm}内の医院の場所・面積・気になる床の状態をお知らせください。現地確認のうえ、無料でお見積もりをご案内します。")
        title = a.get("title") or f"{nm}のクリニック定期清掃・床清掃｜歯科医院・医院の清掃業者｜留福美装"
        where = f"{'・'.join(a['stations'][:3])}周辺など{nm}全域に対応。" if a["stations"] else f"{nm}全域に対応。"
        desc = (f"{a['pref']}{nm}のクリニック・医院・歯科医院の定期清掃、床洗浄・ワックス、剥離洗浄、業務用エアコン洗浄。"
                f"{where}{a['points'][0][1]}など、地域の建物に合わせて作業します。")
        hero_kw = {"img": a["hero_img"][0], "alt": a["hero_img"][1]} if a.get("hero_img") else {}
        write_page(path, title, desc, body,
                   crumbs=[("対応エリア", "area/"), (nm, None)],
                   graph=[service_node(f"{nm}のクリニック清掃", desc, path, "クリニック定期清掃・床清掃",
                                       area=[{"@type": "City", "name": a["pref"] + nm}])],
                   hero=sub_hero(f"AREA — {a['pref']}", a.get("h1") or f"{nm}の<br>クリニック清掃・床清掃",
                                 f"{nm}のクリニック・医院・歯科医院の床洗浄・ワックス、剥離洗浄、定期清掃、業務用エアコン洗浄。地域の建物の特徴に合わせて、診療に影響しない時間帯に作業します。",
                                 **hero_kw),
                   priority="0.6" if a.get("far") else "0.7")

    # ---- 関東の他5県
    for p in PREFS:
        path = f"area/{p['slug']}/"
        nm = p["name"]
        groups = "\n".join(
            f'''      <div class="area-pref">
        <div class="area-block-label">{nm}の{g}({len(lst)})</div>
        <div class="area-list">{"".join(f"<span>{x}</span>" for x in lst)}</div>
      </div>''' for g, lst in p["groups"])
        total = sum(len(l) for _, l in p["groups"])
        body = section("ABOUT", f"{nm}のクリニック・医院の清掃について。", prose(f'''
        <p>{p["intro"]}</p>
        <p>留福美装はさいたま市大宮区の拠点から、{nm}のクリニック・医院・歯科医院の床洗浄・ワックス、剥離洗浄、定期清掃、業務用エアコン洗浄に伺います。駅前ビルのクリニックではビルの作業ルールに合わせて、駐車場のある戸建て型の医院では入口まわりの汚れや床面積に合わせて、作業の段取りを組みます。</p>
        <p>{p["note"]}出張費を含めた金額は、お見積もりの段階で必ずご案内します。</p>
'''))
        body += section("AREA", f"{nm}の対応市町村(全{total}市町村)。", groups +
                        f'\n      <p class="area-note" style="margin-top:12px;">{nm}内の全市町村のクリニック・医院・歯科医院・診療所からのご相談を承ります。</p>', band=True)
        body += section("POINT", f"{nm}で作業するときに確認していること。", strength([
            ("pin", "移動と日程の段取り", "現地確認・お見積もり・初回作業の日程をまとめて組むなど、訪問回数を抑えます。"),
            ("box", "建物に合わせた準備", "ビルの作業申請、駐車場所、搬入経路を事前に確認します。"),
            ("chart", "複数院をまとめて", "県内・県外の分院とあわせて、窓口ひとつで日程を組めます。"),
            ("check", "出張費も事前に明確に", "遠方の場合の出張費も、作業前に金額をお伝えします。"),
        ]))
        svc = [(f"@@/{s}", f"{nm}の{n}" if s != "price/" else "料金", d) for s, n, d in SERVICES]
        body += section("SERVICE", f"{nm}で対応している清掃メニュー。", link_cards(svc), band=True)
        spc = "".join(f'<a href="@@/specialty/{s}/">{nm}の{n}</a>' for s, n, _ in SPECIALTY_LIST)
        others = "".join(f'<a href="@@/area/{q["slug"]}/">{q["name"]}</a>' for q in PREFS if q["slug"] != p["slug"])
        body += section("CLINIC", f"{nm}の歯科医院・眼科・各種クリニックの方へ。",
                        f'      <div class="tag-list">{spc}</div>\n      <h3 class="sol-h3" style="margin-top:36px;">関東のその他のエリア</h3>\n      <div class="area-list"><a href="@@/area/#saitama">埼玉県</a><a href="@@/area/#tokyo">東京都</a>{others}</div>')
        body += cta_banner(h2=f"{nm}のクリニック清掃、まずはご相談ください。",
                           p=f"{nm}内の医院の場所・面積・気になる床の状態をお知らせください。出張費を含めて、無料でお見積もりをご案内します。")
        desc = (f"{nm}のクリニック・医院・歯科医院の定期清掃、床洗浄・ワックス、剥離洗浄、業務用エアコン洗浄。"
                f"{nm}の全{total}市町村に対応し、複数院の清掃も窓口ひとつでまとめてお受けします。")
        write_page(path, f"{nm}のクリニック定期清掃・床清掃｜歯科医院・医院の清掃業者｜留福美装", desc, body,
                   crumbs=[("対応エリア", "area/"), (nm, None)],
                   graph=[service_node(f"{nm}のクリニック清掃", desc, path, "クリニック定期清掃・床清掃",
                                       area=[{"@type": "AdministrativeArea", "name": nm}])],
                   hero=sub_hero(f"AREA — {nm}", f"{nm}の<br>クリニック清掃・床清掃",
                                 f"{nm}の全{total}市町村のクリニック・医院・歯科医院へ伺います。床洗浄・ワックス、剥離洗浄、定期清掃、業務用エアコン洗浄まで、窓口ひとつでお受けします。"),
                   priority="0.6")
