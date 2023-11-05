import turtle

wn = turtle.Screen()

wn.bgcolor("white")


t = turtle.Turtle()

t.speed(1)  


for _ in range(4):
    t.forward(100)  
    t.right(90)  


t.penup()
t.goto(150, 0)  
t.pendown()

for _ in range(3):
    t.forward(100)  
    t.left(120)


wn.exitonclick()
