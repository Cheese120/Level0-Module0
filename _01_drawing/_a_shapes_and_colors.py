import turtle


window = turtle.Screen()
window.bgcolor('yellow')

# This code makes a new Turtle. Pick a new name for the turtle
yuta = turtle.Turtle()

# Make your turtle's shape 'turtle', .shape('turtle')
yuta.shape('turtle')
# Set your turtle's speed using .speed(2)
yuta.speed(10)
# Set your turtle's color using .color('green') and .pencolor('blue')
yuta.color('green')
yuta.pencolor('red')
# Move your turtle forward using .forward(100)
# TEST    Did your turtle move forward?
yuta.forward(100)
# Move your turtle left or right using .left(90) or .right(90)
yuta.left(90)
# Now put the forward and left/right code into a for loop to repeat 4 times.
# TEST    Did your turtle draw a square?
for i in range(4):
    yuta.forward(100)
    yuta.left(90)
# Move your turtle to a new place on the screen using .goto(x, y)
# x=0 and y=0 is the center of the screen
yuta.goto(-100,-150)
# Have your turtle draw a circle using .circle(radius, steps=30)
# TEST    Did your turtle draw a circle?
yuta.color('blue')
yuta.begin_fill()
yuta.circle(125, steps=30)
# Add color to your shape by adding .begin_fill() before drawing the circle
# and .end_fill() below
yuta.end_fill()
# Draw 3 more shapes with different fill colors!
yuta.goto(-200,250)
yuta.color('purple')
yuta.begin_fill()
for i in range(5):
    yuta.right(75)
    yuta.forward(50)
yuta.end_fill()
yuta.goto(250,-250)
yuta.color('red')
yuta.begin_fill()
for i in range(6):
    yuta.right(60)
    yuta.forward(100)
yuta.end_fill()
yuta.goto(200,200)
yuta.color('orange')
yuta.begin_fill()
for i in range(4):
    yuta.left(90)
    yuta.forward(200)
yuta.end_fill()
# ===================== DO NOT EDIT THE CODE BELOW ============================
turtle.done()
