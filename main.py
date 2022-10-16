
from Center.JhongJhengSportsCenter import JhongJhengSportCenter
from Center.YongHeSportsCenter import YongHeSportCenter
from Center.BanQiaoSportsCenter import BanQiaoSportCenter
from Center.NanGangSportsCenter import NanGangSportCenter
from Center.ZhugUangSportsCenter import ZhugUangSportCenter
from Info.PersonalInfo import PersonalInfo
from Time.ScheduledTime import ScheduledTime

if __name__ == '__main__':
    centers = []
    year = 2022
    month = input("Booking month : ")
    day = input("Booking day : ")
    startTime = input("Start time : ")
    endTime = input("End time : ")
    hours = input("How much time did you want to play ? ")
    courts = input("How many courts did you want to order ? ")
    time1 = ScheduledTime(year, month, day, startTime, endTime, int(hours), int(courts))
    day = input("Booking day for Ban Qiao : ")
    time2 = ScheduledTime(year, month, day, startTime, endTime, int(hours), int(courts))
    account = input("Account : ")
    pwd = input("Password : ")
    personalInfo = PersonalInfo(account, pwd)
    centers.append(JhongJhengSportCenter(time1, personalInfo))
    centers.append(YongHeSportCenter(time1, personalInfo))
    centers.append(BanQiaoSportCenter(time2, personalInfo))
    centers.append(NanGangSportCenter(time1, personalInfo))
    # centers.append(ZhugUangSportCenter(time2, personalInfo))
    for center in centers:
        center.start()
