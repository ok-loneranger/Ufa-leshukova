import pygame
import random

pygame.font.init()

# WINDOW SIZE
window_size_x = 480
window_size_y = 853

# GAME SETTINGS
game_run = True

# PLAYER SETTINGS
player_size_x = 100
player_size_y = 40
player_color = (0,255,0)
player_position_x = 100
player_position_y = 600
player_speed = 5

# FALLING ITEMS
colors = [[255,0,0], [0,255,0], [0,0,255], [255,255,0]]

item_size_x = 20
item_size_y = 20
item_speed = 2

items = [[[10,0], [255,0,0]],[[55,0],[255,0,0] ],[[100,0], [255,0,0]],[[145,0], [255,0,0]],
        [[190,0], [255,0,0]],[[235,0], [255,0,0]],[[280,0], [255,0,0]],[[325,0], [255,0,0]],[[370,0], [255,0,0]],
        [[415,0], [255,0,0]],[[460,0], [255,0,0]]]

for i in range(11):
    items[i][0][1] = random.randint(-600 - i * 100, -100 - i * 100)

# STATISTIC
health_point = 10
score = 0
lose = 0
font = pygame.font.SysFont(None, 25)
