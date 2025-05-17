from bs4 import BeautifulSoup
from open_last_job_in_tab import open_last_job_link_in_new_tab
import csv
import time
from selenium.webdriver.common.by import By

def scrape_job_listings_from_page(driver, keyword, max_pages=1):
    results = []
    for page in range(1, max_pages + 1):
        if page == 1:
            url = f"https://tenshoku.mynavi.jp/list/kw{keyword}/?jobsearchType=4&searchType=8"
        else:
            url = f"https://tenshoku.mynavi.jp/list/kw{keyword}/pg{page}/?jobsearchType=4&searchType=8"

        driver.get(url)
        time.sleep(2)
        # GUI操作用（open_last_job_in_tab）
        # open_last_job_link_in_new_tab(driver)
        # time.sleep(20)

        soup = BeautifulSoup(driver.page_source, "html.parser")
        cards = soup.select("div.cassetteRecruit__content")

        for card in cards:
            company = card.select_one("h3.cassetteRecruit__name")
            employment_type = card.select_one("span.labelEmploymentStatus")
            tags = card.select("li.cassetteRecruit__attributeLabel span.labelCondition")
            salary_elems = card.select("td.tableCondition__body")
            salary = salary_elems[-1].get_text(strip=True) if salary_elems else ""

            results.append([
                company.get_text(strip=True) if company else "",
                employment_type.get_text(strip=True) if employment_type else "",
                ", ".join([tag.get_text(strip=True) for tag in tags]),
                salary
            ])

        print(f"✅ {page}ページ目を処理しました（{len(cards)}件）")

    return results
