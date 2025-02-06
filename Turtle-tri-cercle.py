wn = turtle.Screen()    # creates a graphics window
wn.setup(500,500)       # set window dimension

alex = turtle.Turtle()  # create a turtle named alex
alex.shape("turtle")    # alex looks like a turtle


alex.color("green")
alex.right(60)
alex.left(60)
alex.circle(50)
#draws circles
for counter in range(1,4):
    alex.circle(20*counter)

alex.right(120)
alex.forward(0)
alex.pendown()

alex.color("blue")
alex.circle(50)
for counter in range(1,4):
    alex.circle(20*counter)

alex.right(120)
alex.forward(0)
alex.pendown()

alex.color("red")
alex.circle(50)
for counter in range(1,4):
    alex.circle(20*counter)

""" This program will creat 3 color cercle next to each other"""
    
alex.hideturtle() 
wn.mainloop()
