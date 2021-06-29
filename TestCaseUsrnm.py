from keyboard import press
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys

driver: WebDriver = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe')

driver.get("https://oranum.com/en/home")
driver.find_element_by_css_selector("div.Ui-sc-ui0.zctkV.c1f9gxzh.c1tx18g4.ce6oks5.c1onkw2o").click()

driver.implicitly_wait(5)

driver.find_element_by_id("downshift-0-input").send_keys("Matt")
press("Enter")

driver.implicitly_wait(5)

driver.find_element_by_id("downshift-0-input").send_keys(Keys.CONTROL + "a")
driver.find_element_by_id("downshift-0-input").send_keys(Keys.DELETE)

driver.implicitly_wait(5)

driver.find_element_by_id("downshift-0-input").send_keys("MattWarren")

driver.implicitly_wait(5)

driver.find_element_by_id("downshift-0-input").send_keys(Keys.CONTROL + "a")
driver.find_element_by_id("downshift-0-input").send_keys(Keys.DELETE)

driver.find_element_by_id("downshift-0-input").send_keys("Faith")

driver.implicitly_wait(5)

driver.find_element_by_id("downshift-0-input").send_keys(Keys.CONTROL + "a")
driver.find_element_by_id("downshift-0-input").send_keys(Keys.DELETE)

driver.implicitly_wait(5)

driver.find_element_by_id("downshift-0-input").send_keys("Faith24")

driver.quit()