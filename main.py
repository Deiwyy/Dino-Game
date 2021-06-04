import pygame
import sys
from window import Window
from game import Game
pygame.init()



class Main:
	def __init__(self):
		self.window = Window(1100, 600)
		self.game = Game(self, self.window)
		self.FPS = 60
		self.clock = pygame.time.Clock()

	def main(self):
		while True:
			self.clock.tick(self.FPS)
			events = pygame.event.get()
			keys_pressed = pygame.key.get_pressed()
			self.game.update(events, keys_pressed)

	def stop(self):
		pygame.quit()
		sys.exit(0)


if __name__ == '__main__':
	m = Main()
	m.main()