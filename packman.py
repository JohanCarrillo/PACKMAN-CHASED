import pygame
from character import Character
from enum import Enum

IMAGES_PATH = 'assets/packman'

class State(Enum):
	NORMAL = 0
	WEAKENED = 1
	DEAD = 2

class Packman(pygame.sprite.Sprite, Character):
	def __init__(self, position: dict[float, float], speed: float, direction: float, state: State) -> None:
		pygame.sprite.Sprite.__init__(self)
		Character.__init__(self, position, speed, direction)
		self.state = state

		def update(self):
			"""update position, direction, state and image
			"""
			Character.update_position(self)
			pass

		packman_animation_1 = pygame.image.load(IMAGES_PATH)