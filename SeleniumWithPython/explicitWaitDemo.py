import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

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

#Sum validation

prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
sum = 0
for price in prices:
    sum += int(price.text)
print(sum)
totalAmount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)

assert sum == totalAmount

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
#time.sleep(1)
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)

