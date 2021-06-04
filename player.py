import pygame
from texture_manager import TextureManager
from animation_manager import AnimationManager
pygame.init()



class Player:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.textures = TextureManager.get_textures('dino')
		self.anim_manager = AnimationManager()
		self.anim_manager.set_playing(True)
		self.anim_manager.set_animation(self.textures['run'], 10)
		self.is_jumping = False
		self.is_running = True
		self.is_ducking = False
		self.is_in_air = False
		self.hitbox = None
		self.hitbox_trim = 20
		self.update_hitbox(True)
		self.GRAVITY = 1
		self.y_vel = 0
		self.MAX_Y_VEL = 15
		self.JUMP_FORCE = -22


	def update_hitbox(self, first_time=False):
		last_hitbox = self.hitbox
		self.hitbox = self.anim_manager.get_current_frame().get_rect()
		self.hitbox.x = self.x + self.hitbox_trim/2
		self.hitbox.width = self.hitbox.width - self.hitbox_trim*1.5
		self.hitbox.height = self.hitbox.height
		self.hitbox.y = self.y
		if not first_time:
			self.hitbox.bottom = last_hitbox.bottom


	def get_hitbox(self):
		return self.hitbox

	def update(self, keys_pressed):
		self.y_vel += self.GRAVITY
		if self.y_vel > self.MAX_Y_VEL:
			self.y_vel = self.MAX_Y_VEL

		self.anim_manager.update()
		if keys_pressed[pygame.K_s]:
			if not self.is_ducking:
				self.duck()
		elif keys_pressed[pygame.K_w]:
			if not self.is_jumping:
				self.jump()
		else:
			if not self.is_running:
				self.run()

		if self.is_in_air:
			self.jump()
		elif not self.is_running and not self.is_ducking:
			self.run()



		self.update_hitbox()


	def reset_state(self):
		self.is_jumping = False
		self.is_running = False
		self.is_ducking = False


	def duck(self):
		self.reset_state()
		self.is_ducking = True
		self.anim_manager.set_animation(self.textures['duck'], 10)

	def jump(self):
		self.reset_state()
		self.is_jumping = True
		if not self.is_in_air:
			self.is_in_air = True
			self.y_vel = self.JUMP_FORCE
		self.anim_manager.set_animation(self.textures['jump'], 10)

	def run(self):
		self.reset_state()
		self.is_running = True
		self.anim_manager.set_animation(self.textures['run'], 10)


	def move(self, colliders):
		self.hitbox.y += self.y_vel
		for c in colliders:
			if self.hitbox.colliderect(c):
				self.hitbox.bottom = c.top
				self.y_vel = 0
				self.is_in_air = False

	def check_collision(self, obstacles):
		if not self.hitbox.collidelist(obstacles):
			return True
			



	def draw(self, surface):
		surface.blit(self.anim_manager.get_current_frame(), (self.hitbox.x-self.hitbox_trim/2, self.hitbox.y))

