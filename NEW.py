
import os
import random

print "Hi, I'm Jereliza!"
while True:
	x = raw_input()
	if "hello" in x.lower():
		print "It's a nice day, isn't it!"
	if "problem" in x.lower():
		print "Tell me more..."
	
	
	else:
		a = random.randint(1,3)
		if a == 1:
			print "What did you say?"
		elif a == 2:
			print "Hmm..."
		elif a == 3:
			print "Can you describe that a little more clearly?"

