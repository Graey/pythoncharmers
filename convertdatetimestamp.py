# Python program to convert 
# date to timestamp 


import time 
import datetime 


string = "20/01/2020"
print(time.mktime(datetime.datetime.strptime(string, 
											"%d/%m/%Y").timetuple())) 
