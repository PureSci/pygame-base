import math
import pygame
from bullet import Bullet
import constants
from enemy import Enemy
from entity import Entity

class Gun:
    def __init__(self, width: int, length: int, enemies: list[Enemy]):
        self.width = width
        self.length = length
        self.bullets: list[Bullet] = []
        self.enemies = enemies
    
    def set_entity(self, entity: Entity):
        self.entity = entity
    
    def draw(self, delta_time: float):
        direction = self.__calculate_direction__()
        perp_direction = pygame.Vector2(-direction.y, direction.x) * self.width

        end = self.__calculate_end__(direction)

        corner1 = self.entity.center + perp_direction / 2
        corner2 = self.entity.center - perp_direction / 2
        corner3 = end - perp_direction / 2
        corner4 = end + perp_direction / 2
        for bullet in self.bullets:
            isded, bullet_x, bullet_y, bullet_size = bullet.draw(delta_time)
            for enemy in self.enemies:
                if (bullet_x < enemy.x + enemy.size and bullet_x + bullet_size > enemy.x and
                    bullet_y < enemy.y + enemy.size and bullet_y + bullet_size > enemy.y):
                    self.enemies.remove(enemy)
                    self.bullets.remove(bullet)
            if isded:
                self.bullets.remove(bullet)
        pygame.draw.polygon(self.entity.screen, constants.PLAYER_COLOR, [corner1, corner2, corner3, corner4]) 

    def fire(self, to_x: int, to_y: int):
        end = self.__calculate_end__(self.__calculate_direction__())
        bullet = Bullet(self.entity.screen, self.entity.color, end.x, end.y, self.width, constants.BULLET_SPEED, to_x, to_y)
        self.bullets.append(bullet)

    def __calculate_end__(self, direction: pygame.Vector2):
        return pygame.Vector2(self.entity.center.x + self.length * direction.x, self.entity.center.y + self.length * direction.y)

    def __calculate_direction__(self):
        cursor_x, cursor_y = pygame.mouse.get_pos()

        angle = math.atan2(cursor_y - self.entity.center.y, cursor_x - self.entity.center.x)
        return pygame.Vector2(math.cos(angle), math.sin(angle))