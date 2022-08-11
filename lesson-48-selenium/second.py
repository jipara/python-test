from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches",["enable-automation"])

chrome_driver_path = "/Users/mymacbook/Desktop/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path, chrome_options=options)
# driver.get('https://google.com')
#driver = webdriver.Chrome(executable_path=chrome_driver_path)


driver.get(url="https://www.python.org/")
# xpath = '//*[@id="content"]/div/section/div[2]/div[2]/div/ul'
# driver2 = driver.find_element(By.XPATH, xpath)
# print(driver2.tag_name)
#
# html_list = driver.find_element(By.CLASS_NAME, "menu")
# tag_name = html_list.find_elements(By.TAG_NAME, "li")
# for item in tag_name:
#     text = item.text
#     print(text)


# event_times = driver.find_element(By.CSS_SELECTOR, ".event-widget time")
# list = third_option.find_elements(By.CSS_SELECTOR, "li")
# print(list)
# for item in list:
#     text = item.text
#     print(text.title())
list_key = []
event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
for time in event_times:
    #time_of_events = {}
    list_key.append(time.text)
#print(list_key)

event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")


list_value = []
for event in event_names:
    list_value.append(event.text)

#print(len(list_value))



schedule = {list_key[i]: list_value[i] for i in range(len(list_value))}
print(schedule)


####2 option

event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
events = {}


for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text
    }

print(events)
