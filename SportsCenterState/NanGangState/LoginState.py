from SportsCenterState.State import State
from SportsCenterState.NanGangState.MainPageState import MainPageState
from selenium.webdriver.common.by import By
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from Center.SportsCenter import SportsCenter

class LoginState(State) :
    
    def handle(self, center : SportsCenter):
        main_window_handle = None
        while not main_window_handle:
            main_window_handle = center.driver.current_window_handle
        try:
            center.driver.find_element(By.XPATH, u'//a[text()="確定"]').click()
        except UnexpectedAlertPresentException:
            print('UnexpectedAlertPresentException')
        try:
            center.driver.find_element(By.XPATH, u'//a[text()="確定"]').click()
        except UnexpectedAlertPresentException:
            print('UnexpectedAlertPresentException')
        account = center.driver.find_element(By.XPATH, "//*[@id=\"ContentPlaceHolder1_loginid\"]")
        account.clear()
        # 身分證
        account.send_keys(center.info.getAccount())
        password = center.driver.find_element(By.XPATH, '//*[@id=\"loginpw\"]') #網頁的密碼點
        password.clear()
        # 密碼
        password.send_keys(center.info.getPassword())
        WebDriverWait(center.driver, 600).until(lambda driver: len(center.driver.find_element(By.XPATH, '//*[@id=\"ContentPlaceHolder1_Captcha_text\"]').get_attribute("value")) == 5)
        center.driver.find_element(By.XPATH, '//*[@id=\"login_but\"]').click()
        center.setState(MainPageState())
        center.handle()