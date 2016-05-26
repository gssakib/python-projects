ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that. "
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night","Song","Frisbee","Corns", "Banana","Girl","Boy"]

for num in range(0,(len(stuff)-2)):
	next_one = more_stuff.pop()
	print "Adding: ", next_one
	stuff.append(next_one)
	print "There are %d items now." % len(stuff)
	
print "There we go: ", stuff

print "Lets do some more things with stuff."

print stuff[1]
print stuff[-1]
print stuff.pop()
print ' '.join(stuff)
print '#'.join(stuff[3:5])

