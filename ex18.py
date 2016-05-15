#this one is like the scripts with argv

def print_two(*args):
	arg1, arg2 = args
	
	print ("arg1: %r, arg2: %r")  % (arg1, arg2)

#variation

def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

	
def print_one(arg1):
	print "arg1: %r" %(arg1)
	
def print_none():
	print "got nothin...."
	


print_two("oscar","rat")
print_two_again("oscar", "rat")
print_one("gaz")
print_none()

