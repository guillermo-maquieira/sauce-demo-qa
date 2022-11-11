from selenium import webdriver

username = "standard_user"
password = "secret_sauce"

driver = webdriver.Chrome("chromedriver")

driver.get("https://www.saucedemo.com/")
driver.find_element("id", "user-name").send_keys(username)
driver.find_element("id", "password").send_keys(password)
driver.find_element("name", "login-button").click()

driver.find_element("id", "add-to-cart-sauce-labs-backpack").click()
driver.find_element("id", "add-to-cart-sauce-labs-bike-light").click()
driver.find_element("id", "add-to-cart-sauce-labs-bolt-t-shirt").click()

