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

skel_circles = [0, 1, 2, 3]

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

dy = circle_diameter + v_circle_spacing

num_skel_circles = len(skel_circles)


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

    circle = create_circle(center_x,center_y,radius)
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
    """

    :rtype : object
    """
    for i in range (4):
        circle = create_circle(guess_x + circle_diameter * i ,guess_y,circle_radius)
        circle.setFill('white')
        circle.draw(window)


    return circle[i]


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

    for i in range (4):
     circle = create_circle(secret_code_x + circle_diameter * i,secret_code_y,circle_radius)
     circle.setFill(secret_code[i])
     circle.draw(window)

     return None
def create_and_display_final_text(final_text_x, final_text_y, text_to_use):
    """
    Creates a Text-box, sets its text to ‘‘text_to_use’’, its anchor-point
    at (final_text_x, final_text_y), and displays it in the window.
    text_to_use: the text for the Text-box to be created
    win: the graphics window into which the text should be displayed
    return value: None
    """


    center_point = Point(top_left_x + width / 2, top_left_y + height / 2)
    text = Text(center_point,item_name )
    text.setSize(12)

    text.setFill(text_color)
    text.draw(window)



def find_clicked_circle(click_point, list_of_circles):
    """
    Returns the index of the circle in "list_of_circles" that includes
    point, "click_point". If no circle in "list_of_circles" include "click_point",
    the function returns None.
    click_point: an instace of "Point"
    list_of_circles: a list of instances of "Circle"
    return value: the index of circle in "list_of_circles" that
    includes "click_point" or None.
    """
    for i in range(len(list_of_circles)):
        if(is_click_in_circle(click_point,list_of_circles[i])):
            return i
    return None




def is_click_in_circle(click_point, circle):
    """
    Returns True if point "click_point" is in circle "circle". Otherwise,
    it returns False.
    click_point: An instance of "Point"
    circle: An instance of "Circle"
    return value: returns True if "click_point" is anywhere in "circle".
                Otherwise, it returns False.
    """
    circle_center_point=circle.getCenter()
    a = circle_center_point.getX() - click_point.getX()
    b = circle_center_point.getX() - click_point.getY()
    if a * a + b * b < circle.getRadius() * circle.getRadius():
        return True
    else:
        return False



def move_circles_up(circle, dy):
    for i in range(len(circle)):
        circle[i].move(0, -dy)


    window.update()






def main():
    list_of_circles = []

    exit_circle = create_exit_circle(exit_x, exit_y, circle_radius)

    list_of_circles.append(exit_circle)
    state_circle = create_state_circle(state_x, state_y, circle_radius)

    list_of_circles.append(state_circle)


    palette_circles = create_color_palette(leftmost_x, palette_y, circle_radius, palette_colors)
    for i in range(num_palette_colors):

        list_of_circles.append(palette_circles[i])


    skel_circle = create_skel_circle(guess_x, guess_y, circle_radius)
    for i in range(num_skel_circles):
        skel_circle[i]
        list_of_circles.append(skel_circle[i])
    secret_code_circles = create_secret_code_circles(secret_code_x, secret_code_y, circle_radius, secret_code_colors)
    for i in range(4):
           secret_code_circles[i].draw(window)
    text_to_use = create_and_display_final_text(state_x / 2, state_y, 'Done')
    text_to_use.draw(window)
    num_guesses = 0
    exit_clicked = False
    color_chosen = 'white'
    while (num_guesses <= 8 and exit_clicked == False):
        count = 0
        while count < 4:
            mouse_click = window.getMouse()
            idx_of_clicked_circle = find_clicked_circle(mouse_click, list_of_circles)
            if idx_of_clicked_circle is not None:
                circle_clicked = list_of_circles[idx_of_clicked_circle]
                if circle_clicked == exit_circle:
                    exit_clicked = True
                    count = 4
                elif circle_clicked in palette_circles:
                    for i in range(len(palette_circles)):
                        if circle_clicked == palette_circles[i]:
                            color_chosen = palette_colors[i]
                    state_circle.setFill(color_chosen)
                else:
                    idx = find_clicked_circle(mouse_click, list_of_circles)
                    if idx is not None:
                        clicked_circle = list_of_circles[idx]
                        new_circle = clicked_circle.clone()
                        new_circle.setFill(color_chosen)
                        new_circle.draw(window)
                        count += 1
                        state_circle.setFill('white')
        move_circles_up(skel_circle, dy)




    window.close()




main()
