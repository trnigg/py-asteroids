import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # Create containers
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # Assign containers to player
    Player.containers = (updateable, drawable)

    # Instatiate player and sets starting point as middle of screen.
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) 





    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        updateable.update(dt)
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
