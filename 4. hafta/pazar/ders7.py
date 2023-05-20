from tkinter import *
from datetime import date, datetime

window = Tk() #initializes tkinter to create display window
window.geometry('500x300') # width and height of the window
window.resizable(0, 0) # sets fix size of window
window.title(' Age calculator') # gives the window a title

yasiniz = Label(window,fg="red",text = "Gün \t\tAy \tYıl",font='arial 12 bold').place(x = 210)
setYourAlarm = Label(window,text = "Doğum tarihinizi giriniz: ",bg="grey",font="arial 11 bold").place(x=80, y=40)

date = StringVar()
month = StringVar()
year = StringVar()

dateTime= Entry(window,textvariable = date, relief = RAISED, width = 4,font=(20)).place(x=210,y=40)
monthTime= Entry(window,textvariable = month,width = 4,font=(20)).place(x=270,y=40)
yearTime = Entry(window,textvariable = year,width = 4,font=(20)).place(x=330,y=40)

def age():
    # Get current date
    today = datetime.today().date()

    setAge_year = int(year.get())
    setAge_month = int(month.get())
    setAge_date = int(date.get())

    current_age = today.year-int(setAge_year)
    if today.month < setAge_month or today.month == setAge_month and today.day < setAge_date:
         current_age -= 1

    CurrentLabel = Label(window, text=f'Siz: {current_age} yaşındasınız',fg='black')
    CurrentLabel.place(relx=0.2, rely=0.8, anchor=CENTER)

submit = Button(window,text = "Yaşınızı hesaplayın",fg="red",width = 20,command=age,font=("arial 15 bold" )).place(x=90,y=100)
exit = Button(window,text = "Çıkış",fg="red",width = 10,command=window.destroy,font=("arial 20 bold" )).place(x=150,y=140)

window.mainloop()