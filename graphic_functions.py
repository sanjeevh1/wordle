import pygame
import sys

class Graphics():
	"""A class with functions that draw several objects."""
	
	def __init__(self, settings):
		self.settings = settings
		self.screen = pygame.display.set_mode(self.settings.dimensions)
		self.screen.fill(settings.white)
		pygame.display.set_caption("Wordle")
		self.initialize_screen()
		
	def initialize_screen(self):
		"""Draws empty squares."""
		i = 0
		while i < self.settings.guesses_allowed:
			j = 0
			while j < self.settings.word_length:
				self.fill(self.settings.light_gray, i, j)
				self.clear(i, j)
				j += 1
			i += 1
	
	def get_x(self, col):
		"""Returns the x coordinate of the left end of a box in the given column."""
		x = self.settings.margin + col * (self.settings.box_length + self.settings.spacing)
		return x
	
	def get_y(self, row):
		"""Returns the y coordinate of the top of a box in the given row."""
		y = self.settings.margin + row * (self.settings.box_length + self.settings.spacing)
		return y
	
	def fill(self, color, row, col):
		"""Fills the box corresponding to row, col."""
		x = self.get_x(col)
		y = self.get_y(row)
		length = self.settings.box_length
		square = pygame.Rect(x, y, length, length)
		pygame.draw.rect(self.screen, color, square)

	def clear(self, row, col):
		"""Clears the box corresponding to row, col."""
		x = self.get_x(col) + self.settings.box_thickness
		y = self.get_y(row) + self.settings.box_thickness
		length = self.settings.box_length - 2 * self.settings.box_thickness
		square = pygame.Rect(x, y, length, length)
		pygame.draw.rect(self.screen, self.settings.white, square)

	def print_char(self, color, char, row, col):
		"""Types char into the box corresponding to row, col."""
		text = self.settings.large_font.render(char.title(), True, color)
		width, height = self.settings.large_font.size(char.title())
		x = self.get_x(col) + self.settings.box_length / 2 - width / 2
		y = self.get_y(row) + self.settings.box_length / 2 - height / 2
		self.screen.blit(text, (x, y))
	
	def print_word(self, row, word, colors):
		"""Prints word in given row with given colors."""
		for number in range(len(word)):
			self.fill(colors[number], row, number)
			self.print_char(self.settings.white, word[number], row, number)
		
	def end(self, message):
		"""Displays the final message."""
		
		text = self.settings.small_font.render(message, True, self.settings.white)
		text_width, text_height = self.settings.small_font.size(message)
		text_x = self.settings.screen_width / 2 - text_width / 2
		text_y = self.settings.margin / 2 - text_height / 2
		
		rect_x = self.settings.screen_width / 2 - self.settings.box_margin - text_width / 2
		rect_y = self.settings.margin / 2 - text_height / 2 - self.settings.box_margin
		rect_width = text_width + 2 * self.settings.box_margin
		rect_height = text_height + 2 * self.settings.box_margin
		box = pygame.Rect(rect_x, rect_y, rect_width, rect_height)
		
		pygame.draw.rect(self.screen, self.settings.dark_gray, box)
		self.screen.blit(text, (text_x, text_y))
		pygame.display.flip()
		
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

		
		
	
	




