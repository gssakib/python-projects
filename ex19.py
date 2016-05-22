def root(a,b) :
	return a**b 
	
def cheese_and_crackers(cheese_count, boxes_of_crackers): # defining the fuction 
	print "You have %r cheese !" % cheese_count #associating first arg 
	print "You have %r boxes of crackers!" % boxes_of_crackers #associating first arg 
	print "Man that's enough for a party!" #normal print
	print "the root of amount_of_cheese: %r amount_of_crackers: %r" %(root(cheese_count,0.5),root(boxes_of_crackers,0.5))
	print "Get a blanket. \n" 
	

print "We can just give the fuction numbers directly: "
cheese_and_crackers(20,30) #running function with only values

print "OR, we can just give the fucntion from our script :"
amount_of_cheese = 10 
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese,amount_of_crackers) #running fuction with variable

print "We can even do math inside too: "
cheese_and_crackers(10 + 20, 5 + 6) #summing args

print "And we can combine the two, variables and math :"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000) #running fucntion with variables and  numbers

