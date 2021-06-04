import pygame
pygame.init()



class Window:
	def __init__(self, width, height):
		self.initial_width = width
		self.initial_height = height
		self.window = pygame.display.set_mode((width, height))
		pygame.display.set_caption('Dino!')

	def get_init_width(self):
		return self.initial_width

	def get_init_height(self):
		return self.initial_height

	def get_width(self):
		return self.window.get_width()

	def get_height(self):
		return self.window.get_height()

	def get_size(self):
		return (self.get_width(), self.get_height())

	def get(self):
		return self.window