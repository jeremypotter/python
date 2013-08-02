#        key is username: value is password
#users = {"Jeremy": "creator001"}

# key is username: value is [password and hint]

users = {"JEREMY":["program_creator","What are you?"]}
print "Welcome to the JeremyWorld!"
while True:
	username = raw_input("Username: ").upper()
	if username in users.keys():
		user = users[username]
		while True:
			password = raw_input("Password:")
			if password == user[0]:
				print "Welcome back, " + username + "!" 
				break
			else:
				print "Password hint is '" + user[1] + "'"
	else:
		print "Create an account!"
		new_username = raw_input("Username: ")
		new_password = raw_input("Password: ")
		new_hint = raw_input ("Password hint: ")	
		users[new_username] = [new_password,new_hint]
		print "Congradulations, " + new_username + "! Now log in to go to your page."

#print """Log In. Type "new account" to create a new account.   """
#raw_input("")