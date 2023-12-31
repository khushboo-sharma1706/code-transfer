import time

from selenium import webdriver
from selenium.webdriver.common.by import By

#driver = webdriver.Firefox()
#driver = webdriver.Edge()
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://sso.teachable.com/secure/9521/identity/login/password")
driver.find_element(By.LINK_TEXT, "Forgot Password").click()
time.sleep(5)
driver.find_element(By.XPATH, "//*[@id='email']").send_keys("skhushboo1706@gmail.com")
driver.find_element(By.XPATH, "/html/body/main/div/form/div[2]/input").click()
time.sleep(10)
