from SportsCenterState.State import State
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from Center.SportsCenter import SportsCenter
import SportsCenterState.NanGangState.SelectDayState as Sel
from SportsCenterState.NanGangState.EndState import EndState

class PickCourtState(State):
    def handle(self, center : SportsCenter):
        alert = Alert(center.driver)
        courts = center.targetCourts[center.orderNum]
        for court in courts:
            if "alert" in center.driver.find_element(By.XPATH, court).get_attribute("onclick"):
                continue
            center.driver.find_element(By.XPATH, court).click()
            center.orderNum += 1
            print("Order " + str(center.orderNum) + " in Nan Gang")
            alert.accept()
            break
        
        if center.orderNum == center.time.hours:
            center.setState(EndState)
        else:
            center.driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_Step3Info_lab"]/span[2]/a[3]').click()
            center.setState(Sel.SelectDayState())
        center.handle()