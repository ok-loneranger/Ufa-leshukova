import pygame
import options
import functions
import random

pygame.init()


window = pygame.display.set_mode((options.window_size_x, options.window_size_y))

pygame.display.set_caption("Catch your mind")

while options.game_run:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            options.game_run = False

    # PLAYER MOVES
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        functions.player_moves_right()
    if keys[pygame.K_LEFT]:
        functions.player_moves_left()

    # FALLING ITEMS
    functions.item_fall()

    # DRAWING FIGURES
    window.fill((0,0,0))
    for i in range(11):
        pygame.draw.rect(window, (options.items[i][1]), (
        options.items[i][0][0], options.items[i][0][1], options.item_size_x,
        options.item_size_y))
    pygame.draw.rect(window, (options.player_color), (options.player_position_x,
        options.player_position_y,
        options.player_size_x, options.player_size_y))
    text_score = options.font.render("Score: " + str(options.score), True, (255,255,255))
    text_lose = options.font.render("Lose: " + str(options.lose), True, (255,255,255))
    text_hp = options.font.render("HP: " + str(options.health_point), True, (255,255,255))
    window.blit(text_score, [20,650])
    window.blit(text_lose, [20, 700])
    window.blit(text_hp, [20, 750])



    pygame.display.update()



print(options.score)
