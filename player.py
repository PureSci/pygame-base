import pygame
from enemy import Enemy
from gun import Gun
from gunnedEntity import GunnedEntity

class Player(GunnedEntity):
    def __init__(self, screen: pygame.Surface, color: str, x: float, y: float, size: int, movement_speed: int, gun: Gun, shot_cooldown: int):
        self.last_shot_time = 0
        self.shot_cooldown = shot_cooldown
        super().__init__(screen, color, x, y, size, movement_speed, gun)

    def handle(self, delta_time: float, enemies: list[Enemy]):
        self.__handle_movement__(delta_time)
        self.draw(delta_time)
        self.__handle_gun__()
        return self.__handle_enemies__(enemies)
    
    def __handle_movement__(self, delta_time: float):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.y -= self.movement_speed * delta_time
        if keys[pygame.K_s]:
            self.y += self.movement_speed * delta_time
        if keys[pygame.K_a]:
            self.x -= self.movement_speed * delta_time
        if keys[pygame.K_d]:
            self.x += self.movement_speed * delta_time

        width = self.screen.get_width()
        height = self.screen.get_height()

        if self.x < 0:
            self.x = 0
        if self.x + self.size > width:
            self.x = width - self.size
        if self.y < 0:
            self.y = 0
        if self.y + self.size > height:
            self.y = height - self.size

        self.calculate_center()
    
    def __handle_enemies__(self, enemies: list[Enemy]):
        for enemy in enemies:
            if (self.x < enemy.x + enemy.size and self.x + self.size > enemy.x and
                self.y < enemy.y + enemy.size and self.y + self.size > enemy.y):
                return True
        return False

    def __handle_gun__(self):
        if pygame.mouse.get_pressed()[0]:
            current_time = pygame.time.get_ticks()
            if current_time - self.last_shot_time >= self.shot_cooldown:
                cursor_x, cursor_y = pygame.mouse.get_pos()
                self.gun.fire(cursor_x, cursor_y)
                self.last_shot_time = current_time