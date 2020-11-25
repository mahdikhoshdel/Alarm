from playsound import playsound
import datetime

AmPm = str(input("AM or PM : "))
alarm_hour = int(input("What hour should i set ? "))
alarm_minute = int(input("What minute should i set ? "))

if(AmPm == "pm"):
    alarm_hour += 12

while(True):
    if(alarm_hour == datetime.datetime.now().hour and alarm_minute == datetime.datetime.now().minute):
        print("Alarm is on !!!")
        playsound("./audio/alarm.mp3")
        break
print("Alarm is done, see you next time...")