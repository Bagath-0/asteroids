import pygame
pygame.init
from constants import *
from player import *

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
def main():
    print ("Starting asteroids!")   
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    clock = pygame.time.Clock()
    FPS = 60
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        color = (0,0,0)
        screen.fill(color)
        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(FPS)
        dt = dt/1000
        



if __name__ == "__main__":
    main()
