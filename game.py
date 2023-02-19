import sys, pygame
pygame.init()
pygame.font.init()

# File
with open('scenarioText.txt') as f:
    scenarioText = f.readlines()
    
with open('options.txt') as f:
    scenarioOptionText = f.readlines()

# Screen Stuff
size = width, height = 900, 600
black = 0, 0, 0
screen = pygame.display.set_mode(size)

# Scenarios
scenarioOptions = [[1, 2],[0,0],[0,0]]

# Variables
scenario = 0

    # Text
font = pygame.font.Font('Augusta.ttf', 28)

# Functions
def decide(key):
    return scenarioOptions[scenario][key]

#Startup


while True:

    def textWrap(text, text2, tWidth, sHeight):
        i = 0
        text = text[:-1]
        text2 = text2[:-1]
        while (i < len(text)/tWidth):
            text_surface1 = font.render(text[(tWidth*i):(tWidth*i+tWidth)], False, (255, 255, 255))
            rectSize = text_surface1.get_rect()
            screen.blit(text_surface1, ((width/2)-rectSize.width/2,sHeight+(rectSize.height*i)))
            i+=1
        text_surface1 = font.render(text2, False, (255, 255, 180))
        rectSize = text_surface1.get_rect()
        screen.blit(text_surface1, ((width/2)-rectSize.width/2,sHeight+(rectSize.height*i)))




    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.KEYDOWN:
            try:
                if event.key == pygame.K_1:
                    scenario = decide(0)
                elif event.key == pygame.K_2:
                    scenario = decide(1)
                elif event.key == pygame.K_3:
                    scenario = decide(2)
                elif event.key == pygame.K_4:
                    scenario = decide(3)
            except: print("not an option")

    screen.fill(black)
    
    # Draw Text
    textWrap(scenarioText[scenario], scenarioOptionText[scenario], 70, height/2)



    pygame.display.flip()


