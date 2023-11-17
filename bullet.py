import pygame
from entity import Entity
import math

class Bullet(Entity):
    def __init__(self, screen: pygame.Surface, color: str, x: float, y: float, size: int, movement_speed: int, goal_x: int, goal_y: int):
        super(self.__class__, self).__init__(screen, color, x, y, size, movement_speed)
        angle = math.atan2(goal_y - self.y, goal_x - self.x)
        self.direction = pygame.Vector2(math.cos(angle), math.sin(angle))
    
    def draw(self, delta_time: float):
        self.x += self.movement_speed * self.direction.x * delta_time
        self.y += self.movement_speed * self.direction.y * delta_time
        self.calculate_center()
        super().draw()
        if self.x < 0 or self.x > self.screen.get_width() or self.y < 0 or self.y > self.screen.get_height():
            return (True, self.x, self.y, self.size)
        return (False, self.x, self.y, self.size)