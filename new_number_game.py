import random
print "BASIC MATH GAME"
print "Solve the math problems!"
print
maximum_values = [10,20,30]
for maximum_value in maximum_values:
	a = random.randint(1,maximum_value)
	b = random.randint(1,maximum_value)
	correct_answer = a + b
	print
	print str(a) + " + " + str(b)
	while True:
		answer = raw_input("Your answer: ")
		if int(answer) == correct_answer:
			print "Right!"
			break
		else:
			print "Try again!"
