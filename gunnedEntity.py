import pygame
from entity import Entity
from gun import Gun

class GunnedEntity(Entity):
    def __init__(self, screen: pygame.Surface, color: str, x: float, y: float, size: int, movement_speed: int, gun: Gun):
        super().__init__(screen, color, x, y, size, movement_speed)
        gun.set_entity(self)
        self.gun = gun
    
    def draw(self, delta_time: float):
        self.gun.draw(delta_time)
        super().draw()