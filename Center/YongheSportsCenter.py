

from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException
import time
import logging
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from SportsCenter import SportCenter

year = 2022
month = input()
day = input()
if len(day) < 2:
    brookingDay = str(year) + '/'+ str(month) + '/0' + str(day)
else:
    brookingDay = str(year) + '/'+ str(month) + '/' + str(day)

class YongheSportCenter(SportCenter):
    def run(self):
        driver = webdriver.Chrome('./chromedriver')
        driver.get('https://scr.cyc.org.tw/tp10.aspx?module=login_page&files=login&PT=1')

        main_window_handle = None
        while not main_window_handle:
            main_window_handle = driver.current_window_handle
        try:
            driver.find_element(By.XPATH, u'//a[text()="確定"]').click()
        except UnexpectedAlertPresentException:
            print('UnexpectedAlertPresentException')
        try:
            driver.find_element(By.XPATH, u'//a[text()="確定"]').click()
        except UnexpectedAlertPresentException:
            print('UnexpectedAlertPresentException')
        alert = Alert(driver)
        # Login
        account = driver.find_element(By.XPATH, "//*[@id=\"ContentPlaceHolder1_loginid\"]")
        account.clear()
        # 身分證
        account.send_keys("A000000000")
        password = driver.find_element(By.XPATH, '//*[@id=\"loginpw\"]') #網頁的密碼點
        password.clear()
        # 密碼
        password.send_keys("123456")

        verification_code = input()
        password = driver.find_element(By.XPATH, '//*[@id=\"ContentPlaceHolder1_Captcha_text\"]') #網頁的密碼點
        password.clear()
        password.send_keys(verification_code)
        driver.find_element(By.XPATH, '//*[@id=\"login_but\"]').click()
        driver.find_element(By.XPATH, '//*[@title=\"羽球\"]').click()
        driver.find_element(By.XPATH, '//*[@src=\"img/conf01.png\"]').click()

        alert.accept()
        # TODO : try & except
        driver.find_element(By.XPATH, '//*[@onclick=\"GoToStep2(\'' + brookingDay+ '\',1)\"]').click()
        driver.find_element(By.XPATH, '//tbody/tr[8]/td[4]/img[1]').click()
        print(alert.text)
        # 已被預約！
        alert.accept() 
        # driver.find_element(By.XPATH, '//*[@onclick="if(confirm(\'您是否確定預約「羽\d 06:00~07:00」？\')){Step3Action(1137,6)}"').click()

        # <img name="PlaceBtn" src="img/sche01.png" width="87" height="21" onclick="if(confirm('您是否確定預約「羽5 06:00~07:00」？')){Step3Action(1137,6)}">
        print('finish')

if __name__ == '__main__':
    center = YongheSportCenter()