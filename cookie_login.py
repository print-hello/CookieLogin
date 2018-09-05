import os,time
from selenium import webdriver
import requests
import json

chromedriver = "D:\chromedriver.exe"
os.environ["webdriver.Chrome.driver"] = chromedriver 
driver = webdriver.Chrome(chromedriver)
url = 'url address' 

def get_cookies():
    driver.get(url)
    time.sleep(5)

    elem_user=driver.find_element_by_id('email') 
    elem_user.clear()
    elem_user.send_keys('user')  
    
    elem_pass=driver.find_element_by_id('password') 
    elem_pass.clear() 
    elem_pass.send_keys('password') 
    
    elem_login=driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/div/div[4]/div[1]/form/div/button/div')
    elem_login.click() 

    time.sleep(5)

    cookies = driver.get_cookies()
    with open("cookies.txt", "w") as fp:
        json.dump(cookies, fp)

# cookie登陆
def read_cookies():
    driver.get(url)
    cookies = json.loads(r'cookie list') # 如果手动传入cookie需要进行转义
        for cookie in cookies:
        # cookie.pop('domain')  # 如果报domain无效的错误
        driver.add_cookie(cookie)

    driver.get(url)

    with open("cookies.txt", "r") as fp:
        cookies = json.load(fp)
        for cookie in cookies:
            # cookie.pop('domain')  # 如果报domain无效的错误
            driver.add_cookie(cookie)
        driver.get(url)

if __name__ == '__main__':
    get_cookies()
    read_cookies()