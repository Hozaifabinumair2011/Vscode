# Simple Animated Mother's Day Card 💖

from tkinter import *

# Window
root = Tk()
root.title("Mother's Day")
root.geometry("500x300")
root.config(bg="pink")

# Message
text = Label(
    root,
    text="🌸 Happy Mother's Day Mom 🌸",
    font=("Arial", 22, "bold"),
    bg="pink",
    fg="red"
)
text.pack(pady=100)

# Animation colors
colors = ["red", "purple", "blue", "green", "orange"]

# Animation function
def animate(i=0):
    text.config(fg=colors[i % len(colors)])
    root.after(500, animate, i + 1)  # changes color every 0.5 sec

# Start animation
animate()

# Run window
root.mainloop()