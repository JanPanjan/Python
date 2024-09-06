import turtle

bob = turtle.Turtle()
print(bob)

# dropnemo pen
bob.pd()

# naredimo kvadrat funkcijo
def kvadrat():
    for i in range(4):
        bob.forward(200)
        bob.left(90)

kvadrat()
turtle.mainloop()
