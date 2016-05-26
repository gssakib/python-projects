class Song():
	def __init__(self,lyrics ):
		self.lyrics = lyrics
		
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line
	
birth_song = 'Happy birthday to you.\n I dont want to get sued.\n So I will stop right there'
happy_bday = Song([birth_song])

					
bulls_on_parade = Song(["They rally around tha family",
						"With pocket full of shells",'gazi is good'])
						

happy_bday.sing_me_a_song()

print 10*'-'
bulls_on_parade.sing_me_a_song()

print 10*'-'
happy_bday.__init__([birth_song])



