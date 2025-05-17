from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login import login_with_cookies
from scrape_job import scrape_job_listings_from_page
from save_csv import save_to_csv
import tempfile
import time


def main():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    # options.add_argument("--headless")
    options.add_argument("--disable-dev-shm-usage")
    profile_dir = tempfile.mkdtemp()
    options.add_argument(f"--user-data-dir={profile_dir}")
    service = Service("./chromedriver.exe")

    driver = webdriver.Chrome(service=service, options=options)

    try:
        login_with_cookies(driver)

        # キーワード検索＆スクレイピング
        keyword = "エンジニア"
        max_pages = 1
        data = scrape_job_listings_from_page(driver, keyword=keyword, max_pages=max_pages)
        
        # データをCSVに保存
        save_to_csv(data)

    finally:
        # driver.quit()
        pass

if __name__ == '__main__':
    main()
