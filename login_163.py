from selenium import webdriver
# import os 
import time
import requests
import json

# 如果没有设置chromedriver环境变量用此方式
# chromedriver = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe"
# os.environ["webdriver.Chrome.driver"] = chromedriver 
driver = webdriver.Chrome()
login_url = 'https://mail.163.com/'
driver.get(login_url)
time.sleep(5)

def click_login(user, password):
    try:
        login_state=cookie_login()
    except Exception as e:
        # print(e)
        print('cookie已失效,正在尝试点击登陆...')
        # 没有将定位不到元素
        driver.switch_to.frame('x-URS-iframe')

        elem_user = driver.find_element_by_name('email')
        elem_user.clear()
        elem_user.send_keys(user)

        elem_password = driver.find_element_by_name('password')
        elem_password.clear()
        elem_password.send_keys(password)

        elem_login = driver.find_element_by_id('dologin')
        elem_login.click()

        time.sleep(5)

        cookies = driver.get_cookies()

        # 文件存储
        with open('cookies.txt', 'w') as fp:
            json.dump(cookies, fp)
        
        # 数据库存储
        # cookies = json.dumps(cookies)
        # cookies = cookies.replace('\\', '\\\\')
        # cookies = cookies.replace('\"', '\\"')
        # sql = "update account set cookie=\"" +cookies+"\" where id="+str(***)
        # #print(sql)
        # cur = conn.cursor()
        # cur.execute(sql)
        # conn.commit()
        # cur.close()


# cookies登陆
def cookie_login():
    driver.get(login_url)
    print('正在使用cookie登陆...')
    time.sleep(5)

    # 清除cookies
    driver.delete_all_cookies()
    #print(cookie)

    # 数据库读取
    # cookies = json.loads(cookie)
    # for coo in cookies:
    #     coo.pop('domain')  # 如果报domain无效的错误
    #     driver.add_cookie(coo)

    # 文件读取
    with open('cookies.txt', 'r') as fp:
        cookies = json.load(fp)
        for cookie in cookies:
            driver.add_cookie(cookie)

        driver.get(login_url)
        driver.refresh()

    # 登陆成功判断条件
    # login_state = cookie_login()
    # login_url_last = driver.current_url
    # if login_url == login_url_last:
    #     login_state = 0
    # else:
    #     login_state = 1
    # return login_state


if __name__ == '__main__':
    click_login('printhello@163.com', '*********')