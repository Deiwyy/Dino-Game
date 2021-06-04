import pygame
pygame.init()

class AnimationManager:
	def __init__(self):
		self.current_animation = []
		self.frame_skip = 0
		self.skipped_frames = 0
		self.current_index = 0
		self.max_index = 0
		self.is_playing = False


	def set_animation(self, animation, frame_skip):
		self.current_animation = animation
		self.max_index = len(animation) - 1
		self.current_index = 0
		self.frame_skip = frame_skip

	def get_animation(self):
		return self.current_animation

	def set_playing(self, is_playing):
		self.is_playing = is_playing

	def get_playing(self):
		return self.is_playing

	def update(self):
		if self.is_playing:
			self.skipped_frames += 1
			if self.skipped_frames >= self.frame_skip:
				self.skipped_frames = 0
				self.current_index += 1
			if self.current_index > self.max_index:
				self.current_index = 0

	def get_current_frame(self):
		return self.current_animation[self.current_index]