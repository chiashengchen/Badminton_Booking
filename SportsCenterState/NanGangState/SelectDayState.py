from SportsCenterState.State import State
from selenium.webdriver.common.by import By
from SportsCenterState.NanGangState.SelectPeriod import SelectPeriod
from selenium.common.exceptions import NoSuchElementException
class SelectDayState(State):
    def handle(self, center):
        try:
            center.driver.find_element(By.XPATH, '//*[@onclick=\"GoToStep2(\'' + center.time.getScheduledDate() + '\',1)\"]').click()
            center.setState(SelectPeriod())
        except NoSuchElementException:
            print("error and refresh")
            center.driver.refresh()
            center.setState(SelectDayState())
        center.handle()