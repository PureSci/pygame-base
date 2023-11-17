import math
from random import randint
from pygame import Surface
import pygame
from entity import Entity


class Enemy(Entity):
    def __init__(self, screen: Surface, color: str, size: int, movement_speed: int, follow: Entity):
        rand = randint(1,4)
        x = -50
        y = -50
        if rand == 1:
            x = randint(0, screen.get_width())
        elif rand == 2:
            x = screen.get_width() + 50
            y = randint(0, screen.get_height())
        elif rand == 3:
            y = screen.get_height() + 50
            x = randint(0, screen.get_width())
        else:
            y = randint(0, screen.get_height())
        self.follow = follow
        super(self.__class__, self).__init__(screen, color, x, y, size, movement_speed)
    
    def draw(self, delta_time):
        angle = math.atan2(self.follow.center.y - self.center.y, self.follow.center.x - self.center.x)
        direction = pygame.Vector2(math.cos(angle), math.sin(angle))
        self.x += self.movement_speed * direction.x * delta_time
        self.y += self.movement_speed * direction.y * delta_time
        self.calculate_center()
        super().draw()