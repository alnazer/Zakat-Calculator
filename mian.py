#Zakat Calculator 
from tkinter import *
from tkinter import ttk
import constantes as define


window = Tk()
window.title(define.PROGTITLE)

"""actions start"""
def do_clear():
    global resultString
    resultString.set(0)
    
def do_calculat():
    global resultString
    amount  = resultString.get()
    amount = int(amount)
    if amount < 100:
        resultString.set("0")
    else:
        zakat = float(amount )/40
        resultString.set(zakat)
    
def add_number(number):
    global resultString
    if resultString.get() == "0":
        screen_ammonut = str(number)
    else:
        screen_ammonut = resultString.get()+str(number)
        
    resultString.set(screen_ammonut)

def do_undo():
    global resultString
    screnn_value = resultString.get()
    if int(screnn_value) >= 10:
        resultString.set(screnn_value[0:-1])
    
    
"""actions end""" 

resultString = StringVar()
resultString.set(0)


#first row
screen_label = ttk.Label(text="0",textvariable=resultString,font=("Arial", 20,"bold"),width=16).grid(row=0,column=0,columnspan=5,padx=10)
#second  row btn 987
btn_sevin = ttk.Button(text=define.BUTTONSEVIEN,command=lambda:add_number(7)).grid(row=1,column=1)
btn_egiht = ttk.Button(text=define.BUTTONEIGHT,command=lambda:add_number(8)).grid(row=1,column=2)
btn_nine = ttk.Button(text=define.BUTTONNINE,command=lambda:add_number(9)).grid(row=1,column=3)

#Three row 654
btn_four = ttk.Button(text=define.BUTTONFOUR,command=lambda:add_number(4)).grid(row=2,column=1)
btn_five = ttk.Button(text=define.BUTTONFIVE,command=lambda:add_number(5)).grid(row=2,column=2)
btn_six = ttk.Button(text=define.BUTTONSIX,command=lambda:add_number(6)).grid(row=2,column=3)

#forty row 123
btn_one = ttk.Button(text=define.BUTTONONE,command=lambda:add_number(1)).grid(row=3,column=1)
btn_tow = ttk.Button(text=define.BUTTONTOW,command=lambda:add_number(2)).grid(row=3,column=2)
btn_three = ttk.Button(text=define.BUTTONTHREE,command=lambda:add_number(3)).grid(row=3,column=3)

#fifty  row 0 cal clear
btn_calcu = ttk.Button(text=define.BUTTONCALTEXT,command=lambda:do_calculat()).grid(row=4,column=1)
btn_clear = ttk.Button(text=define.BUTTONCLEAR,command=lambda:do_clear()).grid(row=4,column=2)
btn_zero = ttk.Button(text=define.BUTTONZERO,command=lambda:add_number(0)).grid(row=4,column=3)

btn_undo = ttk.Button(text=define.BUTTONUNDO,command=lambda:do_undo()).grid(row=5,column=1)

window.mainloop()