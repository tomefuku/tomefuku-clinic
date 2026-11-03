# -*- coding: utf-8 -*-
"""トップページ(tomefuku.jp と同じ構成・同じ順番で、内容をクリニック清掃専門に)"""
from config import COMPANY as C, PRICES, price_or_estimate
from content_common import WORKS, WORKS_ORDER, WORKS_TABS, SPECIALTY_LIST, SERVICES
from content_areas import AREAS, AREA_BY_SLUG
from parts import faq_details, faq_jsonld

TOP_FAQS = [
    ("診療時間外や夜間の清掃は可能ですか？",
     "可能です。休診日・診療終了後・夜間など、診療に影響しない時間帯に作業します。これまでも美容クリニック様の床洗浄・カーペット洗浄・業務用エアコン洗浄を夜間に行っています。ワックスの乾燥時間も含め、翌日の診療に支障が出ない日程をご提案します。"),
    ("クリニックの床清掃はどのくらいの頻度が必要ですか？",
     "来院者数や床材、日常清掃の状況によって異なります。待合室など人の出入りが多い場所は1〜3か月に1回程度の床洗浄、年1回程度の剥離洗浄を一つの目安として、床の状態を確認したうえでご提案します。詳しくは<a href=\"@@/column/floor-cleaning-frequency/\">コラム「クリニックの床清掃はどのくらいの頻度が必要？」</a>をご覧ください。"),
    ("定期清掃と日常清掃の違いは何ですか？",
     "日常清掃は掃き掃除・モップ拭き・ゴミ回収など毎日行う清掃で、院内スタッフの方が行っている医院様も多くあります。定期清掃は、ポリッシャーによる床洗浄やワックス塗布、カーペット洗浄など、専用の機材と洗剤を使って月1回〜数か月に1回行う清掃です。留福美装は定期清掃を中心にお受けしています。"),
    ("床の黒ずみや汚れは改善できますか？",
     "床の表面やワックス層に付いた黒ずみは、床洗浄や剥離洗浄で改善できる場合が多くあります。ただし、床材そのものの傷・変色・薬剤による変質は落としきれないことがあります。現地で状態を確認し、改善が見込める範囲を事前にご説明します。"),
    ("医療機器や薬品がある部屋も清掃してもらえますか？",
     "清掃できます。医療機器は動かさず、作業範囲と養生する場所を事前に確認してから作業します。立ち入りできない部屋や清掃の手順など、院内のルールがあれば事前にお知らせください。"),
    ("料金はどのように決まりますか？見積もりは無料ですか？",
     "床清掃は面積・床材・汚れの状態・作業時間帯によって決まるため、現地確認のうえでお見積もりします。お見積もりは無料です。業務用エアコン洗浄は1台33,000円(税込)〜、フィルター清掃は1台3,300円(税込)です。詳しくは<a href=\"@@/price/\">料金ページ</a>をご覧ください。"),
    ("今の清掃業者から変更する場合、どのような流れになりますか？",
     "お問い合わせ後、現地で床の状態や清掃範囲を確認し、お見積もりと清掃計画をご提案します。現在の契約期間や解約時期を踏まえて開始日を決め、必要に応じて初回に剥離洗浄で床を整えてから定期清掃を始めます。"),
    ("床清掃と業務用エアコン洗浄をまとめて依頼できますか？",
     "まとめてご依頼いただけます。床洗浄・ワックス、カーペット洗浄、ガラス清掃、業務用エアコン洗浄・フィルター清掃を一つの窓口でお受けできるため、業者ごとの日程調整の手間を減らせます。"),
    ("複数の院(分院)をまとめて依頼できますか？",
     "可能です。関東で多院展開する美容クリニック様の全院を担当しています。院ごとに日程を分けることも、全院共通の計画でまとめて手配することもできます。"),
    ("対応エリアを教えてください。",
     "埼玉県(川口市・蕨市・戸田市・さいたま市・越谷市・草加市など)と東京都(足立区・北区・板橋区・豊島区・新宿区・渋谷区など)を中心に対応しています。その他の地域もご相談ください。詳しくは<a href=\"@@/area/\">対応エリア</a>をご覧ください。"),
]

SERVICE_OPTIONS = ["床洗浄・ワックス", "床剥離洗浄", "定期清掃", "待合室・診察室の床清掃", "カーペット洗浄",
                   "ガラス清掃", "業務用エアコン洗浄", "エアコンフィルター清掃", "その他・未定"]
FREQ_OPTIONS = ["1回のみ(スポット)", "毎月", "2か月に1回", "3か月に1回", "半年に1回", "年1回", "未定・相談したい"]


