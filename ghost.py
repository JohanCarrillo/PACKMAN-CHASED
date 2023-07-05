import pygame
from enum import Enum
from character import Character

IMAGES_PATH = 'assets/ghost'

class State(Enum):
	NORMAL = 0
	SUPER = 1
	DEAD = 2

class Color(Enum):
	BLUE = "blue"
	PINK = "pink"
	ORANGE = "orange"
	RED = "red"

class Ghost(pygame.sprite.Sprite, Character):
	def __init__(self, position: dict[float, float], speed: float, 
              direction: float, state: State, color: Color) -> None:
		pygame.sprite.Sprite.__init__(self)
		Character.__init__(self, position, speed, direction)
		self.state = state
		self.color = color

		def update(self):
			"""update position, direction, state and image
			"""
			Character.update_position(self)
			pass