# Mother's Day Wishing Card 💖
# Works in Google Colab, VS Code, Jupyter, etc.

from tkinter import *
from tkinter import messagebox
import random

# Window setup
root = Tk()
root.title("Happy Mother's Day")
root.geometry("700x500")
root.config(bg="#ffccdd")

# Random sweet messages
messages = [
    "Thank you for always being there 💖",
    "You are the best mom ever 🌸",
    "Your love makes everything better ✨",
    "Home feels warm because of you 🏡",
    "You are my real-life superhero 🦸‍♀️"
]

# Title
title = Label(
    root,
    text="🌷 Happy Mother's Day 🌷",
    font=("Comic Sans MS", 28, "bold"),
    bg="#ffccdd",
    fg="#d63384"
)
title.pack(pady=20)

# Main message
msg = Label(
    root,
    text="Dear Mom,\nThank you for everything you do.\nYou mean the world to me 💕",
    font=("Arial", 18),
    bg="#ffccdd",
    fg="#5a189a",
    justify=CENTER
)
msg.pack(pady=30)

# Changing surprise text
surprise_label = Label(
    root,
    text="",
    font=("Arial", 16, "bold"),
    bg="#ffccdd",
    fg="#ff006e"
)
surprise_label.pack(pady=20)

# Function for button
def surprise():
    surprise_label.config(text=random.choice(messages))
    messagebox.showinfo("Message 💌", "Sending virtual hugs to Mom 🤗")

# Button
btn = Button(
    root,
    text="Click for Surprise 💝",
    font=("Arial", 16, "bold"),
    bg="#ff4d6d",
    fg="white",
    padx=20,
    pady=10,
    command=surprise
)
btn.pack(pady=20)

# Footer
footer = Label(
    root,
    text="Made with Python ❤️",
    font=("Arial", 12),
    bg="#ffccdd",
    fg="gray"
)
footer.pack(side=BOTTOM, pady=10)

# Run app
root.mainloop()