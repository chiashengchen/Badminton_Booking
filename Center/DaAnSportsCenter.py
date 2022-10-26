from selenium import webdriver
from SportsCenterState.BanQiaoState.EndState import EndState
from SportsCenterState.DaAnState.LoginState import LoginState
from Center.SportsCenter import SportsCenter
import SportsCenterState.DaAnState.EndState as End
from selenium.webdriver.chrome.options import Options

class DaAnSportsCenter(SportsCenter):
    def __init__(self, time, info):
        SportsCenter.__init__(self, time, info)
        self.totalCourts = 6
        opts = Options()
        opts.add_argument("--incognito")  
        ua = "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0"
        opts.add_argument("user-agent={}".format(ua))  
        self.driver = webdriver.Chrome(executable_path='./chromedriver',chrome_options=opts)
        
        try : 
            self.driver.get('https://scr.cyc.org.tw/tp03.aspx?module=login_page&files=login&PT=1') 
            self.state = LoginState()
        except : 
            print("error: cannot load page")
            self.state = End.EndState()
        
    
    def run(self):
        self.state.handle(self)
