import turtle
import random

# Color palette from the extracted colors
color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50),
              (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20),
              (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35),
              (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158),
              (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74),
              (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102),
              (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

# Set up the turtle
turtle.colormode(255)  # Use RGB colors
t = turtle.Turtle()
t.speed("fastest")
t.penup()
t.hideturtle()

# Set starting position
t.setheading(225)
t.forward(300)
t.setheading(0)

# Number of dots and spacing
num_dots = 100
dot_size = 20
spacing = 50

# Draw Hirst-style painting
for dot_count in range(1, num_dots + 1):
    t.dot(dot_size, random.choice(color_list))  # Draw a dot with a random color
    t.forward(spacing)  # Move forward

    # Move to a new row after every 10 dots
    if dot_count % 10 == 0:
        t.setheading(90)
        t.forward(spacing)
        t.setheading(180)
        t.forward(spacing * 10)
        t.setheading(0)

# Keep the window open
turtle.done()
