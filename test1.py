class Scene(object):
	def __init__ (self, name, sex, status, enter):
		self.name = name
		self.sex = sex
		self.status = status
		self.enter = enter
		
	
	def entrance(self):
	##based on the parameters we play out the derived scene
		print "Do you want to enter the next room ? Please type 1 if yes or 0 if no.."
			
		while True:
			try:
				self.opt = int(raw_input(">>>>>>>>>"))
				if self.opt == 1:
					self.status += 1
				else:
					print "sorry you die if you dont continue"
					term = Death(self.name,self.sex,self.status,self.enter)
					term.term()
					
				return  self.status, self.opt
			except ValueError:
				print("Please Enter a valid response.....")
			
			else:
				break
		

class Map(object):
	def __init__(self, scene):
		self.scene = scene
	
	def currnt_scene(self):
		return self.scene
		
	
			
			


class Engine(object):
	def __init__(self, scene_map, name, sex, status = -1, opt = 0 ):
		self.scene_map = scene_map
		self.name = name
		self.sex = sex
		self.status = status
		self.opt = opt
		
	def play(self):
		
		print "Type '1' to play. Type '0' to quit"
		while True:
			try:
				self.opt = int(raw_input(">>>>>>>>>"))
				if self.opt == 1:
					return self.name, self.sex, self.opt
				else:
					Death(self.name,self.sex,self.status,self.opt).term()
		
				
			except ValueError:
				print("Please Enter a valid response.....")
				
			else:
				quit()
		
class CentralCorridor(Scene):
	def __init__(self,name,sex, status, enter):
		
		super(CentralCorridor,self).__init__(name, sex, status, enter)
	
	
	def nar(self):
		if self.status == 0 and self.enter == 1:
			print "Welcome %s to the corridor. Be prepared to have an adventure of a lifetime" % (self.name)
			print "From far far across the horizon, comes the evil GOTHON with all him munchkins, ready to kill you!"
			print "you have to pick the funniest of the two following jokes to defeat him:.........."
			print "1: 'knock,knock whos there? nobody...'"
			print "2: 'what is 1 scared of 2. cuz 2,3,4.'"
			while True:
				try:
					self.opt = int(raw_input(">>>>>>>>>"))
					if self.opt == 1:
						print "wampapampam.....gothon dies...."
						print "Now. you get to proceed to the Bridge.."
						return self.name, self.sex
					else:
						Death(self.name,self.sex,self.status,self.enter).term()
		
				
				except ValueError:
					print("Please Enter a valid response.....")
				
				else:
					quit()
		
			
class Bridge(Scene):
	def __init__(self,name, sex, status, enter):
		super(Bridge,self).__init__(name, sex, status, enter )
	
	
	def nar(self):
		print "Welcome %s to the Bridge. What is that coming from the far horizon...looks very familiar..smells like evil..." % (self.name)			
		print "ITS GOTHON!!!!!!!...."
		print "Gothon is back and now you have to defeat him again to get the bomb by solving the following riddle..."
		print "You walk one mile south, one mile west, and one mile north. You end up exactly where you started. Where are you?"
		path = raw_input(">>>>>>>>")
		print path
		if path == "North Pole" or path == "South Pole":
			print "wampapampam.....gothon dies...."
			print "You place the bomb in gothon's ship where all his mucnkins reside...."
			print "Now. you get to proceed to the Armory where you can initiate bomb and the save the world!.."
			return self.name, self.sex
		else:	
			Death(self.name,self.sex,self.status,self.enter).term()
			

class Armory(Scene):
	def __init__(self,name, sex, status, enter):
		super(Armory,self).__init__(name, sex,status,enter)
		
		
	def nar(self):
		print "Now you are in the laser armory. To use the infamouse LASER..you must choose the correct following combinations."
		print "If you choose correctly you will have blown up the ship where the MUNCHKINS reside...if you dont however..."
		print "If you choose the wrong code, you will blow up the armory and yourself....."
		print "Good luck. ..let fate decide your fate,,, or......maybe theres ...someth..."
		print "TRIBUS-DUO-UNUM"
		print "The options are: "
		print "1. 123\n 2. 132\n 3. 111\n 4. 222 5. 321\n 6.34676543\n 7. sdfgdfs"
		print "Please type in the code or the associated number with the code.."
		while True:
				try:
					opt = int(raw_input(">>>>>>>>>"))
					if opt == 5 or opt == 321:
						print "KABOOOOOOOOOOOOOOOOOOOOOOOM!!!!!!!!!!!!!!!!!!"
						print "Gothon's ship explode and with that every last remaining munchkins."
						return self.name, self.sex
					else:
						print "KABOOOOOOOOOOOOOOOOOOOOOOOM"
						print "The armory explode......"
						Death(self.name,self.sex,self.status,self.enter).term()
		
				
				except ValueError:
					print("Please Enter a valid response.....")
				
				else:
					quit()	

class Escape(Scene):
	def __init__(self,name,sex,status,enter):
		super(Escape,self).__init__(name, sex,status,enter)
	
	def nar(self):
		print "%s, you are almost there....." %(self.name)
		print "You now need to escape,,,,,"
		print "The following are the choices. No clues, no trick, just plain old luck...."
		print "Type in the 1, or 2 or 3....One is supposed to make you free but 3 will definately not. Dont trust everything I say."
		print "For all you know I may the ghost of GOTHON trying to kill you,,,,,rmr walk the middle path..."
		while True:
				try:
					opt = int(raw_input(">>>>>>>>>"))
					if opt == 2:
						print "BUUUSHHHHH.....PSSSSSSSSSSSSSSS........../|\_/|\_/................"
						print "The door opens and.............."
						print "You win %s . Its the end. Good job, now getta outta here." %(self.name)
						return self.name, self.sex
					else:
						print "You were so close man....."
						
						Death(self.name,self.sex,self.status,self.enter).term()
		
				
				except ValueError:
					print("Please Enter a valid response.....")
				
				else:
					quit()	
			
			
			
			
			
			

class Death(Scene):
	def __init__(self, name, sex, status, enter):
		super(Death,self).__init__(name,sex,status,enter)
		
	def term(self):
		
		print"Sorry %s, you must die now because you my friend are a....... LOSER LLLUUSSSAAAA modafackaaa...."% (self.name)
		quit()


print"Welcome to Space Adventure!. We will need a few information to get started. Please input the following info......"
name = raw_input("Name:    ")
sex = raw_input("Sex:    ")
a_map = Map('central_corridor')
trajec = a_map.currnt_scene()
a_game = Engine(a_map,name,sex)
stat = a_game.play()	
in_corridor = CentralCorridor(stat[0],stat[1],0, stat[2])
c_corridor = in_corridor.nar()

## start of bridge scene
a_map = Map('the_bridge').currnt_scene()
a_scene = Scene(name, sex, 0, 0)
stat =  a_scene.entrance()
print stat
in_bridge = Bridge(name,sex,stat[0],stat[1])
c_bridge =  in_bridge.nar()
print c_bridge
# start of armory scene

a_map = Map('the_armory').currnt_scene()
a_scene = Scene(name, sex, stat[0], 0)
stat = a_scene.entrance()
print stat
in_armory = Armory(name,sex, stat[0],stat[1])
c_armory = in_armory.nar()
print c_bridge

# start of escape scene

a_map = Map('the_escape').currnt_scene()
a_scene = Scene(name, sex, stat[0], 0)
stat = a_scene.entrance()
print stat
in_escape =  Escape(name,sex, stat[0],stat[1])
c_escape = in_escape.nar()

print c_escape


