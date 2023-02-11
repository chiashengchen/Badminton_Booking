from Appointment.Appointment import Appointment
from Info.PersonalInfo import PersonalInfo
from Time.ScheduledTime import ScheduledTime

if __name__ == '__main__':
    appointments = []
    year1 = 2023
    year2 = 2023
    # month1 = input("Booking month two weeks later : ")
    # day1 = input("Booking day two weeks later : ")
    # month2 = input("Booking month one week later : ")
    # day2 = input("Booking day one week later  : ")
    # startTime = input("Start time : ")
    # endTime = input("End time : ")
    # hours = input("How much time did you want to play ? ")
    # courts = input("How many courts did you want to order ? ")
    month2 = 1
    day2 = 14
    month1 = 1
    day1 = 7
    startTime = 14
    endTime = 18
    hours = 2
    courts = 1

    time2week = ScheduledTime(year2, month2, day2, startTime, endTime, int(hours), int(courts))
    time1week = ScheduledTime(year1, month1, day1, startTime, endTime, int(hours), int(courts))
    account1 = 'A131757866'
    pwd1 = 'qasx123'
    account2 = 'A123456789'
    pwd2 = 'xxxxxxx'
    infos = []
    infos.append(PersonalInfo(account1, pwd1))
    infos.append(PersonalInfo(account2, pwd2))
    appointments.append(Appointment(time1week, infos, 'BanQiao'))
    appointments.append(Appointment(time2week, infos, 'DaAn'))
    appointments.append(Appointment(time2week, infos, 'JhongJheng'))
    appointments.append(Appointment(time2week, infos, 'LinKou'))
    appointments.append(Appointment(time2week, infos, 'NanGang'))
    appointments.append(Appointment(time2week, infos, 'YongHe'))
    # appointments.append(Appointment(time1week, infos, 'ZhugUang'))    

    # account : A131757866
    # pwd : qasx123
    for appointment in appointments:
        appointment.start()
