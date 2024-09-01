import pygame
pygame.init()
window = pygame.display.set_mode((400,400))
window.fill((255,255,255,255))
green = (0,255,0)
pygame.draw.circle(window,green,(100,100),50,3)
pygame.draw.rect(window,(0,125,255),pygame.Rect(300,300,60,60))
pygame.display.update()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
