hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# put your code here
endtime = hour*60 + mins + dura
hour2 = endtime // 60
if hour2 > 23:
    hour2 %= 24
mins2 = endtime % 60
print(hour2, mins2, sep=':')
