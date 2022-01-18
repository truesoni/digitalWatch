from tkinter import * 
from tkinter.ttk import *
from time import strftime

# Just Begin Our code by creating a root
root = Tk()

# Creating a title as 'Clock'
root.title("Digital Clock") 

# Function Definition
def timeCheck():
    str = strftime('%H:%M:%S %p')
    label.config(text=str)
    label.after(1000, timeCheck)

# Labeling 
label = Label(root,  font=("ds-digital",75), background = "black", foreground = "cyan")
label.pack(anchor = "center")

# Function call
timeCheck()

# Mainloop method to run our project 
mainloop()