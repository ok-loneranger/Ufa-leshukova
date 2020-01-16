import pygame
import options
import random
import math

def player_moves_right():
    if options.player_position_x < options.window_size_x - 110:
        options.player_position_x += options.player_speed

def player_moves_left():
    if options.player_position_x > 10:
        options.player_position_x -= options.player_speed

def item_fall():
    for i in range(11):
        options.items[i][0][1] += options.item_speed
        if options.items[i][0][1] > 600:
            if options.player_position_x - options.items[i][0][0] > -100 and options.player_position_x - options.items[i][0][0] < 20:
                print(options.items[i][1])
                if options.items[i][1] == [255, 0, 0]:
                    options.score += 1
                elif options.items[i][1] == [0, 255, 0]:
                    options.player_speed += 0.2
                elif options.items[i][1] == [0, 0, 255]:
                    options.health_point += 3
                elif options.items[i][1] == [255, 255, 0]:
                    options.item_speed -= 0.01
            else:
                options.health_point -= 1
                options.lose += 1
            options.items[i][0][1] = random.randint(-600 - i * 100, -100 - i * 100)
            options.item_speed += 0.001
            draw_color(i)

def draw_color(i):
    temp = random.randint(0, 100)
    if temp <= 70 and temp >= 0:
        options.items[i][1] = options.colors[0]
    elif temp > 70 and temp <= 80:
        options.items[i][1] = options.colors[1]
    elif temp > 80 and temp <= 90:
        options.items[i][1] = options.colors[2]
    elif temp > 90 and temp <= 100:
        options.items[i][1] = options.colors[3]
