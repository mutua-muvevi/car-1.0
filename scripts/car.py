import pygame
import math


class Car:
    def __init__(self, game, position, crashed, car_type):
        self.game = game
        self.position = list(position)
        self.speed = [0, 0]
        self.crashed = crashed
        self.size = (50, 30)
        self.car_type = car_type
        self.color = (255, 0, 0)
        self.direction = "LEFT"

        self.car_surface = pygame.Surface(self.size, pygame.SRCALPHA)
        self.car_surface.fill(self.color)

    def rect(self):
        return pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1])

    def update(self, movement):
        # Reset speed
        self.speed = [0, 0]

        if movement['UP']:
            self.speed[1] = -5
        if movement['DOWN']:
            self.speed[1] = 5
        if movement['LEFT']:
            self.speed[0] = -5
        if movement['RIGHT']:
            self.speed[0] = 5

        # Normalize speed to handle diagonal movement correctly
        if self.speed[0] != 0 and self.speed[1] != 0:
            self.speed[0] *= 0.7071  # 1 / sqrt(2)
            self.speed[1] *= 0.7071  # 1 / sqrt(2)

        # Determine the direction
        if movement['UP']:
            if movement['LEFT']:
                self.direction = "UP_LEFT"
            elif movement['RIGHT']:
                self.direction = "UP_RIGHT"
            else:
                self.direction = "UP"
        elif movement['DOWN']:
            if movement['LEFT']:
                self.direction = "DOWN_LEFT"
            elif movement['RIGHT']:
                self.direction = "DOWN_RIGHT"
            else:
                self.direction = "DOWN"
        elif movement['LEFT']:
            self.direction = "LEFT"
        elif movement['RIGHT']:
            self.direction = "RIGHT"

        # Update position with boundary check
        new_position = [
            self.position[0] + self.speed[0],
            self.position[1] + self.speed[1]
        ]

        # Check for collision with screen borders
        screen_width, screen_height = self.game.screen.get_size()

        if new_position[0] - (self.size[0] / 2) < 0 or new_position[0] + (self.size[0] / 2) > screen_width:
            self.speed[0] = 0
        else:
            self.position[0] = new_position[0]

        if new_position[1] - (self.size[1] / 2) < 0 or new_position[1] + (self.size[1] / 2)  > screen_height:
            self.speed[1] = 0
        else:
            self.position[1] = new_position[1]

    def render(self, surface, offset=(0, 0)):
        # Determine the angle based on the direction
        angle = 0
        if self.direction == "UP":
            angle = 90
        elif self.direction == "DOWN":
            angle = -90
        elif self.direction == "LEFT":
            angle = 180
        elif self.direction == "RIGHT":
            angle = 0
        elif self.direction == "UP_LEFT":
            angle = 135
        elif self.direction == "UP_RIGHT":
            angle = 45
        elif self.direction == "DOWN_LEFT":
            angle = -135
        elif self.direction == "DOWN_RIGHT":
            angle = -45

        # Rotate the car surface
        rotated_car_surface = pygame.transform.rotate(self.car_surface, angle)

        # Get the rotated rectangle to position the surface correctly
        rotated_rect = rotated_car_surface.get_rect(center=(self.position[0] + offset[0], self.position[1] + offset[1]))

        # Blit the rotated surface onto the main surface
        surface.blit(rotated_car_surface, rotated_rect.topleft)
