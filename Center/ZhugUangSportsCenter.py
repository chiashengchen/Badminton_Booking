from selenium import webdriver
from SportsCenterState.ZhugUangState.LoginState import LoginState
from Center.SportsCenter import SportsCenter

class ZhugUangSportCenter(SportsCenter):
    def __init__(self, time, info):
        SportsCenter.__init__(self, time, info)
        self.totalCourts = 4
        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.get('https://scr.cyc.org.tw/tp16.aspx?module=login_page&files=login&PT=1') 
        self.state = LoginState()
    
    def run(self):
        self.state.handle(self)
