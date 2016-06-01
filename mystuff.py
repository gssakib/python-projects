
#class Scene(object):
#	def __init__ (self, name, sex, lives, status, enter):
#		self.name = name
#		self.sex = sex
#		self.lives = lives
#		self.status = status
#		self.enter = enter
		
#	def enter(self):
	##based on the parameters we play out the derived scene
#		print "Do you want to enter the next room ? Please type 1 if yes or 0 if no.."
			
			

#a_scene = Scene('gazi', 'male',3, 1,1)
#print a_scene.enter


class Scene(object):
	def __init__ (self, name,sex,status,lula,mima,kuka):
		self.name = name
		self.sex = sex
		self.status = status
		self.lula = lula
		self.mima = mima
		self.kuka = kuka
	
	def enter(self):
	##based on the parameters we play out the derived scene
		print self.name
		print self.status
			

a_scene = Scene('gazi','male','0','lula-param','mima',1)
print a_scene.enter