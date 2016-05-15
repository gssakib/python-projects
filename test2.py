from sys import argv 

script, int_file = argv




f = open(int_file)
f.seek(0)
num_1 = f.readline(3)
num_2 = f.readline(4)
reslt = num_1 + num_2

print reslt

	






