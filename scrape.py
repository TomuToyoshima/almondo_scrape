from selenium import webdriver
# import chromedriver_binary
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome("C:\Users\dream\Downloads\chromedriver-win64\chromedriver.exe")

# オプションの設定
options = webdriver.ChromeOptions()

# Selenium実行後もChromeを開いたままにする
options.add_experimental_option('detach', True)

# Chromeブラウザを開く
driver = webdriver.Chrome(
    options=options
)

# 現在のタブでページを開く
driver.get("https://www.env.go.jp/")
sleep(3)
