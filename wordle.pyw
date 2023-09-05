"""Run this module to begin the game."""
import pygame
import sys 
import string
from game_info import Game
from graphic_functions import Graphics
from settings import Settings

pygame.init()
settings = Settings()
game = Game(settings)
graph = Graphics(settings)

#column number of current word
column = 0
#word currently being typed
current_word = ''

while True:
	pygame.display.flip()
	for event in pygame.event.get():
		row = game.num_guesses 
		if game.found_word:
			graph.end(settings.winning_messages[game.num_guesses - 1])
		if game.num_guesses == settings.guesses_allowed:
			graph.end(game.answer.upper())
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.KEYDOWN:
			char = pygame.key.name(event.key)
			try:
				#checks if char is a letter
				string.ascii_lowercase.index(char)	
			
			except ValueError:
				
				#Displays colors and moves to next word if user presses enter
				if event.key == pygame.K_RETURN:
					colors = game.get_colors(current_word)
					if colors != None:
						graph.print_word(row, current_word, colors)
						current_word = ''
						column = 0
						game.num_guesses += 1
				
				#Deletes previous letter if user presses backspace	
				elif (event.key == pygame.K_BACKSPACE) and (len(current_word) > 0):
					column -= 1
					current_word = current_word[:(len(current_word) - 1)]
					graph.clear(row, column)
			
			#types letter on screen if user presses a letter		
			else:	
				if column < 5:
					current_word += char
					graph.print_char(settings.black, char, row, column)
					column += 1


			


