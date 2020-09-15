from selenium import webdriver

with open('shiet.js', 'r') as f:
    shiet = f.read()

url_home = 'https://www.worldometers.info/'
option = webdriver.ChromeOptions()
option.add_argument('headless')
driver = webdriver.Chrome(options=option)
driver.get(url_home)
data = driver.execute_script(shiet)

