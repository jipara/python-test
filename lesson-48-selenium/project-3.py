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


driver.get(url="https://en.wikipedia.org/wiki/Main_Page")

# article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# print(article_count.text)
#
# link = driver.find_element(By.LINK_TEXT, "anyone can edit")
# print(link.click())


search_bottom = driver.find_element(By.NAME, "search")
search_bottom.send_keys("Python")
search_bottom.send_keys(Keys.ENTER)
