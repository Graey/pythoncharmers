days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
total = 0
year, month, day = map(int, input("Enter the Year, Month and Day:").split())
if (year % 100 == 0):
    year = year / 100
if (year % 4 == 0):
    if(month > 2):
        for i in range(0,month-1):
            total += (days[i])
        total += day+1
    else:
        for i in range(0,month-1):
            total += (days[i])
        total += day
else:
    for i in range(0,month-1):
            total += (days[i])
    total += day


print("%dth Day of the year %d"%(total,year))
