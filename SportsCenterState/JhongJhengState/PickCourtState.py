from lib2to3.pgen2 import driver
from SportsCenterState.State import State
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from Time.ScheduledTime import DayPeriods
from Center.SportsCenter import SportsCenter
import SportsCenterState.JhongJhengState.MainPageState as Main
from SportsCenterState.JhongJhengState.EndState import EndState

class PickCourtState(State):
    def handle(self, center : SportsCenter):
        alert = Alert(center.driver)
        courts = center.targetCourts[center.orderNum]
        for court in courts:
            if "alert" in center.driver.find_element(By.XPATH, court).get_attribute("onclick"):
                continue
            center.driver.find_element(By.XPATH, court).click()
            center.orderNum += 1
            break
        alert.accept()
        if center.orderNum == center.time.hours:
            center.setState(EndState)
        else:
            # click go back to home //*[@id="ContentPlaceHolder1_Step3Info_lab"]/span[2]/a[1]
            center.driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_Step3Info_lab"]/span[2]/a[1]').click()
            center.setState(Main.MainPageState())
        center.handle()