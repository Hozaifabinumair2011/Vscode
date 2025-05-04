from tkinter import *
from PIL import Image,ImageTk
root = Tk()
root.geometry("400x300")
root.title("main screen")
upload=Image.open("helo.jpeg")
i=ImageTk.PhotoImage(upload)
l=Label(root,image=i,height=350,width=300)
l.place(x=50,y=0)
l2=Label(root,text="this is image")
l2.place(x=40,y=360)
root.mainloop()