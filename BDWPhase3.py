"""
Auther: Bryan Ward



"""
from graphics import *
from time import clock
from random import seed, randint
from re import split
import random

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




palette_colors = ['green', 'orange', 'darkblue', 'yellow', 'darkred', 'lightblue']
num_palette_colors = len(palette_colors)


skel_circles = [0, 1, 2, 3]
num_skel_circles = len(skel_circles)
secret_code_colors = random.choice(palette_colors)
num_secret_code_circles = 4
circles = []

dy = circle_diameter + v_circle_spacing


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

        circle = create_circle(leftmost_x +(circle_diameter + h_circle_spacing)* i,palette_y,circle_radius)
        circle.setFill(palette_colors[i])
        circle.draw(window)
        color_palette_circles.append(circle)
    return color_palette_circles


def create_skel_circle(left_circle_center_x, left_circle_center_y, radius):
     # This function creates a list of four circles in white color and returns it.
     # The center of the first circle on this list is at (left_circle_center_x, left_circle_center_
     list_of_skel_circles = []

     for i in range (4):
         circle = create_circle(guess_x + (h_circle_spacing + circle_diameter) * i ,guess_y,circle_radius)
         circle.setFill('white')
         list_of_skel_circles.append(circle)
         circle.draw(window)
     return list_of_skel_circles


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
        circle = create_circle(secret_code_x + (circle_diameter + h_circle_spacing) * i,secret_code_y,circle_radius)
        circle.setFill(secret_code[i])
        secret_code_circles.append(circle)
        circle.draw(window)


    return secret_code_circles






def create_and_display_final_text(final_text_x, final_text_y, text_to_use):
    text_box_center_point = Point(final_text_x, final_text_y)
    text_box = Text(text_box_center_point,text_to_use)
    text_box.setSize(20)
    return text_box

"""
Creates a Text-box, sets its text to ``text_to_use'', its anchor-point
at (final_text_x, final_text_y), and displays it in the window.
text_to_use: the text for the Text-box to be created
win: the graphics window into which the text should be displayed
return value: None
"""



def find_clicked_circle(click_point, list_of_circles):
    for i in range(len(list_of_circles)):
        if is_click_in_circle(click_point,list_of_circles[i]):
            return i


    return None

"""
click_point: an instace of "Point"
list_of_circles: a list of instances of "Circle"
return value: the index of circle in "list_of_circles" that
includes "click_point" or None.
"""



def is_click_in_circle(click_point, circle):
    circle_center_point = circle.getCenter()
    a = circle_center_point.getX() - click_point.getX()
    b = circle_center_point.getY() - click_point.getY()
    if a * a + b * b < circle.getRadius() * circle.getRadius():

        return True
    else:
        return False

"""
Returns True if point "click_point" is in circle "circle". Otherwise,
it returns False.
click_point: An instance of "Point"
circle: An instance of "Circle"
return value: returns True if "click_point" is anywhere in "circle".
Otherwise, it returns False.
"""



def move_circles_up(circles, dy ):
    for i in range(len(circles)):
        circles[i].move(0, -dy)

    window.update()

def create_feedback_skel():
    """
    Creates four smaller circles such that when drawn, they form
    two rows each of which includes 2 circles.
    return value: a list of four circles
    """
    # Create a list for the feedback skeleton circles
    # Create a for loop whose range is 2
        # Create a for loop whose range is 2
            # Create a circle whose center point is i * feedback_x + feedback_h_circle_spacing, j * feedback_y + feedback_v_circle_spacing
            # Append this circle to the list you created
    # Return the feedback skeleton circles list

    FeedbackSkeletonCircles = []
    for i in range (2):
        for j in range(2):
            feedbackCircle = create_circle(feedback_x + i * feedback_h_spacing,feedback_y - j * feedback_v_spacing,feedback_circle_radius)
            FeedbackSkeletonCircles.append(feedbackCircle)

    return FeedbackSkeletonCircles

