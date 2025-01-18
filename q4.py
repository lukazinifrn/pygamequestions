import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Quarto exercício")
clock = pygame.time.Clock()
font = pygame.font.Font("GamePython/font/Pixeltype.ttf", 50)

ground_img = pygame.image.load("GamePython/graphics/ground.png")
sky_img = pygame.image.load("GamePython/graphics/Sky.png")
snail_img = pygame.image.load("GamePython/graphics/snail/snail1.png")
title_img = font.render("My Game", False, "black")

snail_xwalk = 600

while True:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            exit()
            
    screen.blit(sky_img, (0,0))
    screen.blit(ground_img, (0,300))
    screen.blit(title_img, (300,50))
    screen.blit(snail_img, (snail_xwalk,270))
    
    snail_xwalk -= 4
    
    if snail_xwalk < -70:
        snail_xwalk = 810
            
    pygame.display.update()
    clock.tick(60)