def contact_section(heading="まずはご相談ください。", h_tag="h2"):
    checks = "\n".join(
        f'            <label><input type="checkbox" name="service" value="{o}"><span>{o}</span></label>' for o in SERVICE_OPTIONS)
    opts = "\n".join(f'            <option value="{o}">{o}</option>' for o in FREQ_OPTIONS)
    return f'''
  <section class="section-pad contact-band" id="contact">
    <div class="wrap">
      <div class="sec-head reveal">
        <span class="kicker">CONTACT</span>
        <{h_tag}>{heading}</{h_tag}>
        <p class="desc">医院・施設の場所、気になっている床の状態、ご希望の清掃内容と頻度をお聞かせください。現地確認のうえ、料金と作業内容をご案内します。お見積もりは無料です。</p>
      </div>
      <div class="contact-grid">
        <a class="contact-card" href="tel:{C["tel_mobile_link"]}">
          <div class="k">TEL(携帯)</div>
          <div class="v">{C["tel_mobile"]}</div>
        </a>
        <a class="contact-card" href="tel:{C["tel_fixed_link"]}">
          <div class="k">TEL(固定)</div>
          <div class="v">{C["tel_fixed"]}</div>
        </a>
        <a class="contact-card" href="mailto:{C["email"]}">
          <div class="k">MAIL</div>
          <div class="v" style="font-size:14px;">{C["email"]}</div>
        </a>
      </div>
      <form class="contact-form" id="contactForm">
        <div class="cf-field">
          <label class="cf-label" for="cf-clinic">医院・施設名 <span class="cf-required">必須</span></label>
          <input type="text" id="cf-clinic" name="clinic" autocomplete="organization" placeholder="例)○○歯科クリニック" required>
        </div>
        <div class="cf-field">
          <label class="cf-label" for="cf-name">ご担当者名 <span class="cf-required">必須</span></label>
          <input type="text" id="cf-name" name="name" autocomplete="name" placeholder="例)院長 山田 太郎/事務長 佐藤" required>
        </div>
        <div class="cf-field">
          <label class="cf-label" for="cf-address">所在地 <span class="cf-optional">任意</span></label>
          <input type="text" id="cf-address" name="address" autocomplete="street-address" placeholder="例)埼玉県川口市○○(市区町村までで構いません)">
        </div>
        <div class="cf-field">
          <label class="cf-label" for="cf-tel">電話番号 <span class="cf-required">必須</span></label>
          <input type="tel" id="cf-tel" name="tel" autocomplete="tel" inputmode="tel" required>
        </div>
        <div class="cf-field">
          <label class="cf-label" for="cf-email">メールアドレス <span class="cf-required">必須</span></label>
          <input type="email" id="cf-email" name="email" autocomplete="email" inputmode="email" required>
        </div>
        <fieldset class="cf-field" style="border:none;padding:0;margin-left:0;margin-right:0;">
          <legend class="cf-label">希望する清掃内容 <span class="cf-optional">複数選択可</span></legend>
          <div class="cf-checks">
{checks}
          </div>
        </fieldset>
        <div class="cf-field">
          <label class="cf-label" for="cf-frequency">希望する清掃頻度 <span class="cf-optional">任意</span></label>
          <select id="cf-frequency" name="frequency">
            <option value="">選択してください</option>
{opts}
          </select>
        </div>
        <div class="cf-field">
          <label class="cf-label" for="cf-message">お問い合わせ内容 <span class="cf-optional">任意</span></label>
          <textarea id="cf-message" name="message" placeholder="例)待合室と診察室あわせて約60㎡。床の黒ずみが気になっています。休診日の日曜に作業を希望します。"></textarea>
        </div>
        <button type="submit" class="cf-submit">送信する</button>
      </form>
      <p class="cf-note" id="cfNote">送信いただいた内容は留福美装に直接届きます。内容をご確認のうえ、折り返しご連絡いたします。</p>
      <iframe name="hidden_iframe" id="hidden_iframe" title="送信処理用" style="display:none;"></iframe>
    </div>
  </section>
'''


def card(href, name, price_html, note, more="詳しく見る", featured=False, kicker=None, tagset=None):
    cls = "price-card featured" if featured else "price-card"
    k = f'\n          <div class="kicker-set">{kicker}</div>' if kicker else ""
    t = ("\n          <div class=\"tagset\">" + "".join(f"<span>{x}</span>" for x in tagset) + "</div>") if tagset else ""
    return f'''        <a class="{cls}" href="{href}">{k}
          <div class="name">{name}</div>
          <div class="note">{note}</div>{t}
          {price_html}
          <div class="more">{more}</div>
        </a>'''


EST = '<div class="price" style="font-size:15px;">お見積もり</div>'


