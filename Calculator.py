'''Created by Travis Allen aka HybridX
This is a pyhton gui calculator built using python 3.x as well as tkinter'''

import sys
from tkinter import *		#Tkinter library 

#Mainframe Snippet - Creates the main/root window in which all widgets will be placed in using the 'grid packer'
window = Tk()					
window.title("Calculator")
window.tk_setPalette(background = "blue")
window.resizable(False, False)
#**************************************************************************************************************************************

#Variable declarations******************************************************************************************************************
number  = StringVar()
stringnum = ""
opertator = ""
memory = ""
#***************************************************************************************************************************************

#Button Functions************************************************************************************************************************
def button_click(num):		
	global stringnum
	stringnum += num
	number.set(stringnum)

def clear():
	global stringnum
	stringnum = ""
	number.set(stringnum)

def equals():
	global stringnum
	result = eval(stringnum)
	number.set(result)
	stringnum = ""
#*****************************************************************************************************************************************

#Entry Widget - A window for the user to type in*******************************************************************************************
entry_window = Entry(window,bg = "white",fg = "black",font = ("arial", 16, "bold"), textvariable = number, bd = 15, justify = "right")
entry_window.grid(columnspan = 10, row = 0)
#******************************************************************************************************************************************

#Button Wigdets*****************************************************************************************************************************
b9 = Button(window,font = ("arial", 16, "bold"),padx=16, pady = 16,bd = 5, text = "9", bg = "sky blue", command= lambda: button_click("9"))
b9.grid(row = 1, column = 0,ipadx = 10, ipady = 10)

b8 = Button(window,font = ("arial", 16, "bold"),padx=16, pady = 16,bd = 5, text = "8", bg = "sky blue",command= lambda: button_click("8"))
b8.grid(column = 1, row =1,ipadx = 10, ipady = 10)

b7 = Button(window,font = ("arial", 16, "bold"),padx=16, pady = 16,bd = 5, text = "7", bg = "sky blue",command= lambda: button_click("7"))
b7.grid(column = 2, row = 1,ipadx = 10, ipady = 10)

b6 = Button(window,font = ("arial", 16, "bold"),padx=16, pady = 16,bd = 5, text = "6", bg = "sky blue",command= lambda: button_click("6"))
b6.grid(row= 2, column = 0,ipadx = 10, ipady = 10)

b5 = Button(window,font = ("arial", 16, "bold"),padx=16, pady = 16,bd = 5, text = "5", bg = "sky blue",command= lambda: button_click("5"))
b5.grid(row= 2, column = 1,ipadx = 10, ipady = 10)

b4 = Button(window,font = ("arial", 16, "bold"),padx=16, pady = 16,bd = 5, text = "4", bg = "sky blue",command= lambda: button_click("4"))
b4.grid(row= 2, column = 2,ipadx = 10, ipady = 10)

b3 = Button(window,font = ("arial", 16, "bold"),padx=16, pady = 16,bd = 5,text = "3", bg = "sky blue",command= lambda: button_click("3"))
b3.grid(row= 3, column = 0,ipadx = 10, ipady = 10)

b2 = Button(window,font = ("arial", 16, "bold"),padx=16, pady = 16,bd = 5, text = "2", bg = "sky blue",command= lambda: button_click("2"))
b2.grid(row= 3, column = 1,ipadx = 10, ipady = 10)

b1 = Button(window,font = ("arial", 16, "bold"),padx=16, pady = 16,bd = 5, text = "1", bg = "sky blue",command= lambda: button_click("1"))
b1.grid(row= 3, column = 2,ipadx = 10, ipady = 10)

b0 = Button(window,font = ("arial", 16, "bold"),padx=16, pady = 16,bd = 5, text = "0", bg = "sky blue",command= lambda: button_click("0"))
b0.grid(row= 4, column = 0,ipadx = 10, ipady = 10)

add_button = Button(window,font = ("arial", 16, "bold"),padx=16, pady = 16,bd = 5, text = "+", bg = "sky blue", command=lambda: button_click("+"))
add_button.grid(row= 1, column = 3,ipadx = 10, ipady = 10)

minus_button = Button(window,font = ("arial", 16, "bold"),padx=16, pady = 16,bd = 5, text = "-", bg = "sky blue", command=lambda: button_click("-"))
minus_button.grid(row= 2, column = 3,ipadx = 10, ipady = 10)

multiply = Button(window,font = ("arial", 16, "bold"),padx=16, pady = 16,bd = 5, text = "*", bg = "sky blue",command=lambda:button_click("*"))
multiply.grid(row= 3, column = 3,ipadx = 10, ipady = 10)

divide = Button(window,font = ("arial", 16, "bold"),padx=16, pady = 16,bd = 5, text = "/", bg = "sky blue",command=lambda: button_click("/"))
divide.grid(row= 4, column = 3,ipadx = 10, ipady = 10)

clear = Button(window,font = ("arial", 16, "bold"),padx=16, pady = 16,bd = 5, text = "C", bg = "sky blue", command= clear)
clear.grid(row= 4, column = 1,ipadx = 10, ipady = 10)

equal = Button(window,font = ("arial", 16, "bold"),padx=16, pady = 16,bd = 5, text = "=", bg = "sky blue", command = equals)
equal.grid(row= 4, column = 2,ipadx = 10, ipady = 10)
#***************************************************************************************************************************************************
window.mainloop()		#Allows GUI to stay on the screen by keeping it in a constant loop