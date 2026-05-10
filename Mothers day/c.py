# Mother's Day Animated Card 💖
from tkinter import *
import random

root = Tk()
root.title("Happy Mother's Day 💖")
root.geometry("700x500")
root.config(bg="#ffccdd")

canvas = Canvas(root, width=700, height=500, bg="#ffccdd", highlightthickness=0)
canvas.pack(fill="both", expand=True)

messages = [
    "Thank you for always being there 💖",
    "You are the best mom ever 🌸",
    "Your love makes everything better ✨",
    "Home feels warm because of you 🏡",
    "You are my real-life superhero 🦸‍♀️"
]

# Title
title = Label(root, text="🌷 Happy Mother's Day 🌷",
              font=("Comic Sans MS", 26, "bold"),
              bg="#ffccdd", fg="#d63384")
title.place(x=120, y=20)

# Message
msg_label = Label(root, text="Dear Mom,\nYou mean the world to me 💕",
                  font=("Arial", 16),
                  bg="#ffccdd", fg="#5a189a",
                  justify=CENTER)
msg_label.place(x=170, y=100)

# Surprise text
surprise_label = Label(root, text="",
                       font=("Arial", 14, "bold"),
                       bg="#ffccdd", fg="#ff006e")
surprise_label.place(x=200, y=200)

# Hearts list for animation
hearts = []

def create_hearts():
    x = random.randint(50, 650)
    heart = canvas.create_text(x, 0, text="💖", font=("Arial", 18))
    speed = random.randint(2, 6)
    hearts.append([heart, speed])
    root.after(300, create_hearts)

def animate():
    for h in hearts:
        canvas.move(h[0], 0, h[1])
        pos = canvas.coords(h[0])
        if pos[1] > 500:
            canvas.coords(h[0], random.randint(50, 650), 0)
    root.after(50, animate)

# Surprise button action
def surprise():
    msg_label.config(text=random.choice(messages))
    surprise_label.config(text="💌 Sending unlimited hugs to Mom 🤗")

    # screen flash effect
    colors = ["#ffccdd", "#ffd6e0", "#ffc2d1", "#ffe0f0"]
    root.config(bg=random.choice(colors))
    canvas.config(bg=root["bg"])

# Button
btn = Button(root, text="Tap for Magic 💝",
             font=("Arial", 14, "bold"),
             bg="#ff4d6d", fg="white",
             command=surprise)
btn.place(x=270, y=300)

# Footer
footer = Label(root, text="Made by Hozaifa ❤️",
               font=("Arial", 10),
               bg="#ffccdd", fg="gray")
footer.place(x=280, y=460)

# start animation
create_hearts()
animate()

root.mainloop()