def price_section():
    a_from = PRICES["aircon_from"]
    cards = [
        card("@@/floor-wax/", "クリニック床洗浄・ワックス", EST,
             "待合室・診察室・処置室・廊下の床を洗浄し、ワックスで保護します。料金は面積別。床材と汚れの状態を確認してお見積もりします。",
             featured=True, kicker="MAIN SERVICE", tagset=["休診日・夜間対応", "面積別料金", "医療機器に配慮"]),
        card("@@/teiki/", "クリニック定期清掃", EST, "月額プランで床・カーペット・ガラスなどを定期的に"),
        card("@@/hakuri/", "床剥離洗浄", EST, "古いワックスと黒ずみを剥がして床をリセット"),
        card("@@/floor-wax/#waiting", "待合室・診察室の床清掃", EST, "来院者の動線の黒ずみを重点的に"),
        card("@@/specialty/dental/", "医院・歯科医院の定期清掃", EST, "ユニットまわりの床・キッズスペースにも配慮"),
        card("@@/aircon/", "業務用エアコン洗浄", f'<div class="price">{a_from}<small>円(税込)〜/台</small></div>',
             "天井埋込型・天吊り型の分解洗浄。診療時間外・夜間の作業に対応します。<br>実績:関東で多院展開する美容クリニック様の全院を担当",
             featured=True, kicker="AIR CONDITIONER", tagset=["複数院一括対応", "夜間対応可"]),
        card("@@/aircon/#filter", "エアコンフィルター清掃",
             f'<div class="price">{PRICES["filter"].replace("円/台", "")}<small>円(税込)/台</small></div>', "業務用エアコンのフィルターを洗浄"),
        card("@@/teiki/#glass", "ガラス清掃", f'<div class="price" style="font-size:15px;">{price_or_estimate(PRICES["glass"])}</div>',
             "入口・待合室の窓ガラスや自動ドア"),
        card("@@/teiki/#carpet", "カーペット洗浄", f'<div class="price" style="font-size:15px;">{price_or_estimate(PRICES["carpet"])}</div>',
             "待合室・施術室のカーペットを洗浄"),
        card("@@/price/", "料金一覧", '<div class="price" style="font-size:15px;">面積別・月額プラン</div>',
             "床清掃の面積別料金と定期清掃の月額プラン", more="料金表を見る"),
    ]
    return f'''
  <!-- 02 SERVICE / PRICE MENU -->
  <section class="section-pad" id="price">
    <div class="wrap">
      <div class="sec-head reveal">
        <span class="kicker">SERVICE / PRICE</span>
        <h2 id="service">何を頼めて、いくらか。</h2>
        <p class="desc">クリニック・医院・歯科医院向けの主な清掃メニューです。床清掃は面積・床材・汚れの状態によって金額が変わるため、現地確認(無料)のうえでお見積もりをご案内します。業務用エアコン洗浄は台数・機種ごとの料金です。</p>
      </div>

      <div class="price-grid">
{chr(10).join(cards)}
      </div>
      <p class="menu-note">表示価格は税込です。建物の状態や汚れ具合、作業時間帯により変動する場合があります。お見積もり後に追加料金が発生する場合は、作業前に必ずご案内します。</p>
      <div class="menu-cta"><a class="btn" href="#contact">料金について相談する</a></div>
    </div>
  </section>
'''


STRENGTH = '''
  <!-- 03 STRENGTH -->
  <section class="section-pad band">
    <div class="wrap">
      <div class="sec-head reveal">
        <span class="kicker">STRENGTH</span>
        <h2>医院様に選ばれる理由。</h2>
      </div>
      <div class="strength-grid">
        <div class="strength-item">
          <div class="mark"><svg viewBox="0 0 24 24" fill="none" stroke="#1f3d2e" stroke-width="1.6"><circle cx="12" cy="12" r="8"/><path d="M12 8v4l3 2"/></svg></div>
          <h3>診療を止めない作業時間</h3>
          <p>休診日・診療終了後・夜間に作業します。ワックスの乾燥時間まで含めて、翌日の診療に影響しない日程を組みます。</p>
        </div>
        <div class="strength-item">
          <div class="mark"><svg viewBox="0 0 24 24" fill="none" stroke="#1f3d2e" stroke-width="1.6"><path d="M4 12h16M4 6h10M4 18h13"/></svg></div>
          <h3>明確な料金とお見積もり</h3>
          <p>作業前に金額と作業範囲をはっきりお伝えします。院長先生・事務長様が予算を立てやすい、面積別・月額プランでご提案します。</p>
        </div>
        <div class="strength-item">
          <div class="mark"><svg viewBox="0 0 24 24" fill="none" stroke="#1f3d2e" stroke-width="1.6"><rect x="4" y="5" width="16" height="14" rx="1"/><path d="M4 10h16"/></svg></div>
          <h3>床もエアコンも一つの窓口で</h3>
          <p>床洗浄・ワックス、剥離洗浄、カーペット・ガラス清掃、業務用エアコン洗浄までまとめてお任せいただけます。分院ごとに異なる業者の管理の手間も減らせます。</p>
        </div>
        <div class="strength-item">
          <div class="mark"><svg viewBox="0 0 24 24" fill="none" stroke="#1f3d2e" stroke-width="1.6"><path d="M4 17l6-6 4 4 6-8"/></svg></div>
          <h3>多院展開クリニックの全院を担当</h3>
          <p>関東で多院展開する美容クリニック様の全院を担当しています。医療機器や院内のルールを尊重し、毎回同じ品質で仕上げます。</p>
        </div>
      </div>
    </div>
  </section>
'''


