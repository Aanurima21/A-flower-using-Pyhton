import turtle
t=turtle.Turtle()
t.speed(0)

#Display changes
t.screen.bgcolor("black")
t.color("blue")

#Creating the flower
for i in range(100):
    t.circle(120-i,100)
    t.circle(30,90)
    t.circle(120-i,100)
    t.rt(10)

turtle.done()
