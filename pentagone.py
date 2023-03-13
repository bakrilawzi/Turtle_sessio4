import random
from turtle import Turtle as t

ahmad  =  t()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
ahmad.pensize(15)
def draw_shape(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        ahmad.forward(100)
        ahmad.right(angle)

for i in range(3,10):

    ahmad.color(random.choice(colours))
    draw_shape(i)