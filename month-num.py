months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
month = int(input("Enter the Month Number: "))

if(month>12):
    print("Invalid Input")

else:
    print(months[month-1])
