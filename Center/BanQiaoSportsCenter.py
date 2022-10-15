from selenium import webdriver
from SportsCenterState.BanQiaoState.LoginState import LoginState
from Center.SportsCenter import SportsCenter

class BanQiaoSportCenter(SportsCenter):
    def __init__(self, time, info):
        SportsCenter.__init__(self, time, info)
        self.totalCourts = 5
        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.get('https://www.cjcf.com.tw/CG01.aspx?module=login_page&files=login&PT=1') 
        self.state = LoginState()
    
    def run(self):
        self.state.handle(self)
