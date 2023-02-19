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
scenarioOptions = [[2, 5],[3,4],[1,1],[1,1],[6,25],[7,23],[8,8],[9,21],[10,22],[11,22],[12,22],[13],[14],[1,1],[16,18],[1,1],[19,20],[19,20],[1,1],[1,1],[16,18],[16,18],[24,7],[1,1],[26,23],[28,31],[29,30],[31,32],[1,1]]

# Variables
scenario = 1

    # Text
font = pygame.font.Font('medieval.ttf', 28)

# Functions
def decide(key):
    return scenarioOptions[scenario-1][key]

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
    textWrap(scenarioText[scenario-1], scenarioOptionText[scenario-1], 60, height/2)



    pygame.display.flip()


