import turtle as t

t.bgcolor("black")
t.pencolor("red")
t.speed(100)
t.penup()
t.goto(0, 200)
t.pendown()

x=0
y=0

while True:
    t.forward(x)
    t.right(y)
    x += 3
    y += 1
    if y == 210:
        break
    t.hideturtle()
t.exitonclick()
t.done()