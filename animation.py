import turtle
import colorsys

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.speed(0)

n = 36
h = 0

for i in range(360):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    h += 1/n
    t.color(c)
    t.circle(150)
    t.right(10)

turtle.done()
