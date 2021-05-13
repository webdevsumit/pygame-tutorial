import pygame

pygame.init()

size = width,height = 2200,800

screen = pygame.display.set_mode(size)

pygame.display.set_caption('tutorial')

clock = pygame.time.Clock()

img = pygame.image.load('Ball.png')

img_rect = img.get_rect()
img_rect.left=0
img_rect.top=0



speed = [20,20]




game = True

msg = 'empty'

font = pygame.font.SysFont(None,64)
font_img = font.render(msg,True,(255,0,0))
font_rect = font_img.get_rect()
font_rect.center = (width/2,height/2)

sound = pygame.mixer.Sound('Bi.mp3')
#pygame.mixer.Sound.play(sound)

pygame.mixer.music.load('Bi.mp3')
pygame.mixer.music.play(-1)

while game:
    
    screen.fill((0,0,0))
    
    #evants
    for event in pygame.event.get():
        
        if event.type==pygame.QUIT:
            game=False
            
        if event.type==pygame.KEYDOWN:
            msg = str(event.key)
            
            if event.key==pygame.K_p:
                pygame.mixer.music.pause()
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            msg = str(event.pos)
                
    if img_rect.left < 0 or img_rect.right > width:
        speed[0]=-speed[0]
            
    if img_rect.top < 0 or img_rect.bottom > height:
        speed[1]=-speed[1]
        
    img_rect = img_rect.move(speed)
    screen.blit(img,img_rect)
    
    
    font_img = font.render(msg,True,(255,0,0))
    screen.blit(font_img,font_rect)
    
    
    pygame.display.update() #display.update() allows to update a portion of the screen, instead of the entire area of the screen. Passing no arguments, updates the entire display
    
    pygame.display.flip() #display.flip() will update the contents of the entire display.
    
    clock.tick(30)
    
pygame.quit()
quit()
    