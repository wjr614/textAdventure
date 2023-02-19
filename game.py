import sys, pygame
pygame.init()
pygame.font.init()

# Screen Stuff
size = width, height = 900, 600
black = 0, 0, 0
screen = pygame.display.set_mode(size)

# Scenarios
scenarioText = ["You start the game", "You Played the game", "You Quit"]
scenarioOptionText = ["Hit 1 To Play or 2 to Quit", "The End", "The End"]
scenarioOptions = [[1, 2],[0,0],[0,0]]

# Variables
scenario = 0

    # Text
font = pygame.font.Font('Augusta.ttf', 32)

# Functions
def decide(key):
    return scenarioOptions[scenario][key]

#Startup


while True:
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                scenario = decide(0)
            elif event.key == pygame.K_2:
                scenario = decide(1)
            elif event.key == pygame.K_3:
                scenario = decide(2)
            elif event.key == pygame.K_4:
                scenario = decide(3)

    screen.fill(black)
    
    # Draw Text
    text_surface1 = font.render(scenarioText[scenario], False, (255, 255, 255))
    text_surface2 = font.render(scenarioOptionText[scenario], False, (255, 255, 255))
    rectSize = text_surface1.get_rect()
    rectSize2 = text_surface2.get_rect()

    screen.blit(text_surface1, ((width/2)-rectSize.width/2,4*(height/5)-rectSize.height/2))
    screen.blit(text_surface2, ((width/2)-rectSize2.width/2,4*(height/5)+rectSize.height/2))



    pygame.display.flip()


