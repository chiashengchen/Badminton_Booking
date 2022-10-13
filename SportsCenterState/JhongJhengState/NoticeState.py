
from SportsCenterState.State import State
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
class NoticeState(State):

    def handle(self, booking):
        alert = Alert(booking.driver)
        booking.driver.find_element(By.XPATH, '//*[@title=\"羽球\"]').click()
        alert.accept()
        booking.driver.find_element(By.XPATH, '//*[@src=\"img/conf01.png\"]').click()
        alert.accept()