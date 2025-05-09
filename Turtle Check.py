import turtle
turtle.bgcolor('white')
turtle.speed(100000)
turtle.color('red', 'yellow')
turtle.begin_fill()
i = 1
while True:
    for j in range(20):
        turtle.forward(200)
        turtle.left(170)
    if i == 20:
        break
    i += 1
    turtle.forward(400)
turtle.end_fill()
turtle.hideturtle()
turtle.done()
