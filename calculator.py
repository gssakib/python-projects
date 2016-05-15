from sys import argv 

script , int_file, rslt_file, usr_name, pas = argv
#defining a function to read input from external files
def read_integers(int_file):
	with open(int_file) as f:
		return map(int,f)



if pas == 'dfort360' :
	print ("Welcome %r!. Here are the operations that you can perform: Add-1 Subtract-2, Multiply-3, Divide-4.")
	opr = raw_input(" what would you like to do today ?:   ") 
	out_file = open(rslt_file, 'w')
	if int(opr) == 1 :
		print"Performing Operation......"
		in_file = open(int_file, 'r')
		num_1 = 
		num_2 = 
		rslt = num_1 + num_2
	elif int(opr) == 2 :
		print"Performing Operation......"
		in_file = open(int_file, 'r')
		num_1 = 
		num_2 = 
		rslt = num_1 - num_2
	elif int(opr) == 3:
		print"Performing Operation......"
		in_file = open(int_file, 'r')
		num_1 = 
		num_2 = 
		rslt = num_1 * num_2
	elif int(opr) == 4:
		print"Performing Operation......"
		in_file = open(int_file, 'r')
		num_1 = 
		num_2 = 
		rslt = num_1 / num_2
	out_file.write(rslt)
	out_file.close()
	in_file.close()
		
		
else :
	print"Wrong pass! Please try again!"

		


	
	
	
	
	
		
	
	
	