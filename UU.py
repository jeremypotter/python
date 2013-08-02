import time

start_time = time.time()
print "Quick! We only have 20 seconds before the system fails!"
print "Help! Type some command words to stop the program!"
print "Type: stop_program"
stop_program = raw_input("///")
if stop_program == "stop_program":
	elapsed_time = int(time.time() - start_time)
	if elapsed_time < 20:
		print "Yes! You saved software land! Do you want to go to software land?"
		while True:
			SLR = raw_input().upper()
			if SLR not in ["YES","NO"]:
				print "What did you say?"
			if SLR == "NO":
				print "Okay, then. But software land is a great place!"
				break 
			if SLR == "YES":
				print "Okay, HERE WE GO!!!"
				break
		
		
		
	else:
		print "SYSTEM FAILED"
		print "fsdoyufwdorh2348up0mroeksvmfe-w0iodofdifoifodilzclc';v'"
		print ",;df/,x/sdl'fkfp;djfidjfidfjidfjdifjci;fjd;ofzj;fosd ivjepofijdfodffdsjcdo"
		print "foiuhdfonwcrimw,[fpdpdpdppdpdpdpdfdkf;'dkf;odmkodfp[okofikofvfvkffvfvfkjdoifjdpfvfsdo;fi;jf]]"
	
	
	
	
else:
	print "SYSTEM FAILED"
	print "fsdoyufwdorh2348up0mroeksvmfe-w0iodofdifoifodilzclc';v'"
	print ",;df/,x/sdl'fkfp;djfidjfidfjidfjdifjci;fjd;ofzj;fosd ivjepofijdfodffdsjcdo"
	print "foiuhdfonwcrimw,[fpdpdpdppdpdpdpdfdkf;'dkf;odmkodfp[okofikofvfvkffvfvfkjdoifjdpfvfsdo;fi;jf]]"