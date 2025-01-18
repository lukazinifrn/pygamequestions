import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Segundo exercício")
clock = pygame.time.Clock()

sky_img = pygame.image.load("GamePython/graphics/Sky.png")
ground_img = pygame.image.load("GamePython/graphics/ground.png")

while True:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(sky_img, (0,0))
    screen.blit(ground_img, (0,300))
    
    pygame.display.update()
    clock.tick(60)