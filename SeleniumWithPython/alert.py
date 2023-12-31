import time

from selenium import webdriver
from selenium.webdriver.common.by import By
name = "Khushboo"
#driver = webdriver.Firefox()
#driver = webdriver.Edge()
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert
alertText = alert.text
print(alertText)
assert name in alertText
time.sleep(5)
alert.accept()
time.sleep(5)
#alert.dismiss()