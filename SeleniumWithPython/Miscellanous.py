import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

#driver = webdriver.Firefox()
#driver = webdriver.Edge()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")
driver = webdriver.Chrome(options = chrome_options)

driver.implicitly_wait(2)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
#time.sleep(5)
driver.get_screenshot_as_file("screen.png")