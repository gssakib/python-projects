import ex25

from sys import argv



script, name, pas = argv

if ((name == "buterfly")or (name== "seeker") or (name == "da-vinci"))  and pas == ('dfort360'):
	print "Welcome to the path of illumination. There will be a set of riddles and depending on the answers and the path you choose, you will be illuminated...."
	print "Select the path from trinity....Omne trium perfectum.....The chances will decide the fate, but the tribus > unum > duo"
	path_1 = raw_input(">>>>>>>>")
	
	if path_1 == "3":
		print"Well done....still a long way to go. continue but make sure to get your feet a pair of companions"
		print "What has a tongue, cannot walk, but gets around a lot?"
		path_2 = raw_input(">>>>>>>>")
		if path_2 == "shoe":
			print "Congrats! Your are only a step away from illumination, or shall I say two cold steps..."
			print "You walk one mile south, one mile west, and one mile north. You end up exactly where you started. Where are you?"
			path_3 = raw_input(">>>>>>>>>")
			if path_3 == "North Pole" or path_3 == "South Pole":
				print"You have reched the end of illumination........."
				print"..............................................."
				happy = raw_input("What makes you happy and you would do it if this was the last day you are living?     ")
				print"The meaning of life is 42 and you should do %s" % happy
				print "You have now been illuminated........"
				
			else:
				print "Sorry, you are not one of us and you dont deserve illumination."
		else:
			print "Sorry, you are not one of us and you dont deserve illumination."
		
	
	
		
	elif path_1 == "2":
		print "Sorry, you are not one of us and you dont deserve illumination."

	else :
		print "Sorry, you are not one of us and you dont deserve illumination."
	
else:
	print "Sorry, you are not one of us and you dont deserve illumination."	

