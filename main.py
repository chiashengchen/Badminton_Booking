
from Center.JhongJhengSportsCenter import JhongJhengSportCenter
from Center.YongheSportsCenter import YongheSportCenter
from Info.PersonalInfo import PersonalInfo
from Time.ScheduledTime import ScheduledTime
from Center.BanqiaoSportsCenter import BanqiaoSportCenter

if __name__ == '__main__':
    centers = []
    year = 2022
    time1 = ScheduledTime(year, 10, 27, 19, 22, 2, 1)
    time2 = ScheduledTime(year, 10, 20, 19, 22, 2, 1)
    account = input("Account :")
    pwd = input("Password :")
    personalInfo = PersonalInfo(account, pwd)
    centers.append(JhongJhengSportCenter(time1, personalInfo))
    centers.append(YongheSportCenter(time1, personalInfo))
    centers.append(BanqiaoSportCenter(time2, personalInfo))
    for center in centers:
        center.start()
