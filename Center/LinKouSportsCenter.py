from selenium import webdriver
from SportsCenterState.LinKouState.LoginState import LoginState
from Center.SportsCenter import SportsCenter
import SportsCenterState.LinKouState.EndState as End
class LinKouSportsCenter(SportsCenter):
    def __init__(self, time, info):
        SportsCenter.__init__(self, time, info)
        self.totalCourts = 4
        self.driver = webdriver.Chrome('./chromedriver')
        try :
            self.driver.get('https://scr.cyc.org.tw/tp17.aspx?module=login_page&files=login&PT=1')
            self.state = LoginState() 
        except :
            print("error")            
            self.state = End.EndState()
        
    
    def run(self):
        self.state.handle(self)
