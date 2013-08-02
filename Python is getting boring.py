import random

rock = random.randint(1,10)
tree = random.randint(1,10)
start_point = random.randint(1,10)
while True:
	coordinates = int(raw_input("Enter the coordinates: "))
	if rock == coordinates:
		print "You found a rock!!!"
	if tree == coordinates:
		print "You found a tree!"