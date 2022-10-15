from SportsCenterState.State import State
from selenium.webdriver.common.by import By
from SportsCenterState.YongheState.PickCourtState import PickCourtState
from Time.ScheduledTime import DayPeriods
from Center.SportsCenter import SportsCenter

class CalculateEmptyCourtsState(State):
    # TODO : calculate continuous time courts
    def handle(self, center : SportsCenter):
        if center.time.getCalendarDayPeriods() == DayPeriods.AFTERNOON:
            startTime = center.time.startTime - 12
            endTime = center.time.endTime - 12
            
        elif center.time.getCalendarDayPeriods() == DayPeriods.EVENING:
            startTime = center.time.startTime - 18
            endTime = center.time.endTime - 18

        else :
            startTime = center.time.startTime - 6
            endTime = center.time.endTime - 6

        emptyCourts = []
        numOfCourt = 0
        for time in range(startTime, endTime):
            courts = []
            for i in range(center.totalCourts) :
                if i == 0:
                    td = 4
                else :
                    td = 3
                if "alert" in center.driver.find_element(By.XPATH, '//tbody/tr[' + str(2 + time * center.totalCourts + i) + ']/td[' + str(td) + ']/img[1]').get_attribute("onclick"):
                    continue
                courts.append('//tbody/tr[' + str(2 + time * center.totalCourts + i) + ']/td[' + str(td) + ']/img[1]')
            if len(courts) >= center.time.court:
                emptyCourts.append(courts)
                numOfCourt += 1
            else :
                emptyCourts.append(None)
        if numOfCourt < center.time.hours:
            print("Not enough courts !!")
            return

        self.findContinousCorts(emptyCourts, center)

        center.emptyCourts = emptyCourts
        center.setState(PickCourtState())
        center.handle()

    def findContinousCorts(self, emptyCourts, center : SportsCenter):
        length = len(emptyCourts)
        curContinousNum = 0
        targetTime = -1
        for i in range(length):
            if emptyCourts[i] == None:
                print("empty court")
                targetTime = -1
                curContinousNum = 0
                continue
            if targetTime == -1:
                targetTime = i
            curContinousNum += 1
            if curContinousNum == center.time.hours:
                break
        if curContinousNum != center.time.hours:
            print("No continous courts !!")
            return
        targetCourts = []
        for i in range(targetTime, targetTime + curContinousNum):
            targetCourts.append(emptyCourts[i])
        center.targetTime = targetTime + center.time.startTime
        center.targetCourts = targetCourts