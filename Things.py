while True:
	A = raw_input("Username: ").upper()
	usernames = []
	passwords = []
	hints = []
	if A not in usernames:
		usernames.append(A)
		print "Welcome!"
		print "Please make an account!"
		B = raw_input("Username: ")
		new_password = raw_input("Password: ")
		passwords.append(new_password)
		F = raw_input("Password hint (optional): ")
		hints.append(F)
	else:
		index = usernames.index(A)
		C = raw_input("Password: ")
		if C == passwords[index]:
			print "Welcome back, " + A
			break
		else:
			print "Try again.(Password hint: " + hints[index] + ")"
			
	