
from SportsCenterState.State import State
from SportsCenterState.JhongJhengState.EndState import EndState
from selenium import webdriver
from selenium.webdriver.common.alert import Alert

class LoginState(State) :
    def __init__(self, time, info):
        State.__init__(self, time, info)
        self.court = 5
        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.get('https://www.cjcf.com.tw/jj01.aspx?module=login_page&files=login&PT=1')
        self.alert = Alert(self.driver)
    
    def handle(self, booking):
        # do log in
        print(type(booking))
        booking.setState(EndState(self.scheduledTime, self.personalInfo))
        booking.handle()