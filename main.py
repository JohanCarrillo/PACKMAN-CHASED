import pygame
from sys import exit
from board import board_skelleton

BLACK = (0, 0, 0)
UNIT_SIZE = 25 # in pixel
HEIGHT = len(board_skelleton) * UNIT_SIZE
WIDTH = len(board_skelleton[0]) * UNIT_SIZE
VALID_KEYS = {
    "up": [pygame.K_w, pygame.K_UP],
    "down": [pygame.K_s, pygame.K_DOWN],
    "right": [pygame.K_d, pygame.K_RIGHT],
    "left": [pygame.K_a, pygame.K_LEFT]
}

def main():
	pygame.init()
	screen = pygame.display.set_mode((WIDTH, HEIGHT)) # start screen with given size
	pygame.display.set_caption('Pack-Man Chased')
	clock = pygame.time.Clock()
	screen.fill(BLACK)

	# event loop
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()
			elif event.type == pygame.KEYDOWN:
				if event.key in VALID_KEYS["up"]:
					# move character up
					pass
				elif event.key in VALID_KEYS["down"]:
					# move character down
					pass
				elif event.key in VALID_KEYS["right"]:
					# move character right
					pass
				elif event.key in VALID_KEYS["left"]:
					# move character left
					pass

		pygame.display.update()
		clock.tick(60)

if __name__ == '__main__':
  main()