import pygame
from texture_manager import TextureManager
from animation_manager import AnimationManager
import random


class Obstacle:
	def __init__(self):
		pass

	def get_hitbox(self):
		return self.hitbox



class Bird(Obstacle):
	def __init__(self, y, win_width):
		self.type = 'bird'
		self.textures = TextureManager.get_textures('bird')
		self.anim_manager = AnimationManager()
		self.anim_manager.set_playing(True)
		self.anim_manager.set_animation(self.textures['flap'], 10)
		self.hitbox_trim = 15
		self.hitbox = self.anim_manager.get_current_frame().get_rect()
		self.hitbox.y = y
		self.hitbox.x = win_width + self.hitbox.width


	def update(self, scroll_speed):
		self.anim_manager.update()
		last_hitbox = self.hitbox
		self.hitbox = self.anim_manager.get_current_frame().get_rect()
		self.hitbox.x = last_hitbox.x
		self.hitbox.y = last_hitbox.y			
		self.hitbox.x += scroll_speed

		# self.hitbox.x += self.hitbox_trim/2
		# self.hitbox.width -= self.hitbox_trim/2
		# self.hitbox.y += self.hitbox_trim/4
		# self.hitbox.height -= self.hitbox_trim/4



	def draw(self, surface):
		surface.blit(self.anim_manager.get_current_frame(), (self.hitbox.x, self.hitbox.y))


class Cactus(Obstacle):
	def __init__(self, ground_height, win_width):
		self.type = 'cactus'
		if random.randint(0, 10) > 5:
			self.texture = random.choice(TextureManager.get_textures('cactus')['large'])
		else:
			self.texture = random.choice(TextureManager.get_textures('cactus')['large'])
		self.hitbox = self.texture.get_rect()
		self.hitbox.bottom = ground_height
		self.hitbox.x = win_width + self.hitbox.width
		self.hitbox_trim = 15
		self.hitbox.x = self.hitbox.x + self.hitbox_trim/2
		self.hitbox.width = self.hitbox.width - self.hitbox_trim*1.5


	def update(self, scroll_speed):
		self.hitbox.x += scroll_speed

	def draw(self, surface):
		surface.blit(self.texture, (self.hitbox.x-self.hitbox_trim/2, self.hitbox.y))
