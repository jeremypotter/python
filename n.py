import turtle



seed="SLSRSRSLS"
bob=turtle.Turtle()
bob.speed(0)
bob.up()
bob.goto(-225,0)
bob.down()
fractal=seed
fractal=fractal.replace("S",seed)
fractal=fractal.replace("S",seed)
fractal=fractal.replace("S",seed)
for letter in fractal:
        if letter=="S":
            bob.forward(450.0/27)
        elif letter=="R":
            bob.right(90)
        elif letter=="L":
            bob.left(90)

