from tkinter import *
window = Tk()
window.title("Sample Window")
window.geometry("300x300")
greeting = Label(text="Helo Everyone",fg="orange",bg="black")
button = Button(text="Click Me",fg="blue",bg="yellow")
greeting.pack()
button.pack()
entry=Entry(fg="white",bg="lime")
entry.pack()
textbox=Text(fg="lime",bg="white")
textbox.pack()
frame=Frame(master=window,relief=RAISED,borderwidth=5)
frame.pack()
window.mainloop()