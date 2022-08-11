from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "/Users/mymacbook/Desktop/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(url="https://www.python.org/")
# price = driver.find_element_by_id("a-offscreen")
# print(price)
# search_bar = driver.find_element(by="name", value="q")
# print(search_bar.tag_name)


# class_name = driver.find_element_by_class_name(".container")
# print(class_name)

[<selenium.webdriver.remote.webelement.WebElement (session="1f970e3075f8fb809b68ae6cdd2916c2", element="86574949-829a-4015-b085-c1ea81ccf28d")>, <selenium.webdriver.remote.webelement.WebElement (session="1f970e3075f8fb809b68ae6cdd2916c2", element="77a9870c-f2ad-4efc-a32e-c66507fc3d54")>, <selenium.webdriver.remote.webelement.WebElement (session="1f970e3075f8fb809b68ae6cdd2916c2", element="7ecb3855-c0c9-4aa3-abf6-6e0bbafaebac")>]


element = driver.find_elements(By.CSS_SELECTOR, "documentation-widget a")
print(element)

element = driver.find_element(By.XPATH, "element_xpath")

#driver.close()
driver.quit()
