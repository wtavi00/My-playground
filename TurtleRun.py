import turtle # allows us to use the turtles library
# Cercle over rectangle
wn = turtle.Screen() # creates a graphics window
wn.setup(540,508)# set window dimension

circle_rad=50 # setthe radius
rectangle_width=150 #set the width
rectangle_height=80 #set the height

alex = turtle.Turtle() # create a turtle named alex
alex.shape("turtle") # alex looks like a turtle
alex.color('red') # alex has a color
alex.circle(circle_rad)
alex.backward(rectangle_width/2)
alex.forward(rectangle_width)
alex.right(90)
alex.forward(rectangle_height)
alex.right(90)
alex.forward(rectangle_width)
alex.right(90)
alex.forward(rectangle_height)

import turtle # Turtle Drawing Cercle inside of a rectangle
wn = turtle.Screen()        # creates a graphics window
wn.setup(540,508)           # set window dimension

alex = turtle.Turtle()      # create a turtle named alex
alex.shape("turtle")        # alex looks like a turtle
alex.color('red')           # alex has a color

'''
alex.circle(50)              # draws a circle of radius 50
alex.backward(50)            # alex moves 50 positions backward
alex.forward(50)             # alex moves 50 positions forward
alex.right(60)               # alex turns 60 degrees right
alex.left(60)                # alex turns 60 degrees left
'''
alex.penup()
alex.goto(0,-50)
alex.pendown()
alex.circle(50)

alex.penup()
alex.goto(-100, -50)  # Start at bottom left of the rectangle
alex.pendown()

for _ in  range(2):
    alex.forward(200)  # Draw the width
    alex.left(90)
    alex.forward(100)  # Draw the height
    alex.left(90)



# Turtle write hello
import turtle
wn = turtle.Screen()        # creates a graphics window
wn.setup(540,508)           # set window dimension

alex = turtle.Turtle()      # create a turtle named alex
alex.shape("turtle")        # alex looks like a turtle
alex.color("blue")          # alex has a color


alex.backward(50)            # alex moves 50 positions backward
alex.forward(100)             # alex moves 50 positions forward
alex.right(60)               # alex turns 60 degrees right
alex.left(60)                # alex turns 60 degrees left
alex.write("Hello This is Turtle. I'm going right")          # alex says "Hello"


destination = "south"  # Can be "north", "south", "east", or "west"

# Move alex to the specified destination
if destination == "north":
    alex.setheading(90)      # Point to the north (upwards)
    alex.forward(100)        # Move forward 100 units
elif destination == "south":
    alex.setheading(270)     # Point to the south (downwards)
    alex.forward(100)        # Move forward 100 units
elif destination == "east":
    alex.setheading(0)       # Point to the east (right)
    alex.forward(100)        # Move forward 100 units
elif destination == "west":
    alex.setheading(180)     # Point to the west (left)
    alex.forward(100) 
wn.mainloop()   

turtle.done()
