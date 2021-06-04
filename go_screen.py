import pygame
from texture_manager import TextureManager
pygame.init()




class GO:
	def __init__(self, screen_size):
		self.textures = TextureManager.get_textures('go')
		self.button_hitbox = self.textures['reset'].get_rect()
		self.button_hitbox.centerx = screen_size[0]/2
		self.button_hitbox.centery = screen_size[1]/2 + 50
	
		self.text_hitbox = self.textures['text'].get_rect()
		self.text_hitbox.centerx = screen_size[0]/2
		self.text_hitbox.centery = screen_size[1]/2 - 50


	def check_click(self, click_pos):
		if self.button_hitbox.collidepoint(click_pos):
			return True

	def draw(self, surface):
		surface.blit(self.textures['reset'], (self.button_hitbox.x, self.button_hitbox.y))
		surface.blit(self.textures['text'], (self.text_hitbox.x, self.text_hitbox.y))