import getpass
import random
import readline
from getch import getch














# Function to check objects
def items_near_location(location, distance):
    location_x, location_y = location
    found_items = []
    for y in range (location_y-distance, location_y+distance):
        for x in range (location_x-distance, location_x+distance):
            found_item = item_at((x,y))
            if found_item:
                found_items.append(found_item)
    return found_items




		
			

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
player_name = raw_input(">>>")


# Build the world and place the character. Loop so if the character shows up dead, we can start over.

inventory = []
item_at_start_point = True
while item_at_start_point:
	print
	print "Press ENTER to generate a world."
	enter = getpass.getpass("")
	

	start_point = (random.randint(1,20),random.randint(1,20))
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

keep_playin = True
while keep_playin:
	print player_name + " is at " + str(start_point)	
	items_near_player = items_near_location(start_point, 4)
	items_next_to_player = items_near_location(start_point, 1)
	
	if len(items_near_player) > 0:
	    for item in items_near_player:
	        print "You see a " + item.type + " at %i, %i" % item.location
	else:
	    print "There are no items near you."
	print "Move with WASD, check your inventory by pressing I, and quit by pressing Q."
	command_input = getch().upper()
	if ord(command_input) == 27:
		keep_playin = False
	old_x,old_y = start_point
	if command_input == "W":
		new_x = old_x
		new_y = old_y-1
		start_point = (new_x,new_y)
	if command_input == "A":
		new_x = old_x-1
		new_y = old_y
		start_point = (new_x,new_y)
	if command_input == "S":
		new_x = old_x
		new_y = old_y+1
		start_point = (new_x,new_y)
	if command_input == "D":
		new_x = old_x+1
		new_y = old_y
		start_point = (new_x,new_y)
	if command_input == "I":
		for item in inventory:
			print "You have a " + item.type
		print "You have no other items in your inventory."
		exit_inventory = getpass.getpass("Press enter to continue.")
	if command_input == "Q":	
		print "Thank for playing!"
		keep_playin = False
