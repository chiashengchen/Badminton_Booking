from SportsCenterState.State import State
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from SportsCenterState.YongHeState.SelectPeriod import SelectPeriod

class SelectDayState(State):
    def handle(self, center):
        center.driver.find_element(By.XPATH, '//*[@onclick=\"GoToStep2(\'' + center.time.getScheduledDate() + '\',1)\"]').click()
        center.setState(SelectPeriod())
        center.handle()