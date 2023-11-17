import time
import pygame
import constants
from enemy import Enemy
from player import Player
from gun import Gun

pygame.init()
screen = pygame.display.set_mode(constants.WINDOW_SIZE)
clock = pygame.time.Clock()
running = True
delta_time = 0
enemytime = time.time() + constants.ENEMY_SPAWN_FREQUENCY
enemies: list[Enemy] = []
stop = False

player = Player(
    screen, 
    constants.PLAYER_COLOR,
    screen.get_width() / 2,
    screen.get_height() / 2,
    constants.PLAYER_SIZE,
    constants.PLAYER_MOVEMENT_SPEED,
    Gun(constants.GUN_WIDTH, constants.GUN_LENGTH, enemies),
    constants.BULLET_RELOAD_TIME
)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if stop is False:
        screen.fill(constants.BACKGROUND_COLOR)

        if time.time() >= enemytime:
            enemies.append(Enemy(screen, constants.ENEMY_COLOR, constants.PLAYER_SIZE, constants.PLAYER_MOVEMENT_SPEED // 2, player))
            enemytime = time.time() + constants.ENEMY_SPAWN_FREQUENCY
        for enemy in enemies:
            enemy.draw(delta_time)

        stop = player.handle(delta_time, enemies)

        pygame.display.flip()

        # limits FPS to 60
        # delta time: seconds since last frame, used for framerate-independent physics.
        delta_time = clock.tick(60) / 1000

pygame.quit()