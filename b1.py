from tkinter import *
from tkinter import messagebox

root=Tk()
root.title("Form")
root.geometry("400x400")
root.configure(bg="orange")

frm = Frame(master=root, height=300, width=300, bg="yellow")

t1= Label(frm, text="Enter in your name:")
t2= Label(frm, text="Enter in your age:")
t3= Label(frm, text="Enter in your country:")
t4= Label(frm, text="Enter in your gender:")
t5= Label(frm, text="Enter in your username:")
t6= Label(frm, text="Enter in your password:")

e1= Entry(frm)
e2= Entry(frm)
e3= Entry(frm)
e4= Entry(frm)
e5= Entry(frm)
e6= Entry(frm, show="*")

def btn():
    messagebox.showinfo("Notification", "Form Submitted")

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

root.mainloop()