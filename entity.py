import pygame

class Entity:
    def __init__(self, screen: pygame.Surface, color: str, x: float, y: float, size: int, movement_speed: int):
        self.screen = screen
        self.color = color
        self.x = x
        self.y = y
        self.size = size
        self.movement_speed = movement_speed
        self.calculate_center()

    def calculate_center(self):
        self.center = pygame.Vector2(self.x + self.size / 2, self.y + self.size / 2)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.size, self.size))
