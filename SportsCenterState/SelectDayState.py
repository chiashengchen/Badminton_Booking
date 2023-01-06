from SportsCenterState.State import State
from selenium.webdriver.common.by import By
from SportsCenterState.CalculateEmptyCourtsState import CalculateEmptyCourtsState
import SportsCenterState.EndState as End
from selenium.common.exceptions import NoSuchElementException
import time
import Content.Content as Content

class SelectDayState(State):
    def handle(self, content : Content.Content):
        driver = content.getDriver()
        center = content.getCenter()
        try:
            driver.find_element(By.XPATH, '//*[@onclick=\"GoToStep2(\'' + content.getTime().getScheduledDate() + '\',1)\"]').click()
            content.setState(CalculateEmptyCourtsState())
        except NoSuchElementException:
            while(not content.isAfterPrepareTime()):
                print("[WAITING]")
                time.sleep(10)
                pass
            if(content.isAfterBufferTime()):
                print("[NOT AVAILABLE IN " + center.getName() +"]")
                content.setState(End.EndState())
            else :
                time.sleep(2)
                driver.refresh()
                content.setState(SelectDayState())
        content.handle()