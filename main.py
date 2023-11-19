import turtle

def shapes():        
    screen.register_shape('rectangle', ((5, 30), (-5, 30), (-5, -30), (5, -30)))



def Rocket(position: tuple) -> object:        
    rocket = turtle.Turtle()
    rocket.left(90)
    rocket.shape('rectangle')
    rocket.color('white')
    rocket.penup()
    rocket.goto(position)
    return rocket



def midLine():
    line = turtle.Turtle()
    line.color('white')
    line.pencolor('white')
    line.hideturtle()
    line.penup()
    line.goto((0, 500))
    line.pendown()
    line.goto((0, -500))        


def rocket_right_up():
    rocket_right.fd(rocket_move)


def rocket_right_down():
    rocket_right.bk(rocket_move)


def rocket_left_up():
    rocket_left.fd(rocket_move)


def rocket_left_down():
    rocket_left.bk(rocket_move)


if __name__ == "__main__":
    
    # config screen
    screen = turtle.Screen()
    screen.setup(width=1.0, height=1.0, startx=None, starty=None)
    screen.bgcolor('black')
    screen.title('pong')
    shapes()
    midLine()

    # config rockets
    rocket_move = 100
    rocket_right = Rocket((850, 0))
    rocket_left = Rocket((-850, 0))

    # rockets move event
    screen.onkey(rocket_right_up, "Up")
    screen.onkey(rocket_right_down, "Down")
    
    screen.onkey(rocket_left_up, "w")
    screen.onkey(rocket_left_down, "s")
    
        
    screen.listen()

    
    
    turtle.mainloop()