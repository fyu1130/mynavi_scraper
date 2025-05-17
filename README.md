懸念点
・CSS セレクタが違う
・検索条件を設定できていない
・ページネーション遷移できてるかチェック
・コード理解
・URLのパターンがわからないと厳しいぞ。
・詳細いらないからfetch_urlsいらないぞ。
応用
・詳細へ移動し具体的なものを収集（ページ遷移追加）

# mynavi_scraper

マイナビ転職サイトにログインし、求人情報を自動取得するスクレイピングツール。

---

## ✅ 概要

* SeleniumとBeautifulSoupを使ってマイナビ転職の求人をスクレイピング
* セッション情報はCookieベースで再利用
* GUIブラウザを使って手動ログイン後、以降は自動化
* GUI操作により各ページの最後のカードを別タブで表示
* 出力形式: CSVファイル

---

## ✅ 動作環境

* OS: Windows 10 / 11 
* Python: 3.10 以上
* Google Chrome: 任意の安定バージョン
* ChromeDriver: Chromeのバージョンと一致するもの

---

## ✅ セットアップ手順

1. 仮想環境の作成と有効化

```powershell
python -m venv venv
venv\Scripts\activate
```

#### ▶ 仮想環境の有効化方法

| 使用環境           | 必要な手順                                                                                       |
| -------------- | ------------------------------------------------------------------------------------------- |
| PowerShell     | `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` の後 `venv\Scripts\Activate.ps1` |
| CMD / Git Bash | `venv\Scripts\activate.bat` だけでOK                                                           |
| 管理者権限          | ❓ 不要 (ユーザー権限で十分)                                                                            |

2. 必要パッケージのインストール

```bash
pip install -r requirements.txt
```

3. ChromeDriver の準備

* [https://googlechromelabs.github.io/chrome-for-testing/](https://googlechromelabs.github.io/chrome-for-testing/) からバージョン一致のものをDL
* `chromedriver.exe` をプロジェクトルートに置く
* chromeのバージョン確認
```google chorme
chrome://settings/help
//バージョンを確認：136.0.7103.114（Official Build） （64 ビット）
```
* [https://googlechromelabs.github.io/chrome-for-testing/](https://googlechromelabs.github.io/chrome-for-testing/) でChrome バージョンに一致する「Stable」列からダウンロード（ Windows の chromedriver-win64.zip ）
* `chromedriver.exe` をプロジェクトルートに置く

4. 動作確認

```bash
python test_gui_browser.py
```

5. 初回ログインと Cookie 保存

```bash
python manual_login.py
```

6. 本番実行

```bash
python main.py
```

---

## ✅ 注意

* マイナビ転職の利用規約に違反しないように利用してください
* `robots.txt` などを確認の上、リクエスト頻度には配慮を

---

## ✅ ディレクトリ構成

```
mynavi_scraper/
├── main.py              # メイン実行スクリプト
├── manual_login.py      # 手動ログイン
├── login.py             # Cookie保存 / 再利用
├── scrape_job.py        # 求人詳細のスクレイピング
├── open_last_job_in_tab.py          # GUIを操作し別タブを開く（コメントアウト済み）
├── save_csv.py          # CSV保存処理
├── test_gui_browser.py  # テスト用
├── requirements.txt
├── .env                 # 認証情報を格納
├── .env.example
├── .gitignore           # github用
├── README.md
├── output/
│   └── results.csv         # 出力CSV
└── cookies/
    └── mynavi_cookies.pkl
```

---

## 改善点

* [ ] driver.switch_to.window() で開いたタブに遷移してスクレイピング処理を続ける

```python
# 新しいタブへ切り替え
tabs = driver.window_handles
driver.switch_to.window(tabs[-1])
print("✅ 新しいタブに切り替えました")

# URLなどを確認
print("🔍 現在のURL:", driver.current_url)
```

---

## 試行錯誤

* wsl上で試みたがGUIの操作が連携しずらいため、windows OSへ

