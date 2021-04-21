import turtle
from random import choice, randint
cho1 = ('red', 'green', 'blue')
while True:
    turtle.pencolor(choice(cho1))
    turtle.forward(randint(1, 200))
    turtle.right(randint(33,90))