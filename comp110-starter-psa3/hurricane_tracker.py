"""
Module: hurricane_tracker

Program to visualize the path of a Hurrican in the North Atlantic Basin.

Authors:
1) Jessica Cervantes - jessicacervantes@sandiego.edu
2) Cavin Nguyen - cavinnguyen@sandiego.edu
"""
import turtle


def screen_setup():
    """
    Creates the Turtle and the Screen with the map background
    and coordinate system set to match latitude and longitude.

    Returns:
    A list containing the turtle, the screen, and the background image.

    DO NOT MODIFY THIS FUNCTION IN ANY WAY!!!
    """

    import tkinter
    turtle.setup(965, 600)  # set size of window to size of map

    wn = turtle.Screen()
    wn.title("Hurricane Tracker")

    # kludge to get the map shown as a background image,
    # since wn.bgpic does not allow you to position the image
    canvas = wn.getcanvas()

    # set the coordinate system to match lat/long
    turtle.setworldcoordinates(-90, 0, -17.66, 45)

    map_bg_img = tkinter.PhotoImage(file="atlantic-basin.gif")

    # additional kludge for positioning the background image
    # when setworldcoordinates is used
    canvas.create_image(-1175, -580, anchor=tkinter.NW, image=map_bg_img)

    t = turtle.Turtle()
    wn.register_shape("hurricane.gif")
    t.shape("hurricane.gif")

    return [t, wn, map_bg_img]


# Define the get_category function here
def get_category(wind_speed):
    """
    Gets the wind speed of the hurricane and assigns its category.

    Parameters:
    wind_speed (integer): Wind speed integer.

    Returns:
    An integer to represent the category of the hurricane.
    """
    if wind_speed < 74:
        return 0
    elif wind_speed >= 74 and wind_speed <= 95:
        return 1
    elif wind_speed >= 96 and wind_speed <= 110:
        return 2
    elif wind_speed >= 111 and wind_speed <= 129:
        return 3
    elif wind_speed >= 130 and wind_speed <= 156:
        return 4
    else:
        return 5
    
def animate(csv_filename):
    """
    Animates the path of a hurricane.

    Parameters:
    csv_filename (string): Name of file containing hurricane data (CSV format).
    """

    # screen_setup returns a list of three items: the turtle to draw with, the
    # screen object for the window, and the background image of the window.
    # We only care about the turtle though.
    setup_data = screen_setup()

    # Give a name to the turtle that we were given back.
    hurricane_turtle = setup_data[0]


    # Your code to perform the animation will go after this line.
    # Longitude = x at index 2, Latitude = y at index 3, wind at index 4
    csv_file = open(csv_filename, "r")
    hurricane_turtle.penup()
    hurricane_turtle.hideturtle()
    for line in csv_file:
        split_line = line.split(',')
        category = get_category(int(split_line[4]))
        category_colors = ["white", "blue", "green", "yellow", "orange", "red"]
        line_thickness = [1, 2, 3, 4, 5, 6]
        hurricane_turtle.pencolor(category_colors[category])
        hurricane_turtle.pensize(line_thickness[category])
        hurricane_turtle.goto(float(split_line[3]), float(split_line[2]))
        hurricane_turtle.showturtle()
        hurricane_turtle.pendown()
        if category > 0:
            hurricane_turtle.write(category)
    csv_file.close()

        


    # DO NOT MODIFY THE FOLLOWING LINE! (It make sure the turtle window stays
    # open).
    turtle.done()


# Do not modify anything after this point.
if __name__ == "__main__":
    filename = input("Enter the name of the hurricane data file: ")
    animate(filename)
