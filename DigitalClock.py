
import sys
from tkinnter import *
import time

def tick():
 team_string = time.strftime("%H:%M:%S")
 clock.config(text=time_string)
 clock.after(200,tick)

root = Tk()
clock = Label(root, font = ("times", "bold"), bg= "green")
clock.grid(row=0, colunm=1)
tick()
root.mainloop()
