from Center.SportsCenter import SportsCenter
from Court.Court import Court
import Time.ScheduledTime as Time 

class BanQiaoSportsCenter(SportsCenter):
    def __init__(self, time : Time.ScheduledTime):
        SportsCenter.__init__(self, time)
        self._name = 'BanQiao'
        self._url = 'https://www.cjcf.com.tw/CG01.aspx?module=login_page&files=login&PT=1'
        self._totalCourts = 6
        self._emptyCourts = self.initEmptyCourts(time)
        self._bookingGap = 7

    def initEmptyCourts(self, appointment : Time.ScheduledTime):
        emptyCourts = []
        start = appointment.getStartTime()
        end = appointment.getEndTime()
        for time in range(start, end):
            courts = []
            for courtNum in range(self._totalCourts):
                if courtNum == 0:
                    td = 4
                else : 
                    td = 3
                xpath = '//tbody/tr[' + str(self.transTR(time, courtNum)) + ']/td[' + str(td) + ']/img[1]'
                courts.append(Court(time, courtNum, xpath))
            emptyCourts.append(courts)    
        return emptyCourts

    def transTR(self, time, courtNum):
        if time >= 18:
            time -= 18
        elif time >= 12:
            time -= 12
        else :
            time -= 6
        return 2 + time * self._totalCourts + courtNum
        
    
    