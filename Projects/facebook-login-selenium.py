from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

user_name = "anything@email.com" #username/mail
password = "password" #password
driver = webdriver.Chrome(executable_path='C:\\Users\\dir name\\Downloads\\chromedriver_win32\\chromedriver.exe') #path of the chromedriver
driver.get("https://www.facebook.com")
results = [] #array to store results
element =  driver.find_element_by_id("email")
element.send_keys(user_name)
element = driver.find_element_by_id("pass")
element.send_keys(password)
element.send_keys(Keys.RETURN)
content = driver.page_source
soup = BeautifulSoup(content)
# driver.close()

for elements in soup.findAll(attrs='_9ay7'):
    msg = elements.find('a')
    if msg not in results:
        results.append(msg.text)
print(results)
