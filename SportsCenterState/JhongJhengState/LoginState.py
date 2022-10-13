
from SportsCenterState.State import State
from SportsCenterState.JhongJhengState.NoticeState import NoticeState
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait

class LoginState(State) :
    
    def handle(self, booking):
        main_window_handle = None
        while not main_window_handle:
            main_window_handle = booking.driver.current_window_handle
        try:
            booking.driver.find_element(By.XPATH, u'//a[text()="確定"]').click()
        except UnexpectedAlertPresentException:
            print('UnexpectedAlertPresentException')
        try:
            booking.driver.find_element(By.XPATH, u'//a[text()="確定"]').click()
        except UnexpectedAlertPresentException:
            print('UnexpectedAlertPresentException')
        account = booking.driver.find_element(By.XPATH, "//*[@id=\"ContentPlaceHolder1_loginid\"]")
        account.clear()
        # 身分證
        account.send_keys(booking.info.getAccount())
        password = booking.driver.find_element(By.XPATH, '//*[@id=\"loginpw\"]') #網頁的密碼點
        password.clear()
        # 密碼
        password.send_keys(booking.info.getPassword())
        WebDriverWait(booking.driver, 10).until(lambda driver: len(booking.driver.find_element(By.XPATH, '//*[@id=\"ContentPlaceHolder1_Captcha_text\"]').get_attribute("value")) == 5)
        booking.driver.find_element(By.XPATH, '//*[@id=\"login_but\"]').click()
        booking.setState(NoticeState())
        booking.handle()