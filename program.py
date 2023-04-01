from tkinter import *
root = Tk()
root.title("Circle Area")

#circle area = πr ,π = 3.14
Label(text="radius",font=30).grid(row=0,sticky=W)
radius = IntVar()
et1 = Entry(width=30,textvariable=radius,font=30)
et1.grid(row=0,column=1)

Label(text="circle area",font=30).grid(row=1,stick=W)
et2 = Entry(width=30,font=30)
et2.grid(row=1,column=1)


def calculate():
    et2.delete(0,END)
    r = radius.get()
    area = 3.14*r*r
    et2.insert(0,area)

def deleteText():
    et1.delete(0,END)
    et2.delete(0,END)
    

btn=Button(text="calculate",command=calculate).grid(row=2,column=1,stick=W)
btn=Button(text="delete",command=deleteText).grid(row=2,column=1,stick=E)

root.mainloop()


