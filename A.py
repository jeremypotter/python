#Very complicated coding!
#By Jeremy, with help by his dad!
import time
import random
import sys
import readline
import subprocess
import os
import turtle
import math
import getpass
import games

def inbox():
	message_list = user[2]
	if len(message_list) > 0:
		print "Inbox:"
		for message_dict in message_list:
			sender = message_dict['user']
			message = message_dict['message']
			print sender + ' said: "' + message + '"' 




def send_message():
	print "Who do you want to send a message to?"
	recipient_name = raw_input().upper()
	if recipient_name in users.keys():
		recipient = users[recipient_name]
		print "Enter the message below"
		message = raw_input()
		message_dict = {'user':username,'message':message}
		recipient[2].append(message_dict)
		print "Your message has been sent!"
	else:
		print "There is no user with that name."
	

#stopwatch
def stopwatch():
	start_time = time.time()
	timed = raw_input()
	elapsed_time = int(time.time() - start_time)
	print "That took " + str(elapsed_time) + " seconds."
	if elapsed_time == "30":
		print "That took half a minute."
	if elapsed_time == "60":
		print "That took one minute."
	if elapsed_time > "60":
		print "That took " + str(elapsed_time) + " seconds. That's more than a minute!"	
	

#timer
def timer():
	timertime = raw_input("How many seconds?	")
	int_a = int(timertime)
	starttime = time.time()
	endtime = starttime +   int_a
	while time.time() < endtime:
		pass
	filename = "sound.wav"
	subprocess.call(["afplay",filename])
	filename = "sound.wav"
	subprocess.call(["afplay",filename]) 
	filename = "sound.wav"
	subprocess.call(["afplay",filename])
	print



def leftandforward():
	turt.left(90)
	turt.forward(200)
	

def draw_graphics():
	screen = turtle.Screen()
	screen.bgcolor("lightgreen")

	turt = turtle.Turtle()
	turt.color("purple")
	turt.pensize(4)
	turt.speed(2)

	turtle.write("is the Key to the World", font = ("Zapfino",25,"normal"))
	time.sleep(1)

	turt.penup()
	turt.goto(-435,360)
	turt.pendown()
	turt.right(90)
	turt.forward(200)
	leftandforward()
	turt.penup()
	leftandforward()
	turt.right(90)
	turt.forward(20)
	turt.right(90)
	turt.pendown()
	turt.forward(200)
	leftandforward()
	leftandforward()
	leftandforward()
	turt.penup()
	turt.left(180)
	turt.forward(220)
	
	# V
	angle = math.degrees(math.atan(0.5))
	length = math.sqrt(200**2+100**2)
	turt.right(90.0-angle)
	turt.pendown()
	turt.forward(length)
	turt.left(180.0-2*angle)
	turt.forward(length)
	turt.penup()
	turt.right(90-angle)
	
	
	turt.forward(20)
	turt.right(90)
	turt.pendown()
	turt.forward(200)
	turt.left(180)
	turt.forward(200)
	turt.right(90)
	turt.forward(200)
	turt.right(90)
	turt.penup()
	turt.forward(100)
	turt.right(90)
	turt.pendown()
	turt.forward(200)
	turt.left(90)
	turt.forward(100)
	leftandforward()

	filename = "Love.wav"
	subprocess.call(["afplay",filename])

	turt.getscreen()._root.mainloop()
	



# Get a command from the user and implement it

command_dict = {'STOPWATCH':stopwatch,"TIMER":timer,"GAME":games.game,"MESSAGE":draw_graphics,"SEND":send_message,"INBOX":inbox}

def do_commands():
	print "Type 'help' to see a list of the available commands."
	anything = raw_input().upper()
	while "EXIT" not in anything:
		
		if anything in command_dict.keys():
			function = command_dict[anything]
			function()

		if "RANDOM" and "NUMBER" in anything:
			X = random.randint(1,sys.maxint)
			print X

		if "RANDOM" and "LETTER" in anything:
			alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
			Y = random.randint(0,25)
			print alphabet[Y]

		if "HELP" in anything:
			print
			print "COMMANDS"
			print "[stopwatch]: Times how long things take!"
			print "[exit]: Log out!"
			print "[random letter]: Just like the name!"
			print "[random number]: Just like the name!"
			print "[timer]: Do things in a certain time!"
			print "[game]: Play a custom keyboard game!"
			print "[message]: Discover a secret message!"
			print "[send]: Send a message to another player!"
		
		anything = raw_input().upper()
	



#Main program
if os.path.isfile("save_game.txt"):
  file = open("save_game.txt","r")
  users_text = file.read()
  users = eval(users_text)
  file.close()
else:
  users = {}


print "Welcome to the JeremyWorld!"
while True:  # More than one person can log in
	username = raw_input("Username: ").upper()
	if username in users.keys():
		user = users[username]
		while True:
			password = getpass.getpass("Password: ")
			if password == user[0]:
				print "Welcome back, " + username.title() + "!" 
				message_list = user[2]
				if len(message_list) > 0:
					print "You have a new message!"
					for message_dict in message_list:
						sender = message_dict['user']
						message = message_dict['message']
						print sender + ' said: "' + message + '"'
				do_commands()
				print "Goodbye, " + username.title() + "."
				file = open("save_game.txt","w")
				file.write(str(users))
				file.close
				print
				print
				break
			else:
				print "Password hint is '" + user[1] + "'"
	else:
		print "Create an account!"
		new_username = raw_input("Username: ")
		new_password = raw_input("Password: ")
		new_hint = raw_input ("Password hint: ")	
		users[new_username.upper()] = [new_password,new_hint,[]]
		print "Congratulations, " + new_username + "! Now log in to go to your page."
