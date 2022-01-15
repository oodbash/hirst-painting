import colorgram
import turtle
import random

number_of_colors = 10

colors = colorgram.extract('image.jpg',number_of_colors)

rgb_colors = []

for i in range(len(colors)):
    r = colors[i].rgb[0]
    g = colors[i].rgb[1]
    b = colors[i].rgb[2]
    color = (r,g,b)
    rgb_colors.append(color)

for c in rgb_colors:
    if (c[0] > 240) and (c[1] > 240) and (c[2] > 240):
        rgb_colors.remove(c)

helena = turtle.Turtle()
screen = turtle.Screen()
screen.colormode(255)

helena.penup()
# print(helena.heading())
# helena.right(180)

# print(helena.heading())
for x in range(10):
    for i in range(10):
        helena.pencolor(random.choice(rgb_colors))
        helena.dot(15)
        helena.forward(20)
    if helena.heading() == 0.0:
        helena.left(90)
        helena.forward(20)
        helena.left(90)
        helena.forward(20)
    else:
        helena.right(90)
        helena.forward(20)
        helena.right(90)
        helena.forward(20)


screen.exitonclick()

