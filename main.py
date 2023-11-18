import turtle

def shapes():    
    
    screen.register_shape('rectangle', ((30, 5), (-30, 5), (-30, -5), (30, -5)))



def Rocket(position: tuple) -> object:
        
    rocket = turtle.Turtle()
    rocket.shape('rectangle')
    rocket.color('white')
    rocket.penup()
    rocket.speed(0)
    rocket.goto(position)
    return rocket





if __name__ == "__main__":
    
    # config screen
    screen = turtle.Screen()
    screen.bgcolor('black')
    shapes()

    # config rockets
    rocket1 = Rocket((400, 0))
    rocket2 = Rocket((-400, 0))


turtle.mainloop()