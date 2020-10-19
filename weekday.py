weekdays = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
week = int(input("Enter the Weekday Number: "))

if(week>7):
    print("Invalid Input")

else:
    print(weekdays[week-1])
