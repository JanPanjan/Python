import turtle
import math

bob = turtle.Turtle()

# naredi funkcijo square, ki naredi square glede na lenght parameter in t ki je turtle
def square(t, lenght):
    """Tvoja želvica naredi lep kvadrat"""
    for i in range(4):
        t.forward(lenght)
        t.left(90)

# naredi poligon glede na n - število stranic
def polygon(t, lenght, n):
    """Tvoja želvica bo naredila lep pravilen poligon"""
    for i in range(n):
        t.forward(lenght)
        t.left(360/n)

def initCircle(t, radius):
    """Premakne želvico naprej, tako da naredi krog
    okoli svoje začetne točke"""
    t.forward(radius)
    t.left(90)

# naredi krog iz radiusa
def circle(t, radius):
    """Tvoja želvica naredi lep krog"""
    initCircle(t, radius)
    # obseg = 2 x pi x r
    # obseg delimo na 360 delov
    # vsako iteracijo se premakne za eno enoto
    obseg = 2 * math.pi * radius
    enota = obseg/360
    for i in range(360):
        t.forward(enota)
        t.left(1)

# circle, ki uporabi poligon
def modCircle(t, radius):
    """Circle, le da uporabimo poligon funkcijo"""
    t.forward(radius)
    t.left(90)

    # naprej mora it za enoto, tako kot prej
    obseg = 2 * math.pi * radius
    enota = obseg/360
    polygon(t, enota, 360)

# circle, le da nariše le določen del loka glede na angle
# 360 pomeni cel krog, 180 pomeni pol kroga, itd.
def arc(t, radius, angle):
    """Tvoja želvica naredi določen del kroga"""
    initCircle(t, radius)

    # kopirano iz circle()
    obseg = 2 * math.pi * radius
    enota = obseg/360
    for i in range(angle):
        t.forward(enota)
        t.left(1)

# klic
# square(bob, 120)
# polygon(bob, 120, 6)
# circle(bob, 200)
# modCircle(bob, 200)
arc(bob, 200, 180)

turtle.mainloop()
