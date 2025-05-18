from tkinter import*
from tkinter import messagebox
root = Tk()
root.title('Denomination Counter')
root.configure(bg='light blue')
root.geometry('650x400')

label1 = Label(root,text="Hey user ! Welcome to Denomination counter Application",bg='Light blue')
label1.place(x=190 , y=340 , anchor=CENTER)
def msg():
    MSGBOX = messagebox.showinfo("Alert","Do you want to calculate the denomination counbt?")
    if MSGBOX == 'ok':
        topwin()
button1=Button(root,text="Lets get Started !",command=msg,bg='brown',fg='white')
button1.place(x=260, y=360)
def topwin():
    top =Toplevel()
    top.title("Denomination Calculator")
    top.cofigure(bg='light grey')
    top.geometry("600x300+50+50")
    label=Label(top,text="Enter total amount", bg='light grey')
    entry=Entry(top)
    lbl = Label(top, text="Here are numbers of notes for each denomination",bg='light grey')
    l1 =Label(top, text="2000",bg='light grey')
    l2 =Label(top, text="500",bg='light grey')
    l3 =Label(top, text="100",bg='light grey')

    t1=Entry(top)
    t2=Entry(top)
    t3=Entry(top)

    def calculator():
        try:
            global amount
            amount = int(entry