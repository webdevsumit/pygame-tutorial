#part-5
import pygame

pygame.init()

screen = pygame.display.set_mode((1000,1000))

width = screen.get_width()
height = screen.get_height()
Clock = pygame.time.Clock()
pygame.display.set_caption('Join the dots')


font96 = pygame.font.SysFont(None,96)
font72 = pygame.font.SysFont(None,72)
font64 = pygame.font.SysFont(None,64)
font56 = pygame.font.SysFont(None,56)

def main_screen():
    main = True
    while main:
        screen.fill((0,0,255))
        
        
        
        pygame.display.update()
        pygame.display.flip()
        Clock.tick(30)


def hero_page():
    hero = True
    
    while hero:
        
        
        screen.fill((170,170,170))
        
        head_img = font96.render('Join the dots',True,(0,0,0))
        head_img_rect = head_img.get_rect()
        head_img_rect.center = (width/3,height/4)
        screen.blit(head_img,head_img_rect)
        
        des_img = font56.render('Line Vs Line',True,(0,0,0))
        des_img_rect = des_img.get_rect()
        des_img_rect.center = (width/3+90,height/4+60)
        screen.blit(des_img,des_img_rect)
        
        start_btn_rect = pygame.draw.rect(screen,(255,255,255),(width/4,height/2,200,100),10,20)
        
        start_btn_text = font72.render('start',True,(255,255,255))
        start_btn_text_rect = start_btn_text.get_rect()
        start_btn_text_rect.center = start_btn_rect.center
        screen.blit(start_btn_text,start_btn_text_rect)
        
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                hero = False
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0]>start_btn_rect.x and event.pos[1]>start_btn_rect.y and event.pos[0]<(start_btn_rect.x+start_btn_rect.width) and event.pos[1]<(start_btn_rect.y+start_btn_rect.height):
                    main_screen()
                
        pygame.display.update()
        pygame.display.flip()
        Clock.tick(30)
    pygame.quit()
    
hero_page()