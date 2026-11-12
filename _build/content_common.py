# -*- coding: utf-8 -*-
"""複数ページで使う共通データ(施工事例カード・診療科目一覧・サービス一覧)"""
from parts import ba_card, stack_card, single_card

BADGE_MULTI = "関東で多院展開する美容クリニック様の全院を担当"

# ---------------------------------------------------------------------------
# 施工事例(すべて tomefuku.jp に掲載中の実際の事例。写真は後から差し替え可能)
# data_cat はタブ名と一致させる(複数ある場合は半角スペース区切り)
# ---------------------------------------------------------------------------
WORKS = {
    "beauty_floor": ba_card(
        "床洗浄", "床洗浄",
        "beauty-clinic-corridor-floor-before", "beauty-clinic-corridor-floor-after",
        "クリニック 床洗浄 施工前 美容クリニック様 院内廊下の床", "クリニック 床洗浄 施工後 美容クリニック様 院内廊下の床",
        "某美容クリニック様 大宮院(さいたま市大宮区)｜院内廊下の床洗浄", badge=BADGE_MULTI,
        desc="院内廊下フロアの床洗浄を実施。診療時間を避けた夜間の作業で、複数院まとめてのご依頼に対応しています。",
        link=("@@/floor-wax/", "床洗浄・ワックスの詳細を見る →")),
    "kawaguchi_floor": ba_card(
        "待合室の床清掃", "床洗浄",
        "kawaguchi-neurosurgery-waiting-room-floor-before", "kawaguchi-neurosurgery-waiting-room-floor-after",
        "クリニック 待合室 床清掃 施工前 埼玉県川口市 某脳神経外科様", "クリニック 待合室 床清掃 施工後 埼玉県川口市 某脳神経外科様",
        "某脳神経外科様(埼玉県川口市)｜待合室の床清掃",
        desc="受付前・待合室の床をポリッシャーで洗浄しました。",
        link=("@@/area/kawaguchi/", "川口市のクリニック清掃について →")),
    "beauty_carpet": stack_card(
        "カーペット洗浄", "カーペット",
        [("beauty-clinic-carpet-cleaning-01", "クリニック カーペット洗浄 業務用クリーナーでの洗浄作業(美容クリニック様)"),
         ("beauty-clinic-carpet-cleaning-02", "クリニック カーペット洗浄 洗浄機での仕上げ作業(美容クリニック様)")],
        "某美容クリニック様 大宮院(さいたま市大宮区)｜カーペット洗浄", badge=BADGE_MULTI,
        desc="院内カーペットの洗浄を実施。床洗浄とあわせた定期清掃としてご依頼いただいています。",
        link=("@@/teiki/", "クリニック定期清掃の詳細を見る →")),
    "beauty_aircon": stack_card(
        "業務用エアコン洗浄", "エアコン",
        [("beauty-clinic-aircon-cleaning-01", "クリニック 業務用エアコン洗浄 天井埋込型エアコンの分解洗浄(美容クリニック様)"),
         ("beauty-clinic-aircon-cleaning-02", "クリニック 業務用エアコン洗浄 高圧洗浄の様子(美容クリニック様)")],
        "某美容クリニック様 大宮院(さいたま市大宮区)｜業務用エアコン洗浄", badge=BADGE_MULTI,
        desc="診療時間を避けた夜間対応で、院内の動線を妨げずに施工しました。",
        link=("@@/aircon/", "業務用エアコン洗浄の詳細・料金を見る →")),
    "office_drain": ba_card(
        "業務用エアコン洗浄", "エアコン",
        "office-aircon-drain-pan-before", "office-aircon-drain-pan-after",
        "クリニック 業務用エアコン洗浄 ドレンパン 施工前(眼科様)", "クリニック 業務用エアコン洗浄 ドレンパン 施工後(眼科様)",
        "某眼科様(さいたま市浦和区)｜業務用エアコン洗浄(ドレンパン)"),
    "office_hex": ba_card(
        "業務用エアコン洗浄", "エアコン",
        "office-aircon-heat-exchanger-before", "office-aircon-heat-exchanger-after",
        "クリニック 業務用エアコン洗浄 熱交換器 施工前(眼科様)", "クリニック 業務用エアコン洗浄 熱交換器 施工後(眼科様)",
        "某眼科様(さいたま市浦和区)｜業務用エアコン洗浄(熱交換器)"),
    "kawaguchi_floor2": ba_card(
        "待合室の床清掃", "床洗浄",
        "kawaguchi-neurosurgery-waiting-room-floor-02-before", "kawaguchi-neurosurgery-waiting-room-floor-02-after",
        "クリニック 待合室 床洗浄 施工前 ポリッシャー作業中 埼玉県川口市 某脳神経外科様", "クリニック 待合室 床洗浄 施工後 埼玉県川口市 某脳神経外科様",
        "某脳神経外科様(埼玉県川口市)｜待合室の床洗浄",
        desc="待合ベンチ前の通路にたまった黒ずみを、ポリッシャーで洗浄しました。",
        link=("@@/floor-wax/#waiting", "待合室・診察室の床清掃について →")),
    "azabu_drain": ba_card(
        "業務用エアコン洗浄", "エアコン",
        "azabujuban-beauty-clinic-aircon-drain-pan-before", "azabujuban-beauty-clinic-aircon-drain-pan-after",
        "クリニック 業務用エアコン洗浄 ドレンパンのカビ 施工前 東京都港区麻布十番 美容クリニック様", "クリニック 業務用エアコン洗浄 ドレンパン 施工後 東京都港区麻布十番 美容クリニック様",
        "某美容クリニック様(東京都港区麻布十番)｜業務用エアコン洗浄(ドレンパン)",
        desc="カビが広がっていたドレンパンを分解して洗浄しました。",
        link=("@@/aircon/", "業務用エアコン洗浄の詳細・料金を見る →")),
    "azabu_work": single_card(
        "業務用エアコン洗浄", "エアコン",
        "azabujuban-beauty-clinic-aircon-cleaning-work", "クリニック 業務用エアコン洗浄 天井埋込型エアコンの分解作業 東京都港区麻布十番 美容クリニック様",
        "某美容クリニック様(東京都港区麻布十番)｜業務用エアコン洗浄 作業風景",
        desc="院内を養生したうえで、天井埋込型エアコンを分解して洗浄しました。"),
    "mito_hex": single_card(
        "業務用エアコン洗浄", "エアコン",
        "mito-beauty-clinic-aircon-heat-exchanger-before-after", "クリニック 業務用エアコン洗浄 熱交換器 左が洗浄前・右が洗浄後 茨城県水戸市 美容クリニック様",
        "某美容クリニック様 水戸院(茨城県水戸市)｜熱交換器の洗浄",
        desc="写真左が洗浄前、右が洗浄後です。熱交換器に詰まった汚れを高圧洗浄で落としました。",
        link=("@@/aircon/", "業務用エアコン洗浄の詳細・料金を見る →")),
    "mito_drain": ba_card(
        "業務用エアコン洗浄", "エアコン",
        "mito-beauty-clinic-aircon-drain-pan-before", "mito-beauty-clinic-aircon-drain-pan-after",
        "クリニック 業務用エアコン洗浄 ドレンパン・送風ファン 施工前 茨城県水戸市 美容クリニック様", "クリニック 業務用エアコン洗浄 ドレンパン・送風ファン 施工後 茨城県水戸市 美容クリニック様",
        "某美容クリニック様 水戸院(茨城県水戸市)｜ドレンパンの洗浄",
        desc="カビや水あかがたまっていたドレンパンと送風ファンを、取り外して洗浄しました。"),
    "mito_carpet": stack_card(
        "カーペット洗浄", "カーペット",
        [("mito-beauty-clinic-carpet-cleaning-polisher", "クリニック カーペット洗浄 院内廊下のポリッシャー洗浄 茨城県水戸市 美容クリニック様"),
         ("mito-beauty-clinic-carpet-cleaning-extractor", "クリニック カーペット洗浄 リンサーで汚れを吸い取る作業 茨城県水戸市 美容クリニック様")],
        "某美容クリニック様 水戸院(茨城県水戸市)｜カーペット洗浄",
        desc="院内廊下のカーペットを洗浄し、汚れを含んだ水をリンサーで吸い取って仕上げました。",
        link=("@@/teiki/#carpet", "カーペット洗浄について →")),
    "mito_1way": single_card(
        "業務用エアコン洗浄", "エアコン",
        "mito-beauty-clinic-aircon-1way-cleaning-work", "クリニック 天井埋込1方向カセット型エアコンの分解洗浄作業 茨城県水戸市 美容クリニック様",
        "某美容クリニック様 水戸院(茨城県水戸市)｜1方向エアコン洗浄 作業風景",
        desc="廊下の天井に設置された1方向カセット型エアコンを分解して洗浄しました。"),
}

