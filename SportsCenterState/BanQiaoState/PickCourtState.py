from SportsCenterState.State import State
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from Center.SportsCenter import SportsCenter
import SportsCenterState.BanQiaoState.MainPageState as Main
from SportsCenterState.BanQiaoState.EndState import EndState

class PickCourtState(State):
    def handle(self, center : SportsCenter):
        alert = Alert(center.driver)
        courts = center.targetCourts[center.orderNum]
        for court in courts:
            if "alert" in center.driver.find_element(By.XPATH, court).get_attribute("onclick"):
                continue
            center.driver.find_element(By.XPATH, court).click()
            center.orderNum += 1
            print("Order " + str(center.orderNum) + " in Ban Qiao")
            alert.accept()
            break
        
        if center.orderNum == center.time.hours:
            center.setState(EndState)
        else:
            # //*[@id="ContentPlaceHolder1_Step3Info_lab"]/span[2]/a[1]
            center.driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_Step3Info_lab"]/span[2]/a[1]').click()
            center.setState(Main.MainPageState())
        center.handle()

        # //*[@id="ContentPlaceHolder1_Step3Info_lab"]/span[2]/a[1]