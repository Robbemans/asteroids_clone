import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, PLAYER_RADIUS
from logger import log_state
from player import Player
from circleshape import CircleShape


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2
    player = Player(x, y, PLAYER_RADIUS)

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        clock.tick(60)
        dt += (clock.tick(60)/1000)



if __name__ == "__main__":
    main()
