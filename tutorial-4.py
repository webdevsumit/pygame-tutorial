import pygame

pygame.init()

screen = pygame.display.set_mode((1000,1000))


pygame.display.set_caption('try pygame')

while True:
    
    
    screen.fill((0,0,255))
    
    
    pygame.draw.line(screen, (0,0,0),(0,0),(1000,1000),10)
    rect = pygame.draw.rect(screen, (0,0,0),(500,100,500,500),5,100)
    
    pygame.draw.polygon(screen, (255,0,0),((0,0),(100,100),(1000,0)),10)
    
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            break
            
    pygame.display.update()
    pygame.display.flip()
    
pygame.quit()
quit()