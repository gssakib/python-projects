from sys import argv

script, user_name, pas = argv
prompt = '>>>>>>>>  '

if pas == "dfort360" :
	print "Hi %s, I am the %s script." % (user_name, script)
	print "I would like to ask you a few questions."
	print "Do you like me %s?" % user_name
	likes = raw_input(prompt)

	print "where do you live %s?" % user_name
	lives = raw_input(prompt)

	print "What kind of computer do you have ?"
	computer = raw_input(prompt)

	print """
	Alright, so you said %r about liking me.
	You live in %s. Not sure where that is.
	And you have %s computer. Nice.
	""" % (likes, lives, computer)
else :
	print " Wrong pass-word. Please try to run the program again."

