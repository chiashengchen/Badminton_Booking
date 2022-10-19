from selenium import webdriver
from SportsCenterState.DaAnState.LoginState import LoginState
from Center.SportsCenter import SportsCenter
class DaAnSportsCenter(SportsCenter):
    def __init__(self, time, info):
        SportsCenter.__init__(self, time, info)
        self.totalCourts = 6
        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.get('https://scr.cyc.org.tw/tp03.aspx?module=login_page&files=login&PT=1') 
        self.state = LoginState()
    
    def run(self):
        self.state.handle(self)
