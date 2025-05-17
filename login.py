import time
import os
import pickle
from selenium.webdriver.common.by import By

COOKIE_PATH = "cookies/mynavi_cookies.pkl"

def manual_login_and_save(driver):
    driver.get("https://tenshoku.mynavi.jp/login/")
    input("\n\u30ED\u30B0\u30A4\u30F3\u304C\u7D42\u308F\u3063\u305F\u3089Enter: ")
    os.makedirs("cookies", exist_ok=True)
    with open(COOKIE_PATH, "wb") as f:
        pickle.dump(driver.get_cookies(), f)
    print("[INFO] Cookie saved.")

def login_with_cookies(driver):
    driver.get("https://tenshoku.mynavi.jp/login/")
    time.sleep(2)
    if os.path.exists(COOKIE_PATH):
        with open(COOKIE_PATH, "rb") as f:
            cookies = pickle.load(f)
        for cookie in cookies:
            driver.add_cookie(cookie)
        driver.get("https://tenshoku.mynavi.jp/search/")  # ログイン後ページ
        time.sleep(3)
    else:
        print("[WARN] Cookieが見つかりません。manual_login.py を実行してください。")
