"""
Auther: Bryan Ward



"""
from graphics import *
from time import clock
from random import seed, randint
from re import split

window = GraphWin("Mastermind", 360, 700,)


g_window_width = 360
g_window_height = 700

leftmost_x = 50
palette_y = g_window_height - 50


circle_radius = 20
circle_diameter = 2 * circle_radius
h_circle_spacing = 5
v_circle_spacing = 10

exit_x = 10 + circle_radius
exit_y = 30

state_x = g_window_width - circle_radius
state_y = exit_y
circle_width = 1

secret_code_x = exit_x
secret_code_y = exit_y

guess_y = palette_y - 100
guess_x = leftmost_x + circle_radius + h_circle_spacing

feedback_circle_radius = 5
feedback_x = leftmost_x + 5 * circle_radius * 2 + 4 * h_circle_spacing + feedback_circle_radius
feedback_y = guess_y + circle_radius - feedback_circle_radius
feedback_h_spacing = 20
feedback_v_spacing = 20

secret_code_x = guess_x
secret_code_y = 150


seed(clock())

palette_colors = ['green', 'orange', 'darkblue', 'yellow', 'darkred', 'lightblue']
num_palette_colors = len(palette_colors)


def create_circle(center_x, center_y, radius):
    # Using the (center_x, center_y) and radius, creates and returns a circle.
    # Return value: The circle that this function creates.
    point = Point(center_x,center_y)
    circle = Circle(point,radius)

    return circle
def create_exit_circle(center_x, center_y, radius):
    # Using the (center_x, center_y) and radius, creates a circle,
    # set its fill-color to red, and returns it.

    circle = create_circle(exit_x,exit_y,circle_radius)
    circle.setFill('red')
    circle.draw(window)
    return circle


def create_state_circle(center_x, center_y, radius):

    # Using the (center_x, center_y) and radius, creates a circle, uses
    # white to fill it, and returns it.

    circle = create_circle(state_x,state_y,circle_radius)
    circle.setFill('white')
    circle.draw(window)
    return circle


def create_color_palette(left_circle_center_x, left_circle_center_y, radius, palette_colors):
    # "palette_colors" is a list of color-names. This function creates six
    # circles (call it "palette_circles") using the colors in
    # "palette_colors" and returns it. The color of the circle at
    # "palette_circles[0]" will be "palette_colors[0]" and its center will
    # be at (left_circle_center_x, left_circle_center_y).  The center of
    # the second circle will be at
    # (left_circle_center_x + circle_diameter + h_circle_spacing, left_circle_center_y)
    # and its color would be "palette_colors[1]". Note that
    # h_circle_spacing is a global variable.

    palette_circles = 6
    color_palette_circles = []
    for i in range (palette_circles):

        circle = create_circle(leftmost_x +circle_diameter * i,palette_y,circle_radius)
        circle.setFill(palette_colors[i])
        circle.draw(window)
        color_palette_circles.append(circle)
    return color_palette_circles


def create_skel_circle(left_circle_center_x, left_circle_center_y, radius):
     # This function creates a list of four circles in white color and returns it.
     # The center of the first circle on this list is at (left_circle_center_x, left_circle_center_
     for i in range (4):
         circle = create_circle(guess_x + circle_diameter * i ,guess_y,circle_radius)
         circle.setFill('white')
         circle.draw(window)
     return


def create_secret_code_colors(palette_colors):
     # The function uses "palette_colors" to randomly select four
     # colors to be used as the secret code. The colors are stored in a list
     # which the function returns.
     color_palette = []
     for i in range (4):
        random_color = palette_colors[randint(0,num_palette_colors-1)]
        color_palette.append(random_color)

     return color_palette


def create_secret_code_circles(left_circle_center_x, left_circle_center_y, radius, secret_code):
     # The function creates a list of four circles using the colors in
     # secret_code_colors. The color of the first circle is "secret_code_color[0]"
     # and its center is at (left_circle_center_x, left_circle_center_y).

    secret_code_circles = []
    for i in range (4):
        circle = create_circle(secret_code_x + circle_diameter * i,secret_code_y,circle_radius)
        circle.setFill(secret_code[i])
        secret_code_circles.append(circle)
        circle.draw(window)


def main():
    # some code here
    left_circle_center_x = leftmost_x
    left_circle_center_y = palette_y
    radius = circle_radius
    secret_code = create_secret_code_colors(palette_colors)

    create_color_palette(left_circle_center_x, left_circle_center_y,radius,palette_colors)
    create_exit_circle(exit_x, exit_y, radius)
    create_state_circle(state_x, state_y, radius)
    create_skel_circle(guess_x,guess_y,radius)
    create_secret_code_circles(secret_code_x,secret_code_y,radius,secret_code)



    #print(create_secret_code_circles)
    # perhpas more code here...
   # mouse_click = window.getMouse()
   # if is_click_in_circle(mouse_click, exit_circle):
    window.getMouse()
    window.close()

    #return         # return from "main" will terminate the program.
    #elif # the rest of the condition here.
           # the rest of the code here...
    #num_palette_colors = len(palette_colors)
main()
