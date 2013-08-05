import getpass
import random
import readline
from getch import getch


def player_sight_range():
	player_x,player_y = start_point
	for y in range(player_y-2,player_y+2):
		for x in range(player_x-2,player_x+2):
			found_item = item_at((x,y))
			if found_item:
				print "You can see a " + found_item.type + " at " + str(x) + "," + str(y) + "."








class JWoraldItem():

	def __init__(self, type):
		self.type = type


# Function that returns an item if it is as the location
def item_at(location):
	for item in items:
		if item.location == location:
			return item



print "Jworald Software"
print "Command Line Version"
print "Code and ideas by Jeremy Potter"
print "Code assistant Francis Potter"
print
print "Please name your character."
player_name = raw_input()


# Build the world and place the character. Loop so if the character shows up dead, we can start over.

item_at_start_point = True
while item_at_start_point:
	print
	print "Press enter to generate a world."
	enter = getpass.getpass("")
	start_point = (random.randint(1,20),random.randint(1,20))
	print player_name + " is at " + str(start_point)
	item_types_string = "rock,tree,bush,bird,plant"
	item_types = item_types_string.split(',')
	items = []
	for item_type in item_types:
		how_many = random.randint(1,5)
		for item_count in range(1,how_many):
			item = JWoraldItem(item_type)
			item.location = ( random.randint(1,20), random.randint(1,20) )
			items.append(item)

	item_at_start_point = item_at(start_point)
	if item_at_start_point:
		print "You spawned inside a " + item_at_start_point.type + "."
		print "You died."

# Check the objects and give the player the next step.

player_sight_range()
print "Move by pressing M and check your inventory by pressing I."
command_input = getch()
if command_input == "M" or "m":
	print "Use WASD keys to move."
	move_to_input = getch()
	if move_to_input == "W" or "w":
		old_x,old_y = start_point
		new_x = old_x
		new_y = old_y-1
		start_point = (new_x,new_y)
		print "Now you are at " + str(start_point) + "."
		player_sight_range()


