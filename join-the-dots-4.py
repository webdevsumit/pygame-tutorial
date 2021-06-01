#part-8
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

def main_screen(no_of_dots):
    
    main = True
    player1_score = 0
    player2_score = 0
    
    dots_arr = []
    mouse_pos = []
    line_arr = []
    line_width = width/(no_of_dots+1)
    line_height = (height-100)/(no_of_dots+1)
    
    for i in range(1,no_of_dots+1):
        temp_arr = []
        for j in range(1,no_of_dots+1):
            temp_arr.append([line_width*j,line_height*i+100])
        dots_arr.append(temp_arr)
    
    while main:
        mouse_pos = pygame.mouse.get_pos()
        screen.fill((170,170,170))
        
        player1_text = font72.render('player 1 : '+str(player1_score),True,(155,0,0))
        player1_text_rect = player1_text.get_rect()
        player1_text_rect.center = (200,100)
        screen.blit(player1_text,player1_text_rect)
        
        player2_text = font72.render('player 2 : '+str(player2_score),True,(0,0,255))
        player2_text_rect = player2_text.get_rect()
        player2_text_rect.center = (width-200,100)
        screen.blit(player2_text,player2_text_rect)
        
        dots_text = font72.render('No of dots : '+str(no_of_dots)+'x'+str(no_of_dots),True,(255,255,255))
        dots_text_rect = dots_text.get_rect()
        dots_text_rect.center = (width/2,100)
        screen.blit(dots_text,dots_text_rect)
        
        for in_arr in dots_arr:
            for cord in in_arr:
                pygame.draw.circle(screen,(0,0,0),cord,5)
                
        for i in range(no_of_dots):
            for j in range(no_of_dots-1):
                cord = dots_arr[i][j]
                hr_next_cord = dots_arr[i][j+1]
                
                if mouse_pos[0]>cord[0] and mouse_pos[0]<hr_next_cord[0] and mouse_pos[1]>cord[1]-30 and mouse_pos[1]<cord[1]+30 :
                    pygame.draw.line(screen,(0,0,0),cord,hr_next_cord)
                    
        for i in range(no_of_dots-1):
            for j in range(no_of_dots):
                cord = dots_arr[i][j]
                vr_next_cord = dots_arr[i+1][j]
                    
                if mouse_pos[1]>cord[1] and mouse_pos[1]<vr_next_cord[1] and mouse_pos[0]>cord[0]-30 and mouse_pos[0]<cord[0]+30 :
                    pygame.draw.line(screen,(0,0,0),cord,vr_next_cord)           
         
        for cord_arr in line_arr:
            pygame.draw.line(screen,(0,0,0),cord_arr[0],cord_arr[1],5)
         
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                hero = False
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(no_of_dots):
                    for j in range(no_of_dots-1):
                        cord = dots_arr[i][j]
                        hr_next_cord = dots_arr[i][j+1]
                        
                        if event.pos[0]>cord[0] and event.pos[0]<hr_next_cord[0] and event.pos[1]>cord[1]-30 and event.pos[1]<cord[1]+30 :
                            line_arr.append([cord,hr_next_cord])
                            
                            
                for i in range(no_of_dots-1):
                    for j in range(no_of_dots):
                        cord = dots_arr[i][j]
                        vr_next_cord = dots_arr[i+1][j]
                            
                        if event.pos[1]>cord[1] and event.pos[1]<vr_next_cord[1] and event.pos[0]>cord[0]-30 and event.pos[0]<cord[0]+30 :
                            line_arr.append([cord,vr_next_cord])
                
        pygame.display.update()
        pygame.display.flip()
        Clock.tick(30)


def hero_page():
    hero = True
    no_of_dots = 4
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
        up_btn_rect = pygame.draw.rect(screen,(255,255,255),(width/2+100,height/2-100,100,100),10,20)
        down_btn_rect = pygame.draw.rect(screen,(255,255,255),(width/2+100,height/2+100,100,100),10,20)
        
        start_btn_text = font72.render('start',True,(255,255,255))
        start_btn_text_rect = start_btn_text.get_rect()
        start_btn_text_rect.center = start_btn_rect.center
        screen.blit(start_btn_text,start_btn_text_rect)
        
        dots_text = font72.render('No of dots : '+str(no_of_dots)+'x'+str(no_of_dots),True,(255,255,255))
        dots_text_rect = dots_text.get_rect()
        dots_text_rect.center = (width/2,height/2+50)
        screen.blit(dots_text,dots_text_rect)
        
        up_btn_text = font96.render('-',True,(255,255,255))
        up_btn_text_rect = up_btn_text.get_rect()
        up_btn_text_rect.center = up_btn_rect.center
        screen.blit(up_btn_text,up_btn_text_rect)
        
        down_btn_text = font96.render('+',True,(255,255,255))
        down_btn_text_rect = down_btn_text.get_rect()
        down_btn_text_rect.center = down_btn_rect.center
        screen.blit(down_btn_text,down_btn_text_rect)
        
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                hero = False
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0]>start_btn_rect.x and event.pos[1]>start_btn_rect.y and event.pos[0]<(start_btn_rect.x+start_btn_rect.width) and event.pos[1]<(start_btn_rect.y+start_btn_rect.height):
                    pygame.draw.rect(screen,(255,255,255),(width/4,height/2,200,100),100,20)
                    main_screen(no_of_dots)
                    
                if event.pos[0]>up_btn_rect.x and event.pos[1]>up_btn_rect.y and event.pos[0]<(up_btn_rect.x+up_btn_rect.width) and event.pos[1]<(up_btn_rect.y+up_btn_rect.height) and no_of_dots>3:
                    pygame.draw.rect(screen,(255,255,255),(width/2+100,height/2-100,100,100),100,20)
                    no_of_dots -= 1
                    
                if event.pos[0]>down_btn_rect.x and event.pos[1]>down_btn_rect.y and event.pos[0]<(down_btn_rect.x+down_btn_rect.width) and event.pos[1]<(down_btn_rect.y+down_btn_rect.height) and no_of_dots<10:
                    pygame.draw.rect(screen,(255,255,255),(width/2+100,height/2+100,100,100),100,20)
                    no_of_dots += 1
                    
                
        pygame.display.update()
        pygame.display.flip()
        Clock.tick(30)
    pygame.quit()
    
hero_page()