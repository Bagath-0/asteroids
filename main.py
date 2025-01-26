import pygame
pygame.init
from constants import *
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
def main():
    print ("Starting asteroids!")   
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")
    while True == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        color = (0,0,0)
        screen.fill(color)
        pygame.display.flip()




if __name__ == "__main__":
    main()
