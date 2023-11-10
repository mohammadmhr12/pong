import turtle


def Display(color, height, width):
    display = turtle.Screen()
    display.bgcolor(color)
    display.screensize(height, width)
    turtle.mainloop()
    