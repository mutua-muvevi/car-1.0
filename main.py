import pygame
import sys


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snake 1.0")

        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()

    def load_level(self, map_id):
        pass

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
            self.clock.tick(60)


Game().run()
