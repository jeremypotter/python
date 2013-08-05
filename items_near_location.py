
def items_near_location(location, distance):
    location_x, location_y = location
    found_items = []
    for y in range (location_y-distance, location_y+distance):
        for x in rance (location_x-distance, location_x+distance):
            found_item = item_at((x,y))
            if found_item:
                found_items.append(found_item)
    return found_items


items_near_player = items_near_location(start_point, 4)
if len(items_near_player) > 0:
    for item in items_near_player:
        print "You see a " + item.type + " at %i, %i" % item.location
else:
    print "There are no items near you."
