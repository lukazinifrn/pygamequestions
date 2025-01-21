import pygame
from sys import exit

pygame.init()

# Main configs
window_width = 800
window_height = 400
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Questão 1")
clock = pygame.time.Clock()
font = pygame.font.Font("GamePython/font/Pixeltype.ttf", 50)

# Sky
sky = pygame.image.load("GamePython/graphics/Sky.png")
sky_rect = sky.get_rect(topleft = (0,0))

# Ground
ground = pygame.image.load("GamePython/graphics/ground.png")
ground_ypos = 300

# Title
gametitle = font.render("My Game", False, (64, 64, 64))
gametitle_rect = gametitle.get_rect(midtop = (sky_rect.centerx, 50))

# Player
player = pygame.image.load("GamePython/graphics/Player/player_walk_1.png")
player_rect = player.get_rect(midbottom = (200, ground_ypos))
player_gravity = 0
jump = 0

# Snail
snail = pygame.image.load("GamePython/graphics/snail/snail1.png")
snail_rect = snail.get_rect(midbottom = (600, ground_ypos))
v_snail = 4


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and jump == 0: # Ou and player_rect.bottom == ground.ypos
                player_gravity -= 20
                jump = 1
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if player_rect.collidepoint(event.pos) and jump == 0: # Ou and player_rect.bottom == ground.ypos
                player_gravity -= 20
                jump = 1

    
    screen.blit(sky, (0,0))

    screen.blit(ground, (0, ground_ypos))

    screen.blit(player, player_rect)

    screen.blit(snail, snail_rect)

    pygame.draw.rect(screen, "#c0e8ec", gametitle_rect)
    pygame.draw.rect(screen, "#c0e8ec", gametitle_rect, 10)
    screen.blit(gametitle, gametitle_rect)

    player_gravity += 1
    snail_rect.left -= v_snail
    player_rect.bottom += player_gravity


    if snail_rect.right < 0:
        snail_rect.left = window_width

    if snail_rect.left > window_width:
        snail_rect.right = 0
    
    # Lógica do pulo e gravidade do player
    if player_rect.bottom >= ground_ypos:
        player_rect.bottom = ground_ypos
        player_gravity = 0
        jump = 0

    if player_rect.top <= 0:
        player_rect.top = 0
        player_gravity = 0
    
    pygame.display.update()
    clock.tick(60)