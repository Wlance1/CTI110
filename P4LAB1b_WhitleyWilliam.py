import turtle


wn = turtle.Screen()

wn.bgcolor("white")


t = turtle.Turtle()

t.speed(1)  

t.color("blue") 

t.pensize(5)    


t.penup()

t.goto(-40, 0)  

t.setheading(250)

t.pendown()

t.forward(100)

t.right(140)

t.forward(50)

t.left(140)

t.forward(50)

t.right(140)

t.forward(100)


t.penup()

t.goto(90, 0)  

t.setheading(250)

t.pendown()

t.forward(100)

t.right(140)

t.forward(50)

t.left(140)

t.forward(50)

t.right(140)

t.forward(100)

t.hideturtle()  

wn.exitonclick()
