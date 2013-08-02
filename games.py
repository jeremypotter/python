import random
import readline
import time


def math_game():
	print "BASIC MATH GAME"
	print "Solve the addition problems!"
	print
	maximum_values = [10,20,30,40,50]
	for maximum_value in maximum_values:
		a = random.randint(1,maximum_value)
		b = random.randint(1,maximum_value)
		correct_answer = a + b
		print
		print str(a) + " + " + str(b)
		while True:
			answer = raw_input("Your answer: ")
			if answer.isdigit() and (int(answer) == correct_answer):
				print "Right!"
				break
			else:
				print "Try again!"

	print
	print

def warm_up():
	print "Let's warm up with some addition!"
	while True:
		answer = raw_input("1+1=")
		if answer == "2":
			print "Right! Let's do another one:"
			break
		else:
			print "Try again!"
	while True:
		answer2 = raw_input("9+5=")
		if answer2 == "14":
			print "Good Job!"
			break
		else:
			print "Try again"


def alphabet_game():
	print "ALPHABET GAME!"
	print "Type whatever you see!"
	print
	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	length = 3
	for x in range(5):

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
				print "Try again."
	print
	
	
def game():
	personal_best_times = {}
	best_time = 9999999
	best_time_person = ""
	warm_up()
	while True:
		print
		print "Let's do some mini games now!"
		print
		start_time = time.time()
		math_game()
		alphabet_game()
		elapsed_time = int(time.time() - start_time)
		print "You took " + str(elapsed_time) + " seconds!"
		if username not in personal_best_times.keys():
			personal_best_times[username] = elapsed_time
		else:
			print "Your personal best time was " + str(personal_best_times[username]) + " seconds."
			if elapsed_time < personal_best_times[username]:
				print "You beat your personal best time!"
				personal_best_times[username] = elapsed_time
		if best_time_person != "":
			print "The overall best time was " + str(best_time) + " seconds by " + best_time_person
		if elapsed_time < best_time:
			if best_time_person != "":
				print "You got the new best time!!"
			best_time_person = username
			best_time = elapsed_time
		print
		print "Do you want to try again?"
		try_again = raw_input().upper()
		while try_again not in ["YES","NO"]:
			print "Answer 'yes' or 'no' please"
			try_again = raw_input().upper()
		if try_again=="NO":
			print "Thanks for playing, " + username
			print
			break