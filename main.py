
from Center.JhongJhengSportsCenter import JhongJhengSportCenter
from Center.YongheSportsCenter import YongheSportCenter
from Info.PersonalInfo import PersonalInfo
from Time.ScheduledTime import ScheduledTime

if __name__ == '__main__':
    centers = []
    year = 2022
    month = input("Booking month :")
    day = input("Booking day :")
    startTime = input("Start time :")
    endTime = input("End time :")
    hours = input("How much time did you want to play ?")
    courts = input("How many courts did you want to order ?")
    time = ScheduledTime(year, month, day, startTime, endTime, int(hours), int(courts))
    account = input("Account :")
    pwd = input("Password :")
    personalInfo = PersonalInfo(account, pwd)
    centers.append(JhongJhengSportCenter(time, personalInfo))
    centers.append(YongheSportCenter(time, personalInfo))
    for center in centers:
        center.start()
