from Appointment.Appointment import Appointment
from Info.PersonalInfo import PersonalInfo
from Time.ScheduledTime import ScheduledTime

if __name__ == '__main__':
    appointments = []
    year = 2022
    # month1 = input("Booking month : ")
    # day1 = input("Booking day : ")
    # month2 = input("Booking month for Ban Qiao : ")
    # day2 = input("Booking day for Ban Qiao : ")
    # startTime = input("Start time : ")
    # endTime = input("End time : ")
    # hours = input("How much time did you want to play ? ")
    # courts = input("How many courts did you want to order ? ")
    # time1 = ScheduledTime(year, month1, day1, startTime, endTime, int(hours), int(courts))
    month2 = 12
    day2 = 1
    startTime = 19
    endTime = 21
    hours = 2
    courts = 1

    time2 = ScheduledTime(year, month2, day2, startTime, endTime, int(hours), int(courts))
    account1 = 'A131757866'
    pwd1 = 'qasx123'
    account2 = 'A123456789'
    pwd2 = 'xxxxxxx'
    infos = []
    infos.append(PersonalInfo(account1, pwd1))
    infos.append(PersonalInfo(account2, pwd2))
    # appointments.append(Appointment(time2, infos, 'BanQiao'))
    # appointments.append(Appointment(time2, infos, 'DaAn'))
    appointments.append(Appointment(time2, infos, 'JhongJheng'))
    # appointments.append(Appointment(time2, infos, 'LinKou'))
    # appointments.append(Appointment(time2, infos, 'NanGang'))
    # appointments.append(Appointment(time2, infos, 'YongHe'))
    # appointments.append(Appointment(time2, infos, 'ZhugUang'))    

    # account : A131757866
    # pwd : qasx123
    for appointment in appointments:
        appointment.start()
