import pygame

pygame.init()

size = width,height = 2200,800

screen = pygame.display.set_mode(size)

pygame.display.set_caption('tutorial')

clock = pygame.time.Clock()

img = pygame.image.load('Ball.png')
img = pygame.transform.scale(img,[100,100])

img_rect = img.get_rect()
img_rect.left=0
img_rect.top=0

img_rect2 = img.get_rect()
img_rect2.left=400
img_rect2.top=0

speed = [10,10]
speed2 = [30,30]



game = True

msg = 'empty'

font = pygame.font.SysFont(None,64)
font_img = font.render(msg,True,(255,0,0))
font_rect = font_img.get_rect()
font_rect.center = (width/2,height/2)

sound = pygame.mixer.Sound('Bi.mp3')
#pygame.mixer.Sound.play(sound)

pygame.mixer.music.load('Bi.mp3')
#pygame.mixer.music.play(-1)

while game:
    
    screen.fill((0,0,0))
    
    #evants
    for event in pygame.event.get():
        
        if event.type==pygame.QUIT:
            game=False
            
        if event.type==pygame.KEYDOWN:
            msg = str(event.key)
            
            if event.key==pygame.K_UP:
                speed[1]=-30
            
            if event.key==pygame.K_p:
                pygame.mixer.music.pause()
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            msg = str(event.pos)
                
    if img_rect.left < 0 or img_rect.right > width:
        speed[0]=-speed[0]
            
    if img_rect.top < 0 or img_rect.bottom > height:
        speed[1]=-speed[1]
        
    if img_rect2.left < 0 or img_rect2.right > width:
        speed2[0]=-speed2[0]
            
    if img_rect2.top < 0 or img_rect2.bottom > height:
        speed2[1]=-speed2[1]
        
    if img_rect.colliderect(img_rect2):
        
        speed[0],speed2[0]=speed2[0],speed[0]
        
        if speed[1]==0 or speed2[1]==0:
            pass
        else:
            speed[1],speed2[1]=speed2[1],speed[1]
            
        
    speed[1] = speed[1]+5
    speed2[1] = speed2[1]+5
    
    if img_rect.bottom>height and speed[1]>(-30) and speed[1]<30 :
        speed[1]=0
        
        if speed[0]==0:
            pass
        elif speed[0]<0:
            speed[0] += 0.2
        else:
            speed[0] -= 0.2
        
    if img_rect2.bottom>height and speed2[1]>(-30) and speed2[1]<30 :
        speed2[1]=0
        
        if speed2[0]==0:
            pass
        elif speed2[0]<0:
            speed2[0] += 0.2
        else:
            speed2[0] -= 0.2
    
    img_rect = img_rect.move(speed)
    screen.blit(img,img_rect)
    
    img_rect2 = img_rect2.move(speed2)
    screen.blit(img,img_rect2)
    
    font_img = font.render(msg,True,(255,0,0))
    screen.blit(font_img,font_rect)
    
    pygame.draw.line(screen, (255,255,255),(0,height+20),(width,height+20))
    
    pygame.display.update() #display.update() allows to update a portion of the screen, instead of the entire area of the screen. Passing no arguments, updates the entire display
    
    pygame.display.flip() #display.flip() will update the contents of the entire display.
    
    clock.tick(30)
    
pygame.quit()
quit()
    