import turtle

def GoUp():
    turtle.stamp()
    turtle.setheading(90)
    turtle.forward(50)
 


def GoRight():
    turtle.stamp()
    turtle.setheading(0)
    turtle.forward(50)


def GoDown():
    turtle.stamp()
    turtle.setheading(270)
    turtle.forward(50)
 

def GoLeft():
    turtle.stamp()
    turtle.setheading(180)
    turtle.forward(50)



turtle.shape('turtle')

turtle.onkey(GoUp,'w')

turtle.onkey(GoRight,'d')

turtle.onkey(GoDown,'s')

turtle.onkey(GoLeft,'a')

turtle.listen()
