import random
from obstacle import *

class ObstacleManager:
	def __init__(self):
		self.bird_chance = 15
		self.bird_y = [350, 415]
		self.cactus_y = 400
		self.obstacles = []
		self.bird_speed_up = 1.5

	def spawn(self, win_width, ground_height):
		if random.randint(0, 100) > self.bird_chance:
			self.obstacles.append(Cactus(ground_height, win_width))
		else:
			self.obstacles.append(Bird(random.choice(self.bird_y), win_width))

	def update(self, scroll_speed):
		for o in self.obstacles:
			if o.type == 'bird':
				o.update(self.bird_speed_up*scroll_speed)
			else:
				o.update(scroll_speed)
			if o.hitbox.right < 0:
				self.obstacles.remove(o)

	def get_obstacles(self):
		return self.obstacles

	def draw(self, surface):
		for o in self.obstacles:
			o.draw(surface)