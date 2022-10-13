from SportsCenterState.State import State
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

class SelectDayState(State):
    def handle(self, booking):
        booking.driver.find_element(By.XPATH, '//*[@onclick=\"GoToStep2(\'' + booking.time.getScheduledDate() + '\',1)\"]').click()