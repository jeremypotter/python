from random import random

while True:
	question = raw_input()
	if random()<0.6:
		print "You said '" + question + "'	"
	else:
		print "I forgot the answer to that!"