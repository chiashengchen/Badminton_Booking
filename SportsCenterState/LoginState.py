
from SportsCenterState.State import State
from SportsCenterState.MainPageState import MainPageState
from Center.SportsCenter import SportsCenter
from Content.Content import Content
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.alert import Alert

class LoginState(State) :
    def handle(self, content : Content):
        driver = content.getDriver()
        info = content.getInfo()
        alert = Alert(driver)
        # 一開始進去是兩個 alert, 驗證碼錯誤是一個 alert
        try:
            alert.accept()
            alert.accept()
        except :
            print("BUG ?")
        account = driver.find_element(By.XPATH, "//*[@id=\"ContentPlaceHolder1_loginid\"]")
        account.clear()
        account.send_keys(info.getAccount())
        password = driver.find_element(By.XPATH, '//*[@id=\"loginpw\"]') #網頁的密碼點
        password.clear()
        password.send_keys(info.getPassword())
        WebDriverWait(driver, 600).until(lambda driver: len(driver.find_element(By.XPATH, '//*[@id=\"ContentPlaceHolder1_Captcha_text\"]').get_attribute("value")) == 5)
        driver.find_element(By.XPATH, '//*[@id=\"login_but\"]').click()
        # 驗證碼錯誤
        try:
            if (alert != None and '驗證碼錯誤' in alert.text):
                content.setState(LoginState())
        except NoAlertPresentException:
            content.setState(MainPageState())
        content.handle()