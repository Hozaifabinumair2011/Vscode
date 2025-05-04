from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("400x300")
root.title("main screen")
def msg():
    messagebox.showwarning("alert","stop virus found")
btn=Button(root,text="Scan for virus",command=msg)
btn.place(x=40,y=80)
root.mainloop()
#showwarning,showinfo,showerror,askquestion,askokcacel,askyesno,askretrycancel