import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
screen_rect = screen.get_rect()
pygame.display.set_caption("Quarto exercício")
clock = pygame.time.Clock()

ground_img = pygame.image.load("GamePython/graphics/ground.png").convert()
sky_img = pygame.image.load("GamePython/graphics/Sky.png").convert()
player_img = pygame.image.load("GamePython\graphics\Player\player_walk_1.png").convert_alpha()

player_rect = player_img.get_rect(midbottom = (200, 300))


while True:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            exit()
        if events.type == pygame.MOUSEBUTTONDOWN:
            player_rect.center = events.pos
            
        if events.type == pygame.MOUSEBUTTONUP:
            player_rect.midbottom = (200, 300)
    screen.blit(sky_img, (0,0))
    screen.blit(ground_img, (0,300))
    screen.blit(player_img, player_rect)
    
    pygame.display.update()
    clock.tick(60)