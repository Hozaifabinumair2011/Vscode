import turtle
screen= turtle.Screen()
screen.bgcolor("black")
t = turtle.Turtle()
t.speed(1)
t.pencolor("red")
t.fillcolor("orange")
for i in range(2):
    t.forward(200)  
    t.left(90)  
    t.forward(100)  
    t.left(90)  
turtle.done()