def works_section():
    tabs = "\n".join(
        f'        <button type="button" role="tab" data-cat="{t}"{" class=\"active\" aria-selected=\"true\"" if i == 0 else " aria-selected=\"false\""}>{t}</button>'
        for i, t in enumerate(WORKS_TABS))
    cards = "\n".join(WORKS[k] for k in WORKS_ORDER)
    return f'''
  <!-- 04 WORKS -->
  <section class="section-pad" id="works">
    <div class="wrap">
      <div class="sec-head reveal">
        <span class="kicker">WORKS</span>
        <h2>施工事例。</h2>
        <p class="desc">クリニック・医院での床洗浄、カーペット洗浄、業務用エアコン洗浄の施工事例です。施工事例は順次追加していきます。</p>
      </div>
      <div class="works-tabs" role="tablist" aria-label="施工事例のカテゴリー">
{tabs}
      </div>
      <div class="works-grid">
{cards}
      </div>
    </div>
  </section>
'''


def sd(id_, title, price, intro, lists, link, extra=""):
    p = f'\n            <div class="sd-price">{price}</div>' if price else ""
    i = f'\n            <p style="font-size:13.5px;color:var(--ink-soft);">{intro}</p>' if intro else ""
    ls = "".join(f'\n            <h4>{h}</h4>\n            <ul>' + "".join(f"\n              <li>{x}</li>" for x in items) + "\n            </ul>"
                 for h, items in lists)
    return f'''
      <details class="sd-item" id="{id_}">
        <summary>{title} <span class="plus">+</span></summary>
        <div class="sd-body">
          <div>{i}{p}{ls}{extra}
            <p style="font-size:13.5px;margin-bottom:16px;"><a href="{link[0]}" style="color:var(--gold);">{link[1]}</a></p>
            <a class="btn outline" href="#contact">この内容で相談する</a>
          </div>
        </div>
      </details>
'''


def service_details():
    ac = "".join(f"<li>{n}:{p} <span style=\"color:var(--ink-soft);\">({s})</span></li>" for n, p, s in PRICES["aircon"])
    items = [
        sd("sd-floor", "クリニック床洗浄・ワックス", "面積別料金(お見積もり)",
           "待合室・受付・診察室・処置室・廊下など、院内の床をポリッシャーで洗浄し、ワックスを塗布して保護します。床材(長尺シート・塩ビタイル・フローリング・石材調タイルなど)を確認し、素材に合った方法で仕上げます。",
           [("こんな医院様におすすめ", ["待合室の動線や受付前の黒ずみが気になる", "日常のモップ拭きでは床のくすみが取れない", "開院時のきれいな床の状態を保ちたい"]),
            ("作業内容", ["家具・備品の移動(動かせる範囲)と養生", "ポリッシャーによる床洗浄・汚水回収", "すすぎ・乾燥・ワックス塗布", "備品の復旧・仕上がり確認"])],
           ("@@/floor-wax/", "クリニック床洗浄・ワックスの詳細を見る →")),
        sd("sd-hakuri", "床剥離洗浄", "面積別料金(お見積もり)",
           "古いワックスを剥離剤で取り除き、ワックス層に入り込んだ黒ずみや黄ばみごと床をリセットします。仕上げに新しいワックスを塗り重ねます。",
           [("こんな医院様におすすめ", ["通常の床洗浄では黒ずみが落ちなくなった", "長年のワックスの重ね塗りで床が黄ばんでいる", "清掃業者を変更するので、一度床を整えたい"])],
           ("@@/hakuri/", "床剥離洗浄の詳細を見る →")),
        sd("sd-teiki", "クリニック定期清掃(月額プラン)", "月額プラン(お見積もり)",
           "床洗浄・ワックス、カーペット洗浄、ガラス清掃、エアコンフィルター清掃などを組み合わせ、毎月・隔月・3か月ごとなど決まった頻度で行います。",
           [("こんな医院様におすすめ", ["清掃の手配を毎回するのが手間になっている", "年間の清掃費用を予算化しておきたい", "分院も含めて清掃の品質をそろえたい"])],
           ("@@/teiki/", "クリニック定期清掃の詳細・プランを見る →")),
        sd("sd-waiting", "待合室・診察室の床清掃", "お見積もり",
           "来院者の出入りが集中する待合室・受付前と、スタッフの動きが多い診察室・処置室を中心に床を洗浄します。ソファや受付カウンターまわりなど、汚れのたまりやすい場所を重点的に仕上げます。",
           [], ("@@/floor-wax/#waiting", "待合室・診察室の床清掃について →")),
        sd("sd-dental", "医院・歯科医院の定期清掃", "お見積もり",
           "歯科医院のユニットまわりの床、技工スペースの粉じん、キッズスペースなど、医院ごとの使われ方に合わせて清掃内容を決めます。",
           [], ("@@/specialty/", "診療科目別のご案内を見る →")),
        sd("sd-glass", "ガラス清掃", price_or_estimate(PRICES["glass"]),
           "入口の自動ドア、待合室の窓ガラス、ガラスパーテーションなどの清掃です。床の定期清掃とあわせてご依頼いただけます。",
           [], ("@@/teiki/#glass", "ガラス清掃について →")),
        sd("sd-aircon", "業務用エアコン洗浄", f"{PRICES['aircon_from']}円(税込)〜/台",
           "天井埋込型・天吊り型の業務用エアコンを分解し、高圧洗浄します。診療時間外・夜間の作業に対応し、複数院の一括対応も可能です。",
           [("料金表", [])], ("@@/aircon/", "業務用エアコン洗浄の詳細を見る →"),
           extra=f"\n            <ul>{ac}</ul>"),
        sd("sd-filter", "エアコンフィルター清掃", PRICES["filter"] + "(税込)",
           "業務用エアコンのフィルターを取り外して洗浄します。床の定期清掃とあわせて定期的に行うこともできます。",
           [], ("@@/aircon/#filter", "フィルター清掃について →")),
    ]
    # 空の "料金表" 見出しの ul を除去
    html = "".join(items).replace("\n            <h4>料金表</h4>\n            <ul>\n            </ul>", "\n            <h4>料金表</h4>")
    return f'''
  <!-- 05 SERVICE DETAILS -->
  <section class="section-pad band">
    <div class="wrap">
      <div class="sec-head reveal">
        <span class="kicker">SERVICE DETAILS</span>
        <h2>サービス詳細。</h2>
      </div>
{html}
    </div>
  </section>
'''


