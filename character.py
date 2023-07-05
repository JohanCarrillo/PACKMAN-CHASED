import pygame
from enum import Enum

IMAGE_SIZE = (45, 45)

class Direction(Enum):
  UPWARDS = 0
  DOWN = 1
  TO_THE_RIGHT = 2
  TO_THE_LEFT = 3

class Character:
	def __init__(self, position: dict[float, float], speed: float, direction: float, path_list: list[str]) -> None:
		self.position = position
		self.speed = speed
		self.direction = direction
		self.images = self.load_images(path_list)

	def set_image(self, image):
			"""set character image
			"""

	def update_direction(self):
		pass

	def update_position(self):
		""" update characters's position 
		"""
		pass

	def load_images(self, path_list: list[str]):
		images = []

		for path in path_list:
			images.append(pygame.transform.scale(pygame.image.load(path), IMAGE_SIZE))

		return images