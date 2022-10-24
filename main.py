
from Center.JhongJhengSportsCenter import JhongJhengSportsCenter
from Center.YongHeSportsCenter import YongHeSportsCenter
from Center.BanQiaoSportsCenter import BanQiaoSportsCenter
from Center.NanGangSportsCenter import NanGangSportsCenter
from Center.DaAnSportsCenter import DaAnSportsCenter
from Center.LinKouSportsCenter import LinKouSportsCenter
from Center.ZhugUangSportsCenter import ZhugUangSportsCenter
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
    month = input("Booking month for Ban Qiao : ")
    day = input("Booking day for Ban Qiao : ")
    time2 = ScheduledTime(year, month, day, startTime, endTime, int(hours), int(courts))
    account = input("Account : ")
    pwd = input("Password : ")
    personalInfo = PersonalInfo(account, pwd)
    # centers.append(ZhugUangSportsCenter(time2, personalInfo))

    centers.append(BanQiaoSportsCenter(time2, personalInfo))
    # centers.append(JhongJhengSportsCenter(time1, personalInfo))
    # centers.append(YongHeSportsCenter(time1, personalInfo))
    
    # centers.append(NanGangSportsCenter(time1, personalInfo))
    # centers.append(DaAnSportsCenter(time1, personalInfo))
    # centers.append(LinKouSportsCenter(time1, personalInfo))
    # tmp_center = ZhugUangSportsCenter(time2, personalInfo)
    # tmp_center.handle()
    for center in centers:
        center.start()
