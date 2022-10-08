
from Center.YongheSportsCenter import YongheSportCenter
from Info.PersonalInfo import PersonalInfo
from Time.ScheduledTime import ScheduledTime

if __name__ == '__main__':
    year = 2022
    print("Booking month :")
    month = input()
    print("Booking day :")
    day = input()
    print("Start time :")
    startTime = input()
    print("End time")
    endTime = input()
    time = ScheduledTime(year, month, day, startTime, endTime)
    print("Account :")
    account = input()
    print("Password :")
    pwd = input()
    personalInfo = PersonalInfo(account, pwd)
    center = YongheSportCenter(time, personalInfo)
    center.fakeRun()