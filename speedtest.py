from tkinter import *
from timeit import default_timer as timer
import random

window = Tk()

window.geometry("450x200")
window.title("speedtest")

x = 0


def game():
    global x

    if x == 0:
        window.destroy()
        x = x + 1

    def check_result():
        if entry.get() == words[word]:

            end = timer()
            t=(end - start)
            l = Label(windows,text =t,font=("Times New Roman",18,"bold")).place(x = 170,y = 150) 
        else:
            l = Label(windows,text ="Wrong Input!",font=("Times New Roman",18,"bold")).place(x = 170,y = 150)

    words = ['programming', 'coding', 'algorithm',
             'systems', 'python', 'software']

    word = random.randint(0, (len(words) - 1))

    start = timer()
    windows = Tk()
    windows.title("game")
    windows.geometry("450x200")

    x2 = Label(windows, text=words[word], font=("Comic Sans MS",20))

    x2.place(x=75, y=60)
    x3 = Label(windows, text="Type the below word:", font="times 20")
    x3.place(x=1, y=5)

    entry = Entry(windows)
    entry.place(x=280, y=70)

    b2 = Button(windows, text="Done",
                command=check_result, width=12, bg='cyan')
    b2.place(x=150, y=120)

    b3 = Button(windows, text="Try Again",
                command=game, width=12, bg='coral')
    b3.place(x=250, y=120)
    windows.mainloop()


x1 = Label(window, text="Lets start playing..", font="times 20",bg="gold")
x1.place(x=10, y=50)

b1 = Button(window, text="Go", command=game, width=12, bg='lightgreen')
b1.place(x=150, y=150)

window.mainloop()