name = 'Zed A. Shaw'
age = 35 
height = 74
weight = 180
eyes = 'Blue'
teeth = 'White'
# my_teeth = "White"
hair = 'Brown'
in_no_len = 1
in_no_mass = 1
in_cm = in_no_len * 2.54
lb_kg = in_no_mass * 0.45

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." %weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

print "If I add %d, %d, and %d I get %d." %(age, height,weight, age + height + weight)
 
print "The conversion factor converting from inches to centi-meter is 1 inch = %f centi-meter" % in_cm
print "The conversion factor converting from pound-mass to kilo-grams is 1 pound-mass = %f kilo-grams" % lb_kg