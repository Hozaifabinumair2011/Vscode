import turtle
screen = turtle.Screen()
screen.bgcolor("black")
t = turtle.Turtle()
t.color("Green")
t.fillcolor("light green")
t.speed(1)
for i in range(3):
    t.forward(100)
    t.left(120)
t.hideturtle()
turtle.done()