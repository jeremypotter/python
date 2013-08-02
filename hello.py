import random

print "GUESS THE NUMBER 1-100 GAME"
low_score = 999999
while True:
    name = raw_input()
    x = random.randint(1,100)
    n = 0
    while True:
        guess_text = (raw_input("Guess the number: "))
        if not guess_text.isdigit():
            print "That is not a number. Try again!"
        else:
            guess = int(guess_text)
            n = n + 1
            if guess == x:
                print "Right! It took " + name + " " + str(n) + " guesses."
                if n<low_score:
                    low_score = n
                    print "YOU GOT THE NEW BEST SCORE!!"
                print "Try again"
                print
                break;
            if guess < x:
                print "Higher!"
            else:
                print "Lower!"