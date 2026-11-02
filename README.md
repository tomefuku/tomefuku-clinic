# tomefuku-clinic(留福美装 クリニック清掃専門サイト)

tomefuku.jp と同じデザイン・アニメーション・構成で、内容をクリニック・医院・歯科医院の清掃専門にしたサイトです。
既存の留福美装サイト(tomefuku-website)とは完全に別のプロジェクトです。

## ページ構成(全49ページ)

| URL | 内容 |
|---|---|
| `/` | トップ(tomefuku.jp と同じ構成・同じ順番) |
| `/floor-wax/` | クリニック床洗浄・ワックス(待合室・診察室の床清掃 `#waiting`) |
| `/hakuri/` | 床剥離洗浄 |
| `/teiki/` | クリニック定期清掃(月額プラン・カーペット `#carpet`・ガラス `#glass`) |
| `/aircon/` | 業務用エアコン洗浄・フィルター清掃(`#filter`) |
| `/price/` | 料金 |
| `/contact/` | お問い合わせ(フォーム) |
| `/specialty/` + 10ページ | 診療科目別(歯科・眼科・内科・皮膚科・整形外科・美容・小児科・耳鼻咽喉科・婦人科・心療内科) |
| `/area/` + 23ページ | 対応エリア(埼玉13市・東京10区) |
| `/column/` + 6記事 | コラム |
| `404.html` | ページが見つからないとき |

## GitHubへの公開手順

1. GitHubで新しいリポジトリ `tomefuku-clinic` を作成
2. このフォルダの中身をすべてアップロード(`_build` フォルダも含めてOK。サイト上には公開されません)
3. Settings → Pages → Branch: `main` / `(root)` → Save
4. 独自ドメインが決まったら、Settings → Pages → Custom domain に入力
5. **`_build/config.py` の `SITE_URL` を新ドメインに書き換えて再ビルド**(下記)

※ CNAME は入れていません(tomefuku.jp のドメインと競合させないため)。

## 書き換え・再ビルドの方法

ページは `_build/` のスクリプトから自動生成しています。内容を変えたら、リポジトリのルートで

```
python3 _build/build.py
```

を実行すると全ページ・sitemap.xml・robots.txt が作り直されます。

| 変えたいもの | 書き換える場所 |
|---|---|
| 独自ドメイン(canonical・OGP・構造化データ・sitemap) | `_build/config.py` の `SITE_URL` |
| 料金(未確定の項目は `None` →「お見積もり」と表示) | `_build/config.py` の `PRICES` |
| 会社情報・電話番号 | `_build/config.py` の `COMPANY` |
| トップページの文章・FAQ・代表挨拶 | `_build/pages_top.py` |
| サービス・料金ページの文章 | `_build/pages_service.py` |
| 診療科目ページ | `_build/content_specialty.py` |
| 地域ページ(追加も1件足すだけ) | `_build/content_areas.py` |
| コラム(追加も1件足すだけ) | `_build/pages_column.py` の `COLUMNS` |
| 施工事例 | `_build/content_common.py` の `WORKS` |
| デザイン(tomefuku.jp と共通の部分は変更なし) | `assets/css/style.css` |

## 写真の差し替え

写真は `assets/img/` にあります(WebP形式・内容が分かる英語のファイル名)。
同じファイル名で上書きすればそのまま差し替わります。新しい写真を足す場合は WebP(横1000〜1600px程度)にして、
`content_common.py` の施工事例などにファイル名と説明(alt)を追加してください。

## お問い合わせフォーム

tomefuku.jp と同じ Googleフォームに送信します(通知メールの届け先も同じ)。
既存フォームの5項目に合わせて、次のように送っています。

- お名前 ← ご担当者名
- メールアドレス・電話番号 ← そのまま
- ご住所 ← 所在地
- お問い合わせ内容 ← 先頭に【クリニック清掃サイトからのお問い合わせ】と入れ、医院・施設名/希望する清掃内容/希望頻度/本文/送信ページをまとめて記載

送信処理は `assets/js/main.js` の下部にあります。

## 公開後にやること(Google Search Console)

1. Search Console で新ドメインをプロパティ追加(DNSのTXTレコードで所有権確認)
2. 「サイトマップ」に `sitemap.xml` を送信
3. 「URL検査」でトップ・主要ページのインデックス登録をリクエスト
4. Googleビジネスプロフィールのウェブサイト欄・Instagramのリンクなどから新サイトへリンク
