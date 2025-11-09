from tkinter import *

root=Tk()
root.title("Form")
root.geometry("400x400")

frm = Frame(master=root, height=300, width=300, bg="yellow")

t1= Text(frm, text="Enter in your name:")
t2= Text(frm, text="Enter in your age:")
t3= Text(frm, text="Enter in your country:")
t4= Text(frm, text="Enter in your gender:")
t5= Text(frm, text="Enter in your username:")
t6= Text(frm, text="Enter in your password:")

e1= Entry(frm)
e2= Entry(frm)
e3= Entry(frm)
e4= Entry(frm)
e5= Entry(frm)
e6= Entry(show="*")

def btn():
    textbox.insert(END, "form submitted")

textbox = Text()

button = Button(text="Submit", command=btn, bg="red")


frm.pack()

t1.pack()
e1.pack()
t2.pack()
e2.pack()
t3.pack()
e3.pack()
t4.pack()
e4.pack()
t5.pack()
e5.pack()
t6.pack()
e6.pack()

button.pack()
textbox.pack()

root.mainloop()