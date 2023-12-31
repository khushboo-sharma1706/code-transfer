import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#driver = webdriver.Firefox()
#driver = webdriver.Edge()
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")

time.sleep(5)

# ID, xpath, cssselector, name, classname, linktext

driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()
#Static dropdown

dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_index(1)
time.sleep(10)

#xpath - //tagname[@attribute= 'value'] -> //input[@type = 'submit']
#css -   tagname[attribute= 'value'] #Id
driver.find_element(By.CSS_SELECTOR, "input[type = 'submit']").send_keys("Khushboo")
driver.find_element(By.XPATH, "//input[@type = 'submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert "Success" in message

driver.find_element(By.XPATH, "/html/body/app-root/form-comp/div/h4/input").send_keys("helloagain")
time.sleep(10)
driver.find_element(By.XPATH, "/html/body/app-root/form-comp/div/h4/input").clear()