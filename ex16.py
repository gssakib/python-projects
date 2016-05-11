from sys import argv

script, filename = argv

print "We are going to erase %r. " % filename
print "If you dont want that, hit CTRL -C (^C). "
print "If you do want that, hit RETURN. "

raw_input("?")

print "Opening the file...."
target = open(filename, 'w')

print "Truncating the file.....Good Bye!"
target.truncate()

print "Now I am going to ask you for three lines. "

line1 = raw_input("line 1:  ")
line2 = raw_input("line 2:  ")
line3 = raw_input("line 3:  ")

print "I am going to write these to the file."

line = "This is my favorite 3 song: 1)%r  2)%r   3)%r" % (line1,line2,line3)
target.write(line)




print ("And finally we are closing the file....")
target.close()



