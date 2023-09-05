import json
import random

class Game():
	"""A class for storing information about the game."""
	
	def __init__(self, settings):
		self.num_guesses = 0
		self.settings = settings
		self.answer = random.choice(settings.answers)
		self.found_word = False #will become true when word is correctly guessed

	def get_colors(self, guess):
		"""Returns a list of colors to be displayed."""
		
		if guess not in self.settings.valid_guesses:
			return None
		
		colors = []
		for index in range(self.settings.word_length):
			colors.append(self.settings.dark_gray)
			if guess[index] == self.answer[index]:
				colors[index] = self.settings.green
			else:
				#number of times char appears in correct word but not guessed word
				count_correct = 0
				#number of times letter has already been guessed without being in correct position
				count_guessed = 0
				
				for num in range(self.settings.word_length):
					if self.answer[num] == guess[index]:
						if guess[num] != guess[index]:
							count_correct += 1
					elif (num < index) and (guess[num] == guess[index]):
						count_guessed += 1
				if count_guessed < count_correct:
					colors[index] = self.settings.yellow
							
		if guess == self.answer:
			self.found_word = True
		return colors
		
				
		
		
		
		
	
	
	
	
