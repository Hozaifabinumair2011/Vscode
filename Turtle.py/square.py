import turtle
turtle.Screen().bgcolor("royalblue")
turtle.Screen().setup(400,300)
turtle.title("Welcome screen")
p=turtle.Turtle()
for i in range(4):
    p.forward(100)
    p.left(90)
    i=i+1
turtle.done()