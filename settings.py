import pygame
class Settings():
	"""A class to store information about the game's settings."""
	
	def __init__(self):
		self.word_length = 5
		self.guesses_allowed = 6
		self.num_rows = 6
		self.num_cols = 5
		self.box_length = 50
		self.box_thickness = 1
		self.spacing = 10
		self.margin = 55
		
		#ending message info
		self.winning_messages = ['Genius', 'Magnificent', 'Impressive', 'Splendid', 'Great', 'Phew']
		self.box_margin = 5
		
		#font info
		self.large_font = pygame.font.Font('freesansbold.ttf', 32)
		self.small_font = pygame.font.Font('freesansbold.ttf', 16)
		
		#screen info
		self.screen_width = 2 * self.margin + self.word_length * self.box_length + (self.word_length - 1) * self.spacing
		self.screen_height = 2 * self.margin + self.guesses_allowed * self.box_length + (self.guesses_allowed - 1) * self.spacing
		self.dimensions = (self.screen_width, self.screen_height)
		
		#colors
		self.green = (59, 168, 61)
		self.yellow = (220, 220, 50)
		self.light_gray = (100, 100, 100)
		self.dark_gray = (100, 100, 100)
		self.black = (0, 0, 0)
		self.white = (255, 255, 255)
		
		with open('text_files/valid_guesses.txt') as file_object:
			self.valid_guesses = file_object.read().splitlines()	
		with open('text_files/answers.txt') as file_obj:
			self.answers = file_obj.read().splitlines()