MID_CTA = '''
  <!-- 05.8 MID CTA -->
  <section class="section-pad cta-banner">
    <div class="wrap">
      <h2>まずはお気軽にご相談ください。</h2>
      <p>床の面積・床材・気になる汚れ、ご希望の清掃頻度をうかがい、現地確認のうえ無料でお見積もりをご案内します。</p>
      <a class="btn" href="#contact">お問い合わせはこちら</a>
    </div>
  </section>
'''


def for_clinics():
    sp = "".join(f'<a href="@@/specialty/{s}/">{n}</a>' for s, n, _ in SPECIALTY_LIST)
    sv = "".join(f'<a href="@@/{p}">{n}</a>' for p, n, _ in SERVICES)
    return f'''
  <!-- 06 FOR CLINICS -->
  <section class="section-pad" id="clinic">
    <div class="wrap">
      <div class="sec-head reveal">
        <span class="kicker">FOR CLINICS</span>
        <h2>診療科目ごとのご案内。</h2>
        <p class="desc">歯科医院のユニットまわり、眼科の検査室、整形外科のリハビリ室、小児科のキッズスペース。診療科目によって床の汚れ方も、作業で気をつけることも変わります。科目ごとの清掃のポイントをまとめました。</p>
      </div>
      <div class="fb-wrap">
        <div class="fb-col">
          <h3>診療科目から探す</h3>
          <div class="tag-list">{sp}</div>
        </div>
        <div class="fb-col">
          <h3>清掃メニューから探す</h3>
          <div class="tag-list">{sv}<a href="@@/column/">コラム</a></div>
        </div>
      </div>
      <div class="fb-result">実績:関東で多院展開する美容クリニック様の全院を担当<small>複数院の業務用エアコン洗浄・床洗浄・カーペット洗浄まで、夜間対応で一括してお任せいただいています。</small></div>
      <p style="font-size:13px;color:var(--ink-soft);margin-top:4px;">分院ごとに清掃業者が異なると、日程調整や品質の管理に手間がかかります。複数院の清掃窓口を一本化したい本部・事務局のご担当者様もご相談ください。</p>
      <div class="menu-cta"><a class="btn" href="#contact">医院・法人のご相談はこちら</a></div>
    </div>
  </section>
'''


