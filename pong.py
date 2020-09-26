# Pong in python 3
# By Scott

import turtle
import os

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolour("Black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.colour("white")
