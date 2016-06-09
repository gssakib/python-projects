## base Scene class

class Scene(object):
	def __init__ (self, name, sex,status, enter)
		self.name = name
		
		
	
	
	def enter(self):
	##based on the parameters we play out the derived scene
		print "Do you want to enter the next room ? Please type 1 if yes or 0 if no.."
		
		while True:
			try:
				opt = int(raw_input(">>>>>>>>>"))
			except ValueError:
				print("Please Enter a valid response.....")
				
			else:
				break
		if opt == 1:
				status += 1
		else:
			print "sorry you die if you dont continue"
			##death
			
			
			
			
## Engine class: keeps track of the player lives, keeps count on what room has been entered, game status (the initiation and end of game)
class Engine(object):
	def __init__(self, scene_map, name, sex):
		self.scene_map = scene_map
	    self.name = name
		self.sex = sex
    
	def play(self):
		if self.scene_map == 'central_corridor'
		print"Type '1' to play. Type '0' to quit"
		while True:
			try:
				opt = int(raw_input(">>>>>>>>>"))
			except ValueError:
				print("Please Enter a valid response.....")
				
			else:
				break
		return opt
		

## class Death derived from base Scene, dies in various funny ways		
class Death(Scene):
	def __init__(self, name, sex, status, enter)
		super(Death,self).__init__(name,sex,enter)
		
	def term(self):
		
		print"Sorry %s, you must die now because you are a......0. Loser...."% (self.name)
	
		
#class CentralCorridor derived from base class Scene. Right after opening scene, where hero faces gothon a
class CentralCorridor(Scene):
	def __init__(self,name,sex, status):
		super(CentralCorridor,self).__init__(name, sex, status)
	
	
	def nar(self):
		if status == 0 and enter == 0:
			print "Welcome %s to the corridor. Be prepared to have an adventure of a lifetime" % (name)
			print "From far far across the horizon, comes the evil GOTHON with all him munchkins, ready to kill you!"
			print "you have to pick the funniest of the two following jokes to defeat him:.........."
			print "A: 'knock,knock whos there? nobody...'"
			print "B: 'what is 1 scared of 2. cuz 2,3,4.'"
			opt = raw_input(">>>>>>>>")
			return opt
		


#class LaserWeaponArmory derived from base class Scene		
class LaserWeaponArmory(Scene):
	def __init__(self,name,sex,status, enter)

		
# class EscapePod derived from base class Scene		
class EscapePod(Scene):
	
	def enter(self):
		pass
		
##class Bridge derived from base class Scene

class Bridge(Scene):
	def enter(self):
		pass
	
## class Map
class Map(object):
	def __init__(self, start_scene):
		self.start_scene = start_scene
	
	def next_scene(self, scene_map):
		pass
		
	def opening_scene(self):
		pass
		
		
		
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()	


	
		