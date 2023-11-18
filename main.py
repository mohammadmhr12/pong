import turtle

def shapes():    
    
    screen.register_shape('rectangle', ((30, 5), (-30, 5), (-30, -5), (30, -5)))



def Rocket(position: tuple) -> object:
        
    rocket = turtle.Turtle()
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



if __name__ == "__main__":
    
    # config screen
    screen = turtle.Screen()
    screen.setup(width=1.0, height=1.0, startx=None, starty=None)
    screen.bgcolor('black')
    screen.title('pong')
    shapes()
    midLine()

    # config rockets
    rocket_right = Rocket((850, 0))
    rocket_left = Rocket((-850, 0))


    turtle.mainloop()