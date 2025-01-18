import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Terceiro exercício")
clock = pygame.time.Clock()
font = pygame.font.Font("GamePython/font/Pixeltype.ttf", 50)

sky_img = pygame.image.load("GamePython/graphics/Sky.png")
ground_img = pygame.image.load("GamePython/graphics/ground.png")
title_img = font.render("My game", False, "black")

while True:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(sky_img, (0,0))
    screen.blit(ground_img, (0,300))
    screen.blit(title_img, (300, 50))
    pygame.display.update()
    clock.tick(60)
