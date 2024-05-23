import pygame
import sys

from scripts.car import Car


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Car 1.0")

        self.screen = pygame.display.set_mode((1800, 900))
        self.clock = pygame.time.Clock()

        self.movement = {'UP': False, 'DOWN': False, 'LEFT': False, 'RIGHT': False}
        self.crashed = False

        self.car = Car(self, (50, 50), self.crashed, "player")

    def load_level(self, map_id):
        pass

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_UP, pygame.K_w):
                        self.movement['UP'] = True
                    if event.key in (pygame.K_DOWN, pygame.K_s):
                        self.movement['DOWN'] = True
                    if event.key in (pygame.K_LEFT, pygame.K_a):
                        self.movement['LEFT'] = True
                    if event.key in (pygame.K_RIGHT, pygame.K_d):
                        self.movement['RIGHT'] = True

                if event.type == pygame.KEYUP:
                    if event.key in (pygame.K_UP, pygame.K_w):
                        self.movement['UP'] = False
                    if event.key in (pygame.K_DOWN, pygame.K_s):
                        self.movement['DOWN'] = False
                    if event.key in (pygame.K_LEFT, pygame.K_a):
                        self.movement['LEFT'] = False
                    if event.key in (pygame.K_RIGHT, pygame.K_d):
                        self.movement['RIGHT'] = False

            self.screen.fill((41, 123, 225))

            self.car.update(self.movement)
            self.car.render(self.screen)

            pygame.display.update()

            self.clock.tick(60)


Game().run()
