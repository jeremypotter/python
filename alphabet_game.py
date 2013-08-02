import random

print "ALPHABET GAME!"
print "Type whatever you see!"
print
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
length = 3
while True:
	correct_answer = ""
	for position in range(length):
		letter_index = random.randint(0,25)
		correct_answer += alphabet[letter_index]
	print
	print "Try to type this: " + correct_answer
	while True:
		answer = raw_input("Your try: ")
		if answer == correct_answer:
			print "Great job!"
			length += 1
			break
		else:
			print "Try again"
