from tkinter import *
root = Tk()
var1 = IntVar()
var2 = IntVar()
c1 = Checkbutton(root,text = "like Mango ? ",variable = var1,onvalue = 1,offvalue = 0,width = 40)
c2 = Checkbutton(root,text = "like Orange ? ",variable = var2,onvalue = 1,offvalue = 0,width = 40)
c1.pack()
c2.pack()
root.mainloop()