print "How old are you (in years) ?",
age = raw_input()

height =  raw_input ("How tall are you (in ft) ?")
print "How much do you weigh (lbs) ?",
weight = raw_input()

n_1 = int(raw_input("Input first number:  "))
n_2 = int(raw_input("Input first number:  "))

sum = n_1 + n_2

print "So, you are %r years old, %r ft tall and %r lbs heavy." % (age, height, weight)

print "The sum of %r and %r is equal to %s" % (n_1, n_2, sum)