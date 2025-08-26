"""
Module: purple_america

Program for visualizing election results in interesting ways.

Authors:
1) Name - USD Email Address
2) Name - USD Email Address
"""

import turtle

def draw_subregion(my_turtle, polygon_points):
    """
    Draws a polygonal subregion.

    Parameters:
    my_turtle (type: Turtle) - The turtle that will do the drawing.
    polygon_points (type: List) - List of tuples of the coordinates of the
      polygonal region.

    Returns:
    None
    """

    pass  # replace this line with your implemenation


def draw_filled_subregion(my_turtle, polygon_points, style, votes):
    """ Replace this with a docstring comment with the correct format. """

    pass  # replace this line with your implemenation


def read_subregion(geo_file):
    """ Replace this with a docstring comment with the correct format. """

    return None, None  # replace this line with your implemenation


def draw_map(geo_filename, election_results, style):
    """ Replace this with a docstring comment with the correct format. """

    pass  # replace this line with your implemenation


def get_election_results(election_filename):
    """ Replace this with a docstring comment with the correct format. """

    return None  # replace this line with your implemenation


def main():
    """
    Put your docstring comment here.
    """

    geo_filename = input("Enter the name of the geography file: ")
    election_filename = input("Enter the name of the election data file: ")

    valid_input = False
    while not valid_input:
        prompt_string = "What style of map would you like?\n"
        prompt_string += "Enter 1 for black & white.\n"
        prompt_string += "Enter 2 for red & blue.\n"
        prompt_string += "Enter 3 for purple.\n"
        style_selection = input(prompt_string)
        if style_selection == "1":
            valid_input = True
            style = "black-white"
        elif style_selection == "2":
            valid_input = True
            style = "red-blue"
        elif style_selection == "3":
            valid_input = True
            style = "purple"
        else:
            print("Invalid selection!")


    pass # Replace this line with your implementation of main


"""
WARNING: Do NOT modify anything below this point.
"""
if __name__ == "__main__":
    main()
