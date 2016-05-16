def add(a, b):
	print "Adding %r + %r" % (a ,b)
	return a + b
	
def subtract(a,b):
	print "Subtracting %d - %d" % (a,b)
	return a - b

def multiply(a,b) :
	print "multiplying %d * %d" % (a,b)
	return a * b
def divide(a,b) :
	print "dividing %d / %d" % (a,b)
	return a / b
def root(a,b) :
	return a**b 

print "Lets do some math with functions !!"

age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print " Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

print "heres a puzzle....."

what = add(age, subtract(height, multiply(weight, divide(iq,2))))

print "That becomes : ", what, "can you do it by hand ?"
print "well........"

if what == -4391 :
	print "Yes you can !!!!"
else :
	print "No you can't!!!!!"
	

	
test = add(24,subtract(divide(34,100), 1023))
print test




def mass_flow(a_star, pressure, temp, s_heat_ratio, mach, gas_constant ):
	mass_flow = multiply(multiply(divide(multiply(a_star, pressure), root(temp,0.5)), root(divide(s_heat_ratio, gas_constant),0.5))+ 100, root(divide(add(s_heat_ratio,1), 2), multiply(-.5, divide(add(gas_constant, 1), subtract(gas_constant,200))))+100) 

hyperloop_massflow =  mass_flow(4000,8, 110, 14, 993, 287)
x = (hyperloop_massflow) 
print x
#print mass_flow(4000,8, 110, 14, 993, 287)