WORKS_ORDER = ["mito_hex", "mito_drain", "beauty_floor", "kawaguchi_floor2", "mito_carpet", "kawaguchi_floor", "beauty_carpet", "azabu_drain", "azabu_work", "mito_1way", "beauty_aircon", "office_drain", "office_hex"]
WORKS_TABS = ["すべて", "床洗浄", "カーペット", "エアコン"]

# ---------------------------------------------------------------------------
# サービス(下層ページ)
# ---------------------------------------------------------------------------
SERVICES = [
    ("floor-wax/", "クリニック床洗浄・ワックス", "待合室・診察室・廊下の床を洗浄し、ワックスで保護します。"),
    ("hakuri/", "床剥離洗浄", "古いワックスと黒ずみを剥がし、床を一度リセットします。"),
    ("teiki/", "クリニック定期清掃", "床・カーペット・ガラス・エアコンフィルターを決まった頻度で。"),
    ("aircon/", "業務用エアコン洗浄・フィルター清掃", "天井埋込型・天吊り型の分解洗浄。夜間対応も可能です。"),
    ("price/", "料金", "床洗浄1㎡800円〜・カーペット洗浄1㎡1,100円〜、週1回からの定期清掃プラン。"),
]

# ---------------------------------------------------------------------------
# 診療科目(slug, 表示名, 短い名前)
# ---------------------------------------------------------------------------
SPECIALTY_LIST = [
    ("dental", "歯科医院・歯医者", "歯科医院"),
    ("ophthalmology", "眼科", "眼科"),
    ("internal-medicine", "内科", "内科クリニック"),
    ("dermatology", "皮膚科", "皮膚科"),
    ("orthopedics", "整形外科", "整形外科"),
    ("beauty-clinic", "美容クリニック", "美容クリニック"),
    ("pediatrics", "小児科", "小児科"),
    ("ent", "耳鼻咽喉科", "耳鼻咽喉科"),
    ("gynecology", "婦人科", "婦人科"),
    ("psychiatry", "精神科・心療内科", "心療内科・精神科"),
]
