import pygame
from texture_manager import TextureManager
pygame.init()



class Ground:
	def __init__(self, y):
		self.def_y = y
		self.textures = TextureManager.get_textures('ground')
		self.ground_pieces = [self.new_piece(0)]

	def new_piece(self, x):
		return pygame.Rect(x, self.def_y, self.textures['main'][0].get_width(), self.textures['main'][0].get_height())

	def update(self, win_width, scroll_speed):
		for i, p in enumerate(self.ground_pieces):
			p.x -= scroll_speed
			if p.right <= win_width and i == len(self.ground_pieces)-1:
				self.ground_pieces.append(self.new_piece(win_width))
			if p.right <= 0:
				self.ground_pieces.remove(p)


	def get_ground(self):
		return self.ground_pieces

	def draw(self, surface):
		for p in self.ground_pieces:
			surface.blit(self.textures['main'][0], (p.x, p.y-10))