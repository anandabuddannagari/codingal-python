import turtle

# create screen
screen = turtle.Screen()
screen.title("Dharani's Turtle Design")
screen.bgcolor("lightblue")   # change to any color you like

# create turtle
t = turtle.Turtle()
t.pensize(4)
t.pencolor("purple")
t.speed(3)

# draw square
t.fillcolor("pink")
t.begin_fill()

for _ in range(4):
    t.forward(150)
    t.right(90)

t.end_fill()

# keep window open
turtle.done()
