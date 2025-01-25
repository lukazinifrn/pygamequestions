import pygame
from sys import exit

pygame.init()
window_width = 800
window_height = 400
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Questão 1")
clock = pygame.time.Clock()
font = pygame.font.Font("font/Pixeltype.ttf", 50)

sky = pygame.image.load("graphics/Sky.png")
ground = pygame.image.load("graphics/ground.png")
gametitle = font.render("My Game", False, (64, 64, 64))
player = pygame.image.load("graphics/Player/player_walk_1.png")
snail = pygame.image.load("graphics/snail/snail1.png")
ground_ypos = 300
v_snail = 4

player_rect = player.get_rect(midbottom = (200, ground_ypos))
snail_rect = snail.get_rect(midbottom = (600, ground_ypos))
gametitle_rect = gametitle.get_rect(center = (window_width/2, 50))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                print("Andar para a direita")
            if event.key == pygame.K_a:
                print("Andar para a esquerda")
    
    screen.blit(sky, (0,0))
    screen.blit(ground, (0, ground_ypos))
    screen.blit(player, player_rect)
    screen.blit(snail, snail_rect)
    pygame.draw.rect(screen, "#c0e8ec", gametitle_rect)
    pygame.draw.rect(screen, "#c0e8ec", gametitle_rect, 10)
    screen.blit(gametitle, gametitle_rect)
    # pygame.draw.line(screen, "black", (0,0), (window_width, window_height), 10)
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        player_rect.right += 4
        
    if keys[pygame.K_a]:
        player_rect.left -= 4
        
    if player_rect.left > window_width:
        player_rect.right = 0
        
    if player_rect.right < 0:
        player_rect.left = window_width
            
    snail_rect.left -= v_snail
    if snail_rect.right <= 0:
        snail_rect.left = window_width
    
    pygame.display.update()
    clock.tick(60)