def create_feedback_circles(secret_code_colors, guess_code_colors, feedback_skel_circles):
    feedback_circles = []
    guess_color_used = [False, False, False, False]
    secret_color_used = [False, False, False, False]
    feedback_idx = 0
    for i in range(4):
        if secret_code_colors[i] == guess_code_colors[i]:
            guess_color_used[i] = secret_color_used[i] = True
            feedback_skel = feedback_skel_circles[feedback_idx].clone()
            feedback_idx += 1
            feedback_skel.setFill('red')
            feedback_circles.append(feedback_skel)


    for i in range(4):
        if not guess_color_used[i]:
            for j in range(4):
                if not secret_color_used[j] and secret_code_colors[j] == guess_code_colors[i]:
                    feedback_skel = feedback_skel_circles[feedback_idx].clone()
                    feedback_skel.setFill('white')
                    feedback_circles.append(feedback_skel)
                    feedback_idx += 1
                    secret_color_used[j] = True
                    break
    return feedback_circles

def guess_is_right(secret_code_colors, guess_colors):
    if len(secret_code_colors) == len(guess_colors):
        for i in range(len(secret_code_colors)):
            if guess_colors[i] != secret_code_colors[i]:
                return False
        return True
    return False

def main():
    # some code here

    radius = circle_radius
    secret_code_colors = create_secret_code_colors(palette_colors)

    exit_circle = create_exit_circle(exit_x, exit_y, circle_radius)
    state_circle = create_state_circle(state_x, state_y, circle_radius)
    state_circle.draw(window)
    skel_circles =  create_skel_circle(guess_x,guess_y,radius)

    create_secret_code_circles(secret_code_x,secret_code_y,radius,secret_code_colors)

    palette_circles = create_color_palette(leftmost_x, palette_y, circle_radius, palette_colors)




    num_guesses = 0
    # Create a variable that is set to the result of create_feedback_skel()
    feedback_skel_circles = create_feedback_skel()
    while (num_guesses < 8):
        count = 0
        # Create a list filled with four Nones for the user's guesses
        guessed_colors =[None, None, None, None]

        while count < 4:
            mouse_click = window.getMouse() # click for palette color
            exit_clicked = is_click_in_circle(mouse_click, exit_circle)
            if exit_clicked == True:
                    window.close()
                    return
            idx_of_clicked_circle = find_clicked_circle(mouse_click, palette_circles)


            if idx_of_clicked_circle is not None:




                color = palette_colors[idx_of_clicked_circle]
                state_circle.setFill(color)


                mouse_click = window.getMouse() # click for skeleton circle
                idx = find_clicked_circle(mouse_click, skel_circles)



                print(idx)

                if idx is not None:
                    clicked_circle = skel_circles[idx]
                    new_circle = clicked_circle.clone() # make a copy of it.
                    new_circle.setFill(color)
                    new_circle.draw(window)
                    state_circle.setFill('white')
                    guessed_colors[idx] = color

                    count += 1





                    # Place the user's color in guessed_colors[idx], this keeps track of the color and the exact position that the user
                    # placed it in the skeleton circles


        # Check to see if the user won the game using guess_is_right(secret_colors, guessed_colors)
        if guess_is_right(secret_code_colors, guessed_colors):
            text_to_use = create_and_display_final_text(state_x / 2, state_y, 'You Win!')
            text_to_use.draw(window)

            window.getMouse()
            window.close()
            return

                # If they are right get their next mouse click, close the window, and then end the game.
        # Otherwise
        else:
            feedback_circle = create_feedback_circles(secret_code_colors, guessed_colors, feedback_skel_circles)


            # Create a variable whose value is the result of create_feedback_circles(secret_colors, guessed_colors, feedback_skel_circles)
            # Create a for loop that draws that variable
            for i in range (len(feedback_circle)):

                feedback_circle[i].draw(window)



            

            move_circles_up(skel_circles,dy)









            move_circles_up(feedback_skel_circles,dy)




                # Move the skeleton circles up
        num_guesses += 1

    text_to_use = create_and_display_final_text(state_x / 2, state_y, 'Done')
    text_to_use.draw(window)
    window.getMouse()
    window.close()



    #print(create_secret_code_circles)
    # perhpas more code here...

   # if is_click_in_circle(mouse_click, exit_circle):



    #return         # return from "main" will terminate the program.
    #elif # the rest of the condition here.
           # the rest of the code here...
    #num_palette_colors = len(palette_colors)
main()
