from turtle import *
color('red', 'yellow')
begin_fill()
angle = raw_input("Enter angle: ")
while True:
    forward(200)
    left(float(angle))
    if abs(pos()) < 1:
        break
end_fill()
done()

