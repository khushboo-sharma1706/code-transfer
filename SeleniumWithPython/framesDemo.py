import time

from selenium import webdriver
from selenium.webdriver.common.by import By

#driver = webdriver.Firefox()
#driver = webdriver.Edge()
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.switch_to.frame("")