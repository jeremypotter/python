import random
from tuple_raw_input import tuple_raw_input

rock = (random.randint(1,10),random.randint(1,10))
tree = (random.randint(1,10),random.randint(1,10))
start_point = (random.randint(1,10),random.randint(1,10))
while True:
	coordinates = tuple_raw_input()
	if rock == coordinates:
		print "You found a rock!!!"
	if tree == coordinates:
		print "You found a tree!"