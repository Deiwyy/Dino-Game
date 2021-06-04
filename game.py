import pygame
from ground import Ground
from player import Player
from texture_manager import TextureManager
from obstacle_manager import ObstacleManager
from go_screen import GO
import color
pygame.init()



class Game:
	def __init__(self, mainloop, window):
		self.mainloop = mainloop
		self.game_over = False
		self.screenshot = None
		self.window = window
		self.screen = window.get()
		self.go = GO(self.window.get_size())
		self.player = Player(50, 425)
		self.ground = Ground(self.window.get_height()-TextureManager.get_textures('ground')['main'][0].get_rect().height-20)
		self.ground_scroll_speed = 6
		self.points = 0
		self.add_point_event = pygame.USEREVENT+1
		self.add_point_event_speed = 100
		self.spawn_speed = 2000
		self.spawn_event = pygame.USEREVENT+2
		self.obs_manager = ObstacleManager()
		self.paused = False
		self.blur = pygame.Surface(self.window.get_size())
		pygame.time.set_timer(self.spawn_event, self.spawn_speed)
		pygame.time.set_timer(self.add_point_event, self.add_point_event_speed)

	def update(self, events, keys_pressed):
		for e in events:
			if e.type == pygame.QUIT:
				self.mainloop.stop()
			if e.type == pygame.KEYDOWN:
				if e.key == pygame.K_SPACE:
					if self.paused:
						self.paused = False
					else:
						self.paused = True
						self.screenshot = self.screen.copy()

			if e.type == pygame.MOUSEBUTTONDOWN:
				if self.game_over:
					if self.go.check_click(pygame.mouse.get_pos()):
						self.reset_game()
			if not self.game_over:
				if e.type == self.spawn_event:
					self.obs_manager.spawn(self.window.get_width(), self.ground.get_ground()[0].top)
				if e.type == self.add_point_event:
					self.points += 1



		if not self.game_over and not self.paused:
			self.obs_manager.update(-self.ground_scroll_speed)
			self.ground.update(self.window.get_width(), self.ground_scroll_speed)
			self.player.update(keys_pressed)
			self.player.move(self.ground.get_ground())
			if self.player.check_collision([o.get_hitbox() for o in self.obs_manager.get_obstacles()]):
				self.screenshot = self.screen.copy()
				self.game_over = True
			self.draw()
		elif self.game_over:
			self.game_over_screen()
		elif self.paused:
			self.paused_screen()


	def draw(self):
		self.screen.fill(color.WHITE)
		self.ground.draw(self.screen)
		self.obs_manager.draw(self.screen)
		self.player.draw(self.screen)
		pygame.display.update()


	def game_over_screen(self):
		self.blur.fill(color.GO_BLUR)
		self.blur.set_alpha(128)
		self.screen.blit(self.screenshot, (0, 0))
		self.screen.blit(self.blur, (0, 0))
		self.go.draw(self.screen)
		pygame.display.update()

	def paused_screen(self):
		self.blur.fill(color.PAUSED_BLUR)
		self.blur.set_alpha(128)
		self.screen.blit(self.screenshot, (0, 0))
		self.screen.blit(self.blur, (0, 0))
		pygame.display.update()


	def reset_game(self):
		self.game_over = False
		self.go_screenshot = None
		self.go = GO(self.window.get_size())
		self.player = Player(50, 425)
		self.ground = Ground(self.window.get_height()-TextureManager.get_textures('ground')['main'][0].get_rect().height-20)
		self.ground_scroll_speed = 6
		self.points = 0
		self.obs_manager = ObstacleManager()