def area_section():
    def links(slugs, label_key="short"):
        return "".join(f'<a href="@@/area/{s}/">{AREA_BY_SLUG[s][label_key]}</a>' for s in slugs)
    main = ["kawaguchi", "toda", "warabi", "saitama"]
    sai_other = [a["slug"] for a in AREAS if a["pref"] == "埼玉県" and a["slug"] not in main]
    tokyo = [a["slug"] for a in AREAS if a["pref"] == "東京都"]
    return f'''
  <!-- 07 AREA -->
  <section class="section-pad band" id="area">
    <div class="wrap">
      <div class="sec-head reveal">
        <span class="kicker">AREA</span>
        <h2>対応エリア</h2>
        <p class="desc">さいたま市大宮区の拠点から、埼玉県南部・東部と東京都内のクリニック・医院・歯科医院へ伺います。地域ごとの建物の傾向や作業の段取りは、各エリアのページでご紹介しています。掲載のない地域もお気軽にご相談ください。</p>
      </div>

      <div class="area-diagram">
        <svg viewBox="0 0 440 320" class="area-svg" aria-hidden="true">
          <path d="M120,38 C160,16 235,12 285,28 C325,40 355,62 366,92 C376,120 368,150 348,172 C335,187 322,196 308,206 C298,224 282,238 262,244 C244,250 226,244 216,228 C206,236 190,240 176,232 C182,214 190,198 196,182 C168,196 132,198 104,182 C78,168 62,142 66,114 C58,100 56,84 66,70 C78,52 100,44 120,38 Z" fill="var(--green-mist)" stroke="var(--green)" stroke-width="1.6"/>
          <ellipse cx="270" cy="205" rx="66" ry="46" fill="var(--gold)" opacity=".24"/>
          <ellipse cx="270" cy="205" rx="66" ry="46" fill="none" stroke="var(--gold)" stroke-width="1.4" stroke-dasharray="3 4"/>
          <g font-family="Zen Kaku Gothic New, sans-serif">
            <circle cx="250" cy="192" r="4.5" fill="var(--green-deep)"/>
            <text x="250" y="180" text-anchor="middle" font-size="12" fill="var(--ink)">戸田</text>
            <circle cx="292" cy="192" r="4.5" fill="var(--green-deep)"/>
            <text x="292" y="180" text-anchor="middle" font-size="12" fill="var(--ink)">大宮</text>
            <circle cx="250" cy="218" r="4.5" fill="var(--green-deep)"/>
            <text x="236" y="238" text-anchor="middle" font-size="12" fill="var(--ink)">川口</text>
            <circle cx="292" cy="218" r="4.5" fill="var(--green-deep)"/>
            <text x="306" y="238" text-anchor="middle" font-size="12" fill="var(--ink)">浦和</text>
          </g>
          <text x="90" y="60" font-family="Fraunces, serif" font-size="13" letter-spacing="2" fill="var(--ink-soft)">SAITAMA</text>
          <text x="322" y="245" font-family="Fraunces, serif" font-size="10" letter-spacing="1.5" fill="var(--ink-soft)">→ TOKYO</text>
        </svg>
        <div class="area-legend">
          <span class="dot main"></span>メインエリア
          <span class="dot sub"></span>対応エリア
        </div>
      </div>

      <div class="area-text">
        <div class="area-block">
          <div class="area-block-label">メインエリア(埼玉県)</div>
          <div class="area-list main">
            {links(main)}
          </div>
        </div>
        <div class="area-block">
          <div class="area-block-label">埼玉県の対応エリア</div>
          <div class="area-list">
            {links(sai_other)}
          </div>
        </div>
        <div class="area-block">
          <div class="area-block-label">東京都の対応エリア</div>
          <div class="area-list">
            {links(tokyo)}
          </div>
        </div>
      </div>
      <p class="area-note" style="margin-top:26px;">その他の東京23区・埼玉県内の地域もご相談ください。<a href="@@/area/" style="color:var(--gold);">対応エリア一覧を見る →</a></p>
    </div>
  </section>
'''


MESSAGE = '''
  <!-- 07.5 TOP MESSAGE -->
  <section class="section-pad message-section" id="message">
    <div class="wrap">
      <div class="message-head reveal">
        <span class="kicker">TOP MESSAGE</span>
        <h2>代表挨拶</h2>
      </div>
      <div class="message-wrap reveal">
        <p class="message-lead">綺麗と共に、福をお届けします。</p>
        <div class="message-body">
          <p>元プロキックボクサーとして培ってきた、最後まで逃げずにやり抜く姿勢と、どんな状況にも立ち向かう精神力。そして、日々の厳しいトレーニングで磨き上げた体力と忍耐力。</p>
          <p>引退後、新たな人生の道として出会ったのが「清掃」という仕事でした。</p>
          <p>クリニックや医院の清掃は、ただ床を磨くだけの仕事ではないと、私は考えています。患者さんが安心して待合室で過ごせること。スタッフの皆さまが気持ちよく診療に集中できること。その土台となる空間を整える仕事です。</p>
          <p>多院展開する美容クリニック様の全院をはじめ、医院様の清掃をお任せいただくなかで、診療を止めないこと、医療機器や院内のルールを尊重すること、そして毎回同じ品質で仕上げることの大切さを、現場で学んできました。</p>
          <p>留福美装は、床洗浄・ワックス・剥離洗浄から定期清掃、業務用エアコン洗浄まで、医院様の清掃を一つの窓口でお引き受けします。料金と作業内容を事前に明確にし、院長先生・事務長様が安心して任せられるパートナーであり続けます。</p>
          <p>一つひとつの現場に責任を持ち、見えない部分にも妥協せず、最後まで誠実に仕事をやり遂げる。清掃を通じて空間を整え、その先にある患者さんの安心と、医院様の信頼を届けてまいります。</p>
        </div>
        <p class="message-emphasis">綺麗の先に、福がある。</p>
        <div class="message-body">
          <p>この言葉を胸に、これからも技術と品質を磨き続け、地域の医療を支える医院様のお役に立てる存在を目指してまいります。</p>
          <p>今後とも、留福美装をよろしくお願い申し上げます。</p>
        </div>
        <p class="message-signoff">代表　神原瑠翔</p>

        <div class="message-photo-wrap">
          <div class="ph"><img src="@@/assets/img/representative-kambara.webp" alt="留福美装 代表 神原瑠翔" loading="lazy" decoding="async" width="900" height="999" style="width:100%;height:100%;object-fit:cover;display:block;"></div>
          <div class="message-name">
            <div class="m-role">代表</div>
            <div class="m-person">神原 瑠翔</div>
            <div class="m-brand">TOMEFUKU BISO</div>
          </div>
        </div>
      </div>
    </div>
  </section>
'''


