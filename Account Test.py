import time
import random
import sys
import readline
import subprocess
import os
import turtle
import math
import getpass

#Main program
if os.path.isfile("save_game.txt"):
  file = open("save_game.txt","r")
  users_text = file.read()
  users = eval(users_text)
  file.close()
else:
  users = {}



def do_commands():
	#print "Do you want to send a message? (yes or no)"
	#yesorno = raw_input()
	while 'y' in yesorno.lower():
		print "Who do you want to send a message to?"
		recipient_name = raw_input().upper()
		if recipient_name in users.keys():
			recipient = users[recipient_name]
			print "Enter the message below"
			message = raw_input()
			message_dict = {'user':username,'message':message}
			recipient[2].append(message_dict)
		else:
			print "There is no user with that name."
		print "Do you want to send another message? (yes or no)"
		yesorno = raw_input()
		


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
					print "Inbox:"
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
		new_password = getpass.getpass("Password: ")
		new_hint = raw_input ("Password hint: ")	
		users[new_username.upper()] = [new_password,new_hint]
		print "Congratulations, " + new_username + "! Now log in to go to your page."
