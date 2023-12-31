import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

#driver = webdriver.Firefox()
#driver = webdriver.Edge()
driver = webdriver.Chrome()
driver.maximize_window()

browserSortedVeggieList = []
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
time.sleep(1)
# click on column header
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
# collect all veggies name -> browsersortedveggielist[A, B, C]
veggieWebElements = driver.find_elements(By.XPATH, "//tr/td[1]")
for ele in veggieWebElements:
    browserSortedVeggieList.append(ele.text)
originalbrowserSortedVeggieList = browserSortedVeggieList.copy()

# sort this browsersortedveggielist -> newSortedList[A, B, C]
browserSortedVeggieList.sort()

# browsersortedveggielist == newSortedList
assert browserSortedVeggieList == originalbrowserSortedVeggieList