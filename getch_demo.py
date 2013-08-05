from getch import getch

def go_north():
    print "Going North!"

def go_south():
    print "Going South!"

COMMANDS = {'N':go_north,'S':go_south}

print "Choose a command -- North South East West: ",
char = getch().upper()
print char
if COMMANDS.has_key(char):
    function = COMMANDS[char]
    function()
else:
    print "Unknown command"
