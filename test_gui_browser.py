from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def main():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service("./chromedriver.exe"), options=options)
    driver.get("https://www.google.com")
    input("\n\u30D6\u30E9\u30A6\u30B6\u304C\u958B\u3051\u305F\u3089Enter: ")
    driver.quit()

if __name__ == '__main__':
    main()