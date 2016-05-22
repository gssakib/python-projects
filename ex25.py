def break_words(stuff) :
	"""This function will break up words"""
	words = stuff.split(' ')
	return words
	
def sort_words(words):
	"""This function will sort words"""
	return sorted(words)

def print_first_word(words):
	"""Prints the first words after popping if off."""
	word = words.pop(0)
	print word
def print_last_word(words):
	"""Prints the last words after popping it off"""
	word = words.pop(-1)
	print word
	
def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words = break_words(sentence)
	return sort_words(words)
	
def print_first_and_last(sentence):
	"""Breaks up the words, then prints the first and last words"""
	word = break_words(sentence)
	print_first_word(word)
	print_last_word(word)
	
def print_first_and_last_sorted_sentence(sentence):
	"""Breaks up the words, sorts them and then prints out the last and first words"""
	sorted = sort_sentence(sentence)
	print_first_word(sorted)
	print_last_word(sorted)
	
	
	