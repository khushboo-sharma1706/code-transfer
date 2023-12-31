import time

from selenium import webdriver
from selenium.webdriver.common.by import By

#driver = webdriver.Firefox()
#driver = webdriver.Edge()
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(1)
results = driver.find_elements(By.XPATH, "//div[@class = 'products']/div")
count = len(results)
assert count > 0
print(count)
for result in results:
    result.find_element(By.XPATH, "div/button").click()
    time.sleep(1)

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div/div/header/div/div[3]/div[2]/div[2]/button").click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
#time.sleep(1)
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)

