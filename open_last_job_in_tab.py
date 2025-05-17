from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def open_last_job_link_in_new_tab(driver):
    try:
        # 最後の a.js__ga--setCookieOccName 要素を探す
        links = driver.find_elements(By.CSS_SELECTOR, 'a.js__ga--setCookieOccName')
        if links:
            last_link = links[-1]
            href = last_link.get_attribute("href")
            if href:
                driver.execute_script(f"window.open('{href}', '_blank');")
                print(f"✅ 新しいタブで開きました: {href}")
            else:
                print("⚠️ href属性が取得できませんでした")
        else:
            print("⚠️ a.js__ga--setCookieOccName が見つかりませんでした")
        # seleniumよりもjsを用いた方が確実なので以下のコードはコメントアウト
        # if links:
        #     last_link = links[-1]
        #     ActionChains(driver) \
        #         .key_down(Keys.CONTROL) \
        #         .click(last_link) \
        #         .key_up(Keys.CONTROL) \
        #         .perform()
        #     print("✅ 最後の求人リンクを新しいタブで開きました")
        # else:
        #     print("⚠️ 求人リンクが見つかりませんでした")
    except Exception as e:
        print(f"❌ 最後のリンクを開く際にエラー: {e}")
