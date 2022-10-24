from selenium import webdriver
from SportsCenterState.BanQiaoState.LoginState import LoginState
from Center.SportsCenter import SportsCenter
import SportsCenterState.BanQiaoState.EndState as End
from selenium.common.exceptions import WebDriverException
class BanQiaoSportsCenter(SportsCenter):
    def __init__(self, time, info):
        SportsCenter.__init__(self, time, info)
        self.totalCourts = 6
        self.driver = webdriver.Chrome('./chromedriver')
        try :
            self.driver.get('https://www.cjcf.com.tw/CG01.aspx?module=login_page&files=login&PT=1')
            self.state = LoginState() 
            self.mockError()
        except :
            print("error: cannot load page")
            self.state = End.EndState()
        
    def run(self):
        self.state.handle(self)

    def mockError(self):
        raise WebDriverException
