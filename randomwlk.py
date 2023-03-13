from turtle import Turtle as t
import random
han = t()
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0,90,180,270]
han.speed("fastest")
han.pensize(15)
for _ in range(300):
    han.color(random.choice(colours))
    han.forward(30)
    han.setheading(random.choice(directions))