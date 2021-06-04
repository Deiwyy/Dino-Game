import pygame
import os

pygame.init()

l = lambda x: pygame.image.load(x)

class TextureManager:
	TEXTURES = {
		'dino': {
					'run':[l('assets/Dino/DinoRun1.png'), l('assets/Dino/DinoRun2.png')],
					'duck': [l('assets/Dino/DinoDuck1.png'), l('assets/Dino/DinoDuck2.png')],
					'jump': [l('assets/Dino/DinoJump.png')],
					'start': [l('assets/Dino/DinoStart.png')],
					'dead': [l('assets/Dino/DinoDead.png')]
		},
		'ground': {
					'main': [l('assets/Other/Track.png')]
		},
		'bird': {
					'flap': [l('assets/Bird/Bird1.png'), l('assets/Bird/Bird2.png')]
		},
		'cactus': {
					'large': [l('assets/Cactus/LargeCactus1.png'), l('assets/Cactus/LargeCactus2.png'), l('assets/Cactus/LargeCactus3.png')],
					'small': [l('assets/Cactus/SmallCactus1.png'), l('assets/Cactus/SmallCactus2.png'), l('assets/Cactus/SmallCactus3.png')],
		},
		'go': {
					'text': l('assets/Other/GameOver.png'),
					'reset': l('assets/Other/Reset.png'),
		}
	}


	@staticmethod
	def get_textures(name):
		return TextureManager.TEXTURES[name]