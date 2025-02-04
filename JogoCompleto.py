import pygame
from sys import exit
from random import randint, choice

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk_1 = pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
        player_walk_2 = pygame.image.load("graphics/Player/player_walk_2.png").convert_alpha()
        self.player_walk = [player_walk_1, player_walk_2]
        self.player_jump = pygame.image.load("graphics/Player/jump.png").convert_alpha()

        self.player_index = 0
        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (100, ground_ypos))
        self.gravity = 0
        self.jump = 0
        self.speed = 4
        self.jump_sound = pygame.mixer.Sound("audio/jump.mp3")
        self.jump_sound.set_volume(0.1)
        
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.jump == 0:
            self.gravity = -20
            self.jump = 1
            self.jump_sound.play()
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rect.x +=  self.speed
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rect.x -=  self.speed
            
    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= ground_ypos:
            self.rect.bottom = ground_ypos
            self.jump = 0
            
    def out_window(self):
        if self.rect.left > window_width:
            self.rect.right = 0
        if self.rect.right < 0:
            self.rect.left = window_width
            
    def player_animation(self):
        keys_player = pygame.key.get_pressed()
        if self.rect.bottom < ground_ypos:
            self.image = self.player_jump
        else:
            self.image = self.player_walk[0]
            if keys_player[pygame.K_d] or keys_player[pygame.K_RIGHT] or keys_player[pygame.K_a] or keys_player[pygame.K_LEFT]:
                self.player_index += 0.2
                self.image = self.player_walk[int(self.player_index%len(self.player_walk))]
    
    def player_return_pos(self):
        self.rect.x = 100
        
    def update(self):
        if game_running:
            self.player_input()
            self.apply_gravity()
            self.out_window()
            self.player_animation()
        else:
            self.player_return_pos()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        
        if type == "snail":
            snail1 = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
            snail2 = pygame.image.load("graphics/snail/snail2.png").convert_alpha()
            self.frames = [snail1, snail2]
            ypos = ground_ypos
            self.speed = 5
            
        if type == "fly":
            fly1 = pygame.image.load("graphics/fly/fly1.png").convert_alpha()
            fly2 = pygame.image.load("graphics/fly/fly2.png").convert_alpha()
            self.frames = [fly1, fly2]
            ypos = ground_ypos - 150
            self.speed = 7
            
        self.index = 0
        self.image = self.frames[self.index]
        self.rect = self.image.get_rect(midbottom = (randint(900, 1100), ypos))
    
    def animation(self):
        self.index += 0.1
        self.image = self.frames[int(self.index%len(self.frames))]
    
    def destroy(self):
        if self.rect.x <= -100:
            self.kill()
            
    def update(self):
        self.animation()
        self.rect.x -= self.speed
        self.destroy()
            
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

def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        obstacle_group.empty()
        return False     
    else:
        return True
    
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
player = pygame.sprite.GroupSingle()
player.add(Player())

# Player stand   
player_stand = pygame.image.load("graphics/Player/player_stand.png").convert_alpha() 
player_stand = pygame.transform.rotozoom(player_stand,0, 2)
player_stand_rect = player_stand.get_rect(center = (window_width/2, window_height/2))

# Obstacles
obstacle_timer = pygame.USEREVENT + 1
time_s = 1500
pygame.time.set_timer(obstacle_timer, time_s)

obstacle_group = pygame.sprite.Group()

# Game States
game_running = False

# Operational Variables
time_tick = 0
get_score = 0
speed_timer = pygame.USEREVENT + 2
pygame.time.set_timer(speed_timer, 5000)
bg_music = pygame.mixer.Sound("audio/music.wav")
bg_music.set_volume(0.05)
play = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if game_running:            
            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle(choice(["snail", "fly", "snail"])))           
        else:
            if event.type == pygame.MOUSEBUTTONDOWN or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
                game_running = True
                time_tick = pygame.time.get_ticks()
            
    
    if game_running:
        if play:
            bg_music.play(loops=-1)
            play = False
        screen.blit(sky, (0,0))

        screen.blit(ground, (0, ground_ypos))

        player.draw(screen)
        player.update()
        obstacle_group.draw(screen)
        obstacle_group.update()

        display_score()
        
        game_running = collision_sprite()

    else:
        bg_music.stop()
        screen.fill((94, 129, 162))
        screen.blit(starttitle, starttitle_rect)
        screen.blit(player_stand, player_stand_rect)
        time_s = 1500
        player.update()
        pygame.time.set_timer(speed_timer, 5000)
        if get_score == 0:
            screen.blit(clicktext, clicktext_rect)
        else:
            score_show()
        play = True
            
    pygame.display.update()
    clock.tick(60)