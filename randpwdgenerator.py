from msilib.schema import CheckBox
import random
from tkinter import *
import tkinter

window = Tk()

window.title("Random Password Generator ")

window.geometry("600x600") 
window.configure(bg='grey')

length1 = tkinter.IntVar()
length2 = tkinter.IntVar()
length3 = tkinter.IntVar()
length4 = tkinter.IntVar()
length5 = tkinter.IntVar()

def passwordGeneration(n):
    import random
    import array
    
    MAX_LEN = n
    
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                        'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                        'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                        'z']
    
    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                        'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                        'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                        'Z']
    
    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
            '*', '(', ')', '<']
   
    COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS
    
    rand_digit = random.choice(DIGITS)
    rand_upper = random.choice(UPCASE_CHARACTERS)
    rand_lower = random.choice(LOCASE_CHARACTERS)
    rand_symbol = random.choice(SYMBOLS)
    
    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol
    
    if(MAX_LEN>4):
        for x in range(MAX_LEN - 4):
            temp_pass = temp_pass + random.choice(COMBINED_LIST)
        
            temp_pass_list = array.array('u', temp_pass)
            random.shuffle(temp_pass_list)
        
        password = ""
        for x in temp_pass_list:
                password = password + x
    else:
        password=temp_pass
    return password

def getLength():
    if length1.get() == 4:
        l = Label(window, text=passwordGeneration(4),bg="pink",font=('bold', 15))  
        l.place(x=450,y=160)
    elif length2.get() == 6:
        l = Label(window, text=passwordGeneration(6),bg="lightgreen",font=('bold', 15))  
        l.place(x=460,y=210)
    elif length3.get() == 8:
        l = Label(window, text=passwordGeneration(8), font=('bold', 15))  
        l.place(x=470,y=260)
    elif length4.get() == 10:
        l = Label(window, text=passwordGeneration(10),bg="violet",font=('bold', 15))  
        l.place(x=480,y=310)
    else:
        l = Label(window, text=passwordGeneration(12),bg="yellow",font=('bold', 15))  
        l.place(x=480,y=360)
    l.after(3000, l.destroy)
Font_tuple = ("Comic Sans MS", 20, "bold")
Font_tuple2= ("Adobe Garamond Pro Bold", 20, "bold")
Button(window, text='Generate Password', font=Font_tuple,
       bg='cyan', command=getLength).place(x=210, y=60)
Checkbutton(text='4 character', onvalue=4, offvalue=0,font=Font_tuple2,
            variable=length1,bg='grey',).place(x=250, y=150)
Checkbutton(text='6 character', onvalue=6, offvalue=0,font=Font_tuple2,
            variable=length2,bg='grey').place(x=250, y=200)
Checkbutton(text='8 character', onvalue=8, offvalue=0,font=Font_tuple2,
            variable=length3,bg='grey').place(x=250, y=250)
Checkbutton(text='10 character', onvalue=10, offvalue=0,font=Font_tuple2,
            variable=length4,bg='grey').place(x=250, y=300)
Checkbutton(text='12 character', onvalue=12, offvalue=0,font=Font_tuple2,
            variable=length4,bg='grey').place(x=250, y=350)

window.mainloop()
