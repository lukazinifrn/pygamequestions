import pygame
from sys import exit
from random import randint

def display_score():
    current_time = int((pygame.time.get_ticks()/1000) - (time_tick/1000))
    score_surface = font.render(f"{current_time}", False, (64, 64, 64)).convert()
    score_rect = score_surface.get_rect(midtop = (window_width/2, 50))
    screen.blit(score_surface, score_rect)
    return current_time

def score_show():
    # Score Text
    score_text = font.render(f"SCORE: {get_score}", False, (111,196,169)).convert()
    score_text_rect = score_text.get_rect(midtop = (window_width/2, 320))
    screen.blit(score_text, score_text_rect)

def obs_move(obs_list):
    if obs_list:
        for obs_rect in obs_list:
            obs_rect.x -= v_snail
            
            screen.blit(snail, obs_rect)
            return obs_list
    else:
        return []
pygame.init()

# Main configs
window_width = 800
window_height = 400
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Questão 1")
clock = pygame.time.Clock()
font = pygame.font.Font("font/Pixeltype.ttf", 50)

# Sky
sky = pygame.image.load("graphics/Sky.png").convert()
sky_rect = sky.get_rect(topleft = (0,0))

# Ground
ground = pygame.image.load("graphics/ground.png").convert()
ground_ypos = 300

# starttitle
starttitle = font.render("Pixel Runner", False, (111, 196, 169)).convert()
starttitle_rect = starttitle.get_rect(midtop = (window_width/2, 10))

# Click text
clicktext = font.render("CLICK TO START", False, (111, 196, 169)).convert()
clicktext_rect = clicktext.get_rect(midtop = (window_width/2, 320))

# Player
player = pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
player_rect = player.get_rect(midbottom = (200, ground_ypos))
player_gravity = 0
jump = 0

# Player stand
player_stand = pygame.image.load("graphics/Player/player_stand.png").convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0, 2)
player_stand_rect = player_stand.get_rect(center = (window_width/2, window_height/2))


# Snail
snail = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rect = snail.get_rect(midbottom = (600, ground_ypos))
v_snail = 5

# Obstacles
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1000)

obstacle_rect_list = []

# Game States
game_running = False

# Operational Variables
time_tick = 0
get_score = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if game_running:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and jump == 0: # Ou and player_rect.bottom == ground.ypos
                    player_gravity -= 20
                    jump = 1
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and jump == 0: # Ou and player_rect.bottom == ground.ypos
                    player_gravity -= 20
                    jump = 1
            
            if event.type == obstacle_timer:
                obstacle_rect_list.append(snail.get_rect(midbottom = (randint(window_width, 1000), ground_ypos)))
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                game_running = True
                time_tick = pygame.time.get_ticks()
                snail_rect.midbottom = (600, ground_ypos)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_running = True
                    time_tick = pygame.time.get_ticks()
                    snail_rect.midbottom = (600, ground_ypos)
    
    if game_running:
        get_score = display_score()
        
        screen.blit(sky, (0,0))

        screen.blit(ground, (0, ground_ypos))

        screen.blit(player, player_rect)

        # screen.blit(snail, snail_rect)
        
        display_score()

        # snail_rect.left -= v_snail
        # if snail_rect.right <= 0:
        #     snail_rect.left = window_width
        
        # Obstacle move
        obstacle_rect_list = obs_move(obstacle_rect_list)
    
        # Player
        player_gravity += 1
        player_rect.y += player_gravity
        
        if player_rect.bottom >= ground_ypos:
            player_rect.bottom = ground_ypos
            player_gravity = 0
            jump = 0

        if player_rect.top <= 0:
            player_rect.top = 0
            player_gravity = 0
        
        # Game Over
        if snail_rect.colliderect(player_rect):
            game_running = False
    
    else:
        screen.fill((94, 129, 162))
        screen.blit(starttitle, starttitle_rect)
        screen.blit(player_stand, player_stand_rect)
        if get_score == 0:
            screen.blit(clicktext, clicktext_rect)
        else:
            score_show()
            
    pygame.display.update()
    clock.tick(60)