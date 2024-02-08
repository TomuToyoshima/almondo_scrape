from selenium import webdriver
from selenium.webdriver.chrome.service import Service 

service = Service(executable_path="./chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.set_window_size('300', '300')
driver.get('https://almondotech.com/')