def about_section():
    return f'''
  <!-- 08 ABOUT -->
  <section class="section-pad" id="about">
    <div class="wrap">
      <div class="company-info">
        <div class="ci-row">
          <div class="ci-label">屋号</div>
          <div class="ci-value">{C["name"]}</div>
        </div>
        <div class="ci-row">
          <div class="ci-label">登録番号</div>
          <div class="ci-value">{C["tax_id"]}</div>
        </div>
        <div class="ci-row">
          <div class="ci-label">所在地</div>
          <div class="ci-value">{C["address_full"]}</div>
        </div>
        <div class="ci-row">
          <div class="ci-label">TEL</div>
          <div class="ci-value">携帯　{C["tel_mobile"]}<br>固定　{C["tel_fixed"]}</div>
        </div>
        <div class="ci-row">
          <div class="ci-label">代表者</div>
          <div class="ci-value">{C["representative_spaced"]}</div>
        </div>
        <div class="ci-row">
          <div class="ci-label">業務内容</div>
          <div class="ci-value">
            <ul class="ci-list">
              <li>クリニック・医院・歯科医院の定期清掃</li>
              <li>床洗浄・ワックス・床剥離洗浄・カーペット洗浄</li>
              <li>ガラス清掃</li>
              <li>業務用エアコン洗浄・エアコンフィルター清掃(複数台・複数院対応)</li>
              <li>空室クリーニング・ハウスクリーニング・新築美装・原状回復工事など(<a href="{C["main_site"]}" target="_blank" rel="noopener" style="color:var(--gold);">留福美装 公式サイト</a>)</li>
            </ul>
          </div>
        </div>
        <div class="ci-row">
          <div class="ci-label">所属団体</div>
          <div class="ci-value">{C["association"]}</div>
        </div>
        <div class="ci-row">
          <div class="ci-label">加入保険</div>
          <div class="ci-value">{C["insurance"]}</div>
        </div>
      </div>
    </div>
  </section>
'''


def social_section():
    return f'''
  <!-- 09 INSTAGRAM / GOOGLE -->
  <section class="section-pad band">
    <div class="wrap">
      <div class="sec-head reveal">
        <span class="kicker">INSTAGRAM / GOOGLE</span>
        <h2>現場の様子・口コミ。</h2>
      </div>
      <div class="social-wrap">
        <div class="social-card">
          <div class="k">INSTAGRAM</div>
          <h3>施工の様子を投稿しています</h3>
          <p style="font-size:13.5px;color:var(--ink-soft);margin-bottom:16px;">日々の現場写真や作業風景を公開中です。</p>
          <a class="link" href="{C["instagram"]}" target="_blank" rel="noopener">@tomefuku.jp を見る →</a>
        </div>
        <div class="social-card">
          <div class="k">GOOGLE</div>
          <h3>Googleマップ・口コミ</h3>
          <p style="font-size:13.5px;color:var(--ink-soft);margin-bottom:16px;">お客様からいただいた評価をご確認いただけます。</p>
          <a class="link" href="{C["google_maps"]}" target="_blank" rel="noopener">Googleで見る →</a>
        </div>
      </div>
    </div>
  </section>
'''


def faq_section():
    return f'''
  <!-- 05.5 FAQ -->
  <section class="section-pad" id="faq">
    <div class="wrap">
      <div class="sec-head reveal">
        <span class="kicker">FAQ</span>
        <h2>よくあるご質問。</h2>
        <p class="desc">院長先生・事務長様・スタッフの皆さまからよくいただくご質問をまとめました。さらに詳しい内容は<a href="@@/column/" style="color:var(--gold);">コラム</a>でもご紹介しています。</p>
      </div>
{faq_details(TOP_FAQS)}
    </div>
  </section>
'''


HERO = '''
  <!-- 01 HERO -->
  <section class="hero">
    <div class="ph dark hero-photo">
      <img src="@@/assets/img/clinic-corridor-floor-polisher-cleaning.webp" alt="クリニック院内廊下の床をポリッシャーで洗浄する留福美装の作業風景" fetchpriority="high" decoding="async" style="width:100%;height:100%;object-fit:cover;object-position:50% 40%;display:block;">
    </div>
    <div class="hero-watermark" aria-hidden="true"><img src="@@/assets/img/logo-turtle-white.webp" alt=""></div>
    <div class="wrap hero-inner">
      <span class="hero-eyebrow wordmark">TOMEFUKU BISO</span>
      <h1><span style="display:inline-block;">クリニックの</span><br><span style="display:inline-block;">定期清掃・</span><span style="display:inline-block;">床清掃専門</span></h1>
      <p class="hero-sub"><strong class="hero-key">関東の複数院を、窓口ひとつで一括管理。</strong>東京・埼玉を中心に、待合室・診察室の床洗浄・ワックス、剥離洗浄から業務用エアコン洗浄まで。休診日・夜間に作業し、診療を止めずに院内を整えます。</p>
      <div class="hero-actions">
        <a class="btn" href="#solution">院ごとの清掃をまとめる</a>
        <a class="btn outline" href="#contact">無料見積もり</a>
      </div>
    </div>
    <div class="scroll-cue"><span>SCROLL</span><span class="line"></span></div>
  </section>
'''


