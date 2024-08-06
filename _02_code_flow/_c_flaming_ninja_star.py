import random
import turtle


# Returns a random color!
def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


def get_next_color(i):
    return colors[i % len(colors)]

# ====================== DO NOT EDIT THE CODE ABOVE ===========================


if __name__ == '__main__':
    window = turtle.Screen()
    colors = ['red', 'blue', 'green', 'yellow', 'orange']

    baseSize = 200          # the size of the black part of the star
    flameSize = 130         # the length of the flaming arms
    
    # Make a new turtle
    yuta=turtle.Turtle()
    # Make the turtle shape 'turtle', .shape('turtle')
    yuta.shape('turtle')
    # Set the turtle width to 2
    yuta.width(2)
    # Set the turtle speed to 0 (fastest)
    yuta.speed(0)
    # Use a for loop to repeat all of the code below ONE time (we will change
    # this later)
    for i in range(25):
        # Set the turtle .fillcolor() to orange
        yuta.fillcolor('orange')
        yuta.pencolor('black')
        # Call the turtle .begin_fill() function
        yuta.begin_fill()
        # TURN RIGHT     Turn the turtle 1/8 of a circle (hint: 360 degrees
        #                will turn a full circle)
        yuta.right(360/8)
        # DRAW           Move the turtle 64 pixels
        yuta.forward(64)
        # TURN LEFT      Turn the turtle 40 degrees to the LEFT. (Negative
        #                numbers will turn the turtle counter-clockwise.)
        yuta.left(40)
        # DRAW FLAME     Move the turtle the distance in the variable flameSize
        yuta.forward(flameSize)
        #                Turn the turtle to the right 170 degrees
        yuta.right(170)
        #         #                Move the turtle the distance in the variable flameSize (again)
        yuta.forward(flameSize)
        #  TURN RIGHT    Turn the turtle 62 degrees to the right
        yuta.right(62)
        #  DRAW          Move the turtle the distance in the variable baseSize
        yuta.forward(baseSize)
        # Call the turtle .end_fill() method
        yuta.end_fill()
    # Hide your turtle so you can see the pattern.
        yuta.hideturtle()

    # TEST   Run the program. Check that your shape is the same as the first
    #        picture in the recipe. This is one arm of the ninja star.

    # COLOR  Change the turtle's pen color so that the flame is a different
    #        color to the rest of the star. Run the program again. Check the
    #        second picture in the recipe.

    # LOOP   When you have one arm looking right, change your for loop to
    #        repeat 25 times.
    
    # call the turtle .done() method
    turtle.done()
