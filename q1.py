import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1080, 540))
pygame.display.set_caption("Primeiro exercício")
clock = pygame.time.Clock()
a = pygame.Surface((200,100))
a.fill("blue")

while True:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            exit()
            
    clock.tick(60)
    screen.blit(a, (200, 100))
    pygame.display.update()