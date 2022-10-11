
from Center.YongheSportsCenter import YongheSportCenter
from Info.PersonalInfo import PersonalInfo
from Time.ScheduledTime import ScheduledTime

if __name__ == '__main__':
    year = 2022
    month = input("Booking month :")
    day = input("Booking day :")
    startTime = input("Start time :")
    endTime = input("End time :")
    time = ScheduledTime(year, month, day, startTime, endTime, 2, 1)
    account = input("Account :")
    pwd = input("Password :")
    personalInfo = PersonalInfo(account, pwd)
    center = YongheSportCenter(time, personalInfo)
    center.fakeRun()
