from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches",["enable-automation"])

chrome_driver_path = "/Users/mymacbook/Desktop/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path, chrome_options=options)
# driver.get('https://google.com')
#driver = webdriver.Chrome(executable_path=chrome_driver_path)


driver.get(url="https://secure-retreat-92358.herokuapp.com")

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Jipara")
#name.send_keys(Keys.ENTER)

last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("")

#l_name.send_keys(Keys.ENTER)
#

email = driver.find_element(By.NAME, "email")
email.send_keys("test@gmail.com")

sign_in = driver.find_element(By.CSS_SELECTOR, ".form-signin button")
sign_in.send_keys(Keys.ENTER)
