import pygame
from sys import exit

pygame.init()
window_width = 800
window_height = 400
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Questão 1")
clock = pygame.time.Clock()
font = pygame.font.Font("PYGAME/font/Pixeltype.ttf", 50)

sky = pygame.image.load("PYGAME/graphics/Sky.png")
ground = pygame.image.load("PYGAME/graphics/ground.png")
gametitle = font.render("My Game", False, "black")
player = pygame.image.load("PYGAME/graphics/Player/player_walk_1.png")
snail = pygame.image.load("PYGAME/graphics/snail/snail1.png")

ground_ypos = 300
v_snail = 4

player_rect = player.get_rect(midbottom = (200, ground_ypos))
snail_rect = snail.get_rect(midbottom = (600, ground_ypos))
sky_rect = sky.get_rect(topleft = (0,0))
gametitle_rect = gametitle.get_rect(midtop = (sky_rect.centerx, 50))

while True:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            exit()
        if events.type == pygame.MOUSEMOTION:
            if player_rect.collidepoint(events.pos):
                print("COLISÃO!!!")
            if snail_rect.collidepoint(events.pos):
                print("CARACOL!!!")

    
    screen.blit(sky, (0,0))
    screen.blit(ground, (0, ground_ypos))
    screen.blit(player, player_rect)
    screen.blit(snail, snail_rect)
    screen.blit(gametitle, gametitle_rect)

    aceleration = window_width - snail_rect

    snail_rect.left -= v_snail
    if snail_rect.right <= 400 or snail_rect.left >= 600:
        v_snail = -v_snail




    pygame.display.update()
    clock.tick(60)
