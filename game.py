import sys, pygame
pygame.init()

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

# Functions
def decide(key):
    updateScreen(scenarioOptions[scenario][key])
    return scenarioOptions[scenario][key]

def updateScreen(scenarios):
    print(scenarioText[scenarios])
    print(scenarioOptionText[scenarios])

#Startup
updateScreen(scenario)


while True:
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
    pygame.display.flip()


