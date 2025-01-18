import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Quarto exercício")
clock = pygame.time.Clock()
font = pygame.font.Font("GamePython/font/Pixeltype.ttf", 50)

ground_img = pygame.image.load("GamePython/graphics/ground.png").convert()
sky_img = pygame.image.load("GamePython/graphics/Sky.png").convert()
snail_img = pygame.image.load("GamePython/graphics/snail/snail1.png").convert_alpha()
player_img = pygame.image.load("GamePython\graphics\Player\player_walk_1.png").convert_alpha()
title_img = font.render("My Game", False, "black")

snail_rect = snail_img.get_rect(midbottom = (600, 300))
player_rect = player_img.get_rect(midbottom = (200, 300))


while True:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            exit()
            
    screen.blit(sky_img, (0,0))
    screen.blit(ground_img, (0,300))
    screen.blit(title_img, (300,50))
    screen.blit(snail_img, snail_rect)
    screen.blit(player_img, player_rect)
    snail_rect.left -= 4
    player_rect.left += 3
    
    if snail_rect.right <= 0:
        snail_rect.left = 800
    
    if player_rect.left >= 800:
        player_rect.right = 0 
            
    pygame.display.update()
    clock.tick(60)