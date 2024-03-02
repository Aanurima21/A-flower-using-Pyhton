import turtle
t=turtle.Turtle()
def flower():
    for i in range(20):
        t.lt(20)
        t.fd(100)
        t.lt(120)
        t.fd(100)  

def leaf():
    for i in range(1,20):
        t.fd(7*i)
        t.lt(180)
        t.fd(7*i)
        t.rt(175)
    for i in range(20,1,-1):
        t.fd(7*i-7)
        t.lt(180)
        t.fd(7*i-7)
        t.rt(175)

t.screen.bgcolor("black") #turning the screen black 
t.speed(9)
t.color("yellow")

#creating the flower first

flower()

#positioning the turtle to create the left leaf
t.rt(90)
t.penup()
t.fd(60)
t.pendown()
t.rt(60)
t.color("green")

#creating the left leaf

leaf()

#positioning the turtle to create the right leaf
t.lt(40)
t.penup()
t.fd(225)
t.pendown()
t.rt(140)

#creating the right leaf

leaf()
turtle.done()


