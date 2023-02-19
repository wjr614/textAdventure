import sys, pygame
pygame.init()

size = width, height = 900, 600
black = 0, 0, 0

screen = pygame.display.set_mode(size)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()


    screen.fill(black)
    pygame.display.flip()