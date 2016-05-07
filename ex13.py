from sys import argv
script , b_1, b_2 = argv
cnt = 1
while cnt > 0:

	if int(b_1) == 1 and int(b_2) == 0:
		no_1 = raw_input("Please enter first number:  ")
		no_2 = raw_input("Please enter second number:  ")
		reslt = int(no_1) + int(no_2)
		cnt = 0
	elif int(b_1) == 0 and int(b_2) == 1:
		no_1 = raw_input("Please enter first number:  ")
		no_2 = raw_input("Please enter second number:  ")
		reslt = int(no_1) * int(no_2)
		cnt = 0
	else:
		print("Please try to input correctly again ")
		
		

print ("The final result is:  %r  ") % reslt

