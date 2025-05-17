from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from login import manual_login_and_save
import tempfile
import shutil

def main():
    options = webdriver.ChromeOptions()
    options.add_argument(f"--user-data-dir={tempfile.mkdtemp()}")
    driver = webdriver.Chrome(service=Service("./chromedriver.exe"), options=options)
    try:
        manual_login_and_save(driver)
    finally:
        driver.quit()

if __name__ == '__main__':
    main()
