
from SportsCenterState.State import State
from SportsCenterState.BanQiaoState.MainPageState import MainPageState
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from Center.SportsCenter import SportsCenter
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.alert import Alert

class LoginState(State) :
    def handle(self, center : SportsCenter):
        alert = Alert(center.driver)
        # 一開始進去是兩個 alert, 驗證碼錯誤是一個 alert
        try:
            alert.accept()
            alert.accept()
        except :
            print("BUG ?")
        account = center.driver.find_element(By.XPATH, "//*[@id=\"ContentPlaceHolder1_loginid\"]")
        account.clear()
        account.send_keys(center.info.getAccount())
        password = center.driver.find_element(By.XPATH, '//*[@id=\"loginpw\"]') #網頁的密碼點
        password.clear()
        password.send_keys(center.info.getPassword())
        WebDriverWait(center.driver, 600).until(lambda driver: len(center.driver.find_element(By.XPATH, '//*[@id=\"ContentPlaceHolder1_Captcha_text\"]').get_attribute("value")) == 5)
        center.driver.find_element(By.XPATH, '//*[@id=\"login_but\"]').click()
        # 驗證碼錯誤
        try:
            if (alert != None and '驗證碼錯誤' in alert.text):
                center.setState(LoginState())
        except NoAlertPresentException:
            center.setState(MainPageState())
        center.handle()