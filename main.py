
from Center.YongheSportsCenter import YongheSportCenter
from Info.PersonalInfo import PersonalInfo
from Time.ScheduledTime import ScheduledTime

if __name__ == '__main__':
    year = 2022
    month = input()
    day = input()
    time = ScheduledTime(year, month, day, 0, 0)
    personalInfo = PersonalInfo('A000000000', '123456')
    center = YongheSportCenter(time, personalInfo)
    center.fakeRun()