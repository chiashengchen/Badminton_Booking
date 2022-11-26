from SportsCenterState.State import State
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from Center.SportsCenter import SportsCenter
import SportsCenterState.MainPageState as Main
from SportsCenterState.EndState import EndState
import Content.Content as Content

class PickCourtState(State):
    def handle(self, content : Content.Content):
        driver = content.getDriver()
        lock = content.getLock()
        alert = Alert(driver)
        lock.acquire()
        targetCourts = content.getCenter().getTargetCourts()
        for court in targetCourts:
            if "alert" in driver.find_element(By.XPATH, court.getXPath()).get_attribute("onclick"):
                continue
            driver.find_element(By.XPATH, court.getXPath()).click()
            targetCourts.remove(court)
            alert.accept()
            break
        lock.release()
        if not targetCourts:
            content.setState(EndState())
        else:
            driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_Step3Info_lab"]/span[2]/a[1]').click()
            content.setState(Main.MainPageState())
        # TODO : Error state, booking fail. Go back to main page
        content.handle()