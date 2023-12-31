import time

from selenium import webdriver

#driver = webdriver.Firefox()
#driver = webdriver.Edge()
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.python.org/")
time.sleep(10)
assert "Python" in driver.title
print(driver.title)
print(driver.current_url)
driver.get("https://docs.python.org/3/")
#driver.minimize_window()
time.sleep(10)
driver.refresh()
driver.back()
driver.forward()

