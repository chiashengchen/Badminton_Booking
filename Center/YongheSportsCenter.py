from selenium import webdriver
from Center.SportsCenter import SportsCenter
from SportsCenterState.YongHeState.LoginState import LoginState
import SportsCenterState.YongHeState.EndState as End
class YongHeSportsCenter(SportsCenter):
    def __init__(self, time, info):
        SportsCenter.__init__(self, time, info)
        self.totalCourts = 6
        self.driver = webdriver.Chrome('./chromedriver')
        try:
            self.driver.get('https://scr.cyc.org.tw/tp10.aspx?module=login_page&files=login&PT=1')
            self.state = LoginState()
        except:
            print("error")
            self.state = End.EndState()
    
    def run(self):
            self.state.handle(self)
