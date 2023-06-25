import pygame
from sys import exit

WIDTH = 700
HEIGHT = 700

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()

# event loop
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()

	pygame.display.update()
	clock.tick(60)