SOLUTION = '''
  <!-- 01.5 SOLUTION(複数院の本部向け) -->
  <section class="section-pad band" id="solution">
    <div class="wrap">
      <div class="sec-head reveal">
        <span class="kicker">FOR HEAD OFFICE</span>
        <p class="sol-target">複数院を運営する医療法人・クリニック本部ご担当者様へ</p>
        <h2>院ごとにバラバラの清掃、<br><span class="sol-accent">窓口ひとつ</span>にまとめませんか？</h2>
        <p class="desc">院の数だけ増えていく「清掃の管理業務」を、留福美装がまとめてお引き受けします。</p>
      </div>

      <div class="sol-grid">
        <div class="sol-worries reveal">
          <h3 class="sol-h3">こんなお悩みありませんか？</h3>
          <ul class="sol-checks">
            <li>院ごとに<strong>清掃会社がバラバラ</strong></li>
            <li>院によって<strong>仕上がりに差</strong>がある</li>
            <li><strong>いつ清掃したか</strong>把握できない</li>
            <li>日程調整が<strong>各院の負担</strong>になっている</li>
          </ul>
        </div>
        <div class="sol-diagram reveal">
          <h3 class="sol-h3">本部の清掃管理が、ここまでシンプルに</h3>
          <div class="sol-compare">
            <div class="sol-box">
              <span class="sol-badge">いままで</span>
              <div class="sol-node hq">本部</div>
              <div class="sol-row vendors"><span>清掃会社A</span><span>清掃会社B</span><span>清掃会社C</span></div>
              <div class="sol-row clinics"><span>○○院</span><span>△△院</span><span>□□院</span></div>
              <p class="sol-cap">連絡・契約・日程調整が<br><strong class="neg">院の数だけ発生</strong></p>
            </div>
            <div class="sol-arrow" aria-hidden="true"></div>
            <div class="sol-box good">
              <span class="sol-badge">留福美装なら</span>
              <div class="sol-node hq">本部</div>
              <div class="sol-node one">留福美装(窓口ひとつ)</div>
              <div class="sol-row clinics"><span>○○院</span><span>△△院</span><span>□□院</span></div>
              <p class="sol-cap">ご連絡は<strong>1か所だけ</strong>。<br>全院を同じ基準で清掃</p>
            </div>
          </div>
        </div>
      </div>

      <h3 class="sol-h3 reveal" style="margin-top:56px;">留福美装が、本部の手間を引き受けます</h3>
      <div class="strength-grid">
        <div class="strength-item">
          <div class="mark"><span class="sol-num">1</span></div>
          <h3>窓口をひとつに</h3>
          <p>依頼・日程調整・問い合わせは、同じ担当が全院分まとめて対応。新規開院も電話一本で追加できます。</p>
        </div>
        <div class="strength-item">
          <div class="mark"><span class="sol-num">2</span></div>
          <h3>定期清掃を当社で管理</h3>
          <p>院ごとの実施時期を当社で管理し、時期が来たらご案内。やり忘れがなくなります。</p>
        </div>
        <div class="strength-item">
          <div class="mark"><span class="sol-num">3</span></div>
          <h3>写真付き作業報告書</h3>
          <p>毎回BEFORE/AFTER写真付きの報告書をお送りします。現地に行かずに全院の状態を確認できます。</p>
        </div>
        <div class="strength-item">
          <div class="mark"><span class="sol-num">4</span></div>
          <h3>診療を止めない</h3>
          <p>夜間・休日の作業に対応。患者さんのいない時間に、院内を養生してから作業します。</p>
        </div>
      </div>
      <div class="menu-cta"><a class="btn" href="#contact">まずは1院から相談する</a>　<a class="btn outline" href="#price">料金・サービスを見る</a></div>
    </div>
  </section>
'''


def build(write_page):
    from build import service_node
    body = (HERO + SOLUTION + price_section() + STRENGTH + works_section() + service_details() + MID_CTA + for_clinics()
            + area_section() + MESSAGE + about_section() + social_section() + faq_section() + contact_section())
    graph = [faq_jsonld([(q, a) for q, a in TOP_FAQS])]
    for p, n, d in SERVICES[:4]:
        graph.append(service_node(n, d, p, n))
    write_page(
        "",
        "クリニックの定期清掃・床清掃専門｜東京・埼玉・関東の複数院を一括管理｜留福美装",
        "クリニックの定期清掃・床清掃専門の留福美装。関東の複数院の清掃を窓口ひとつで一括管理し、写真付き報告書で全院の状態を確認できます。東京都・埼玉県の医院・歯科医院の床洗浄・ワックス、剥離洗浄、業務用エアコン洗浄に休診日・夜間対応。",
        body, graph=graph, is_top=True, changefreq="weekly", priority="1.0")
