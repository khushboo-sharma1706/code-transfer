import time

from selenium import webdriver
from selenium.webdriver.common.by import By

#driver = webdriver.Firefox()
#driver = webdriver.Edge()
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes = driver.find_elements(By.XPATH, "//input[@type= 'checkbox']")

print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        break

radiobuttons = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
print(len(radiobuttons))
radiobuttons[2].click()
assert radiobuttons[2].is_selected()
