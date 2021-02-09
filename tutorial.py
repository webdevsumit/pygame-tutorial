import pygame

pygame.init()

size = width,height = 1400,1400

screen = pygame.display.set_mode(size)

pygame.display.set_caption('tutorial')

clock = pygame.time.Clock()

img = pygame.image.load('Ball.png')

game = True

msg = 'empty'

font = pygame.font.SysFont(None,64)
font_img = font.render(msg,True,(255,0,0))
font_rect = font_img.get_rect()
font_rect.center = (width/2,height/2)

while game:
    
    
    #evants
    for event in pygame.event.get():
        
        if event.type==pygame.QUIT:
            game=False
            
        if event.type==pygame.KEYDOWN:
            msg = str(event.key)
            
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            msg = str(event.pos)
                
                
                
    screen.fill((0,0,0))
    screen.blit(img,(0,0))
    
    font_img = font.render(msg,True,(255,0,0))
    screen.blit(font_img,font_rect)
    
    
    pygame.display.update() #display.update() allows to update a portion of the screen, instead of the entire area of the screen. Passing no arguments, updates the entire display
    
    pygame.display.flip() #display.flip() will update the contents of the entire display.
    
    clock.tick(30)
    
pygame.quit()
quit()
    