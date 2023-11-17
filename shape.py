import turtle

# create rectangle shape for Turtle
screen = turtle.Screen()

# add shape to screen
screen.register_shape('rectangle', ((30, 5), (-30, 5), (-30, -5), (30, -5)))


bob = turtle.Turtle()
bob.shape('rectangle')


turtle.mainloop()