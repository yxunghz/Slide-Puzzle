#Option file 
import pygame
import os
import sys
from Button import Button



BASE_DIR = os.path.dirname(__file__)
pygame.font.init()
width, height = 400,500
screen = pygame.display.set_mode((width,height))
background = pygame.image.load(os.path.join(BASE_DIR,"images", "Stars.jpg"))
background = pygame.display.set_mode((width, height))

background_image = {"Stars": pygame.image.load(os.path.join(BASE_DIR, "images", "Stars.jpg")),  
                    "White_Stars": pygame.image.load(os.path.join(BASE_DIR, "images", "White_Stars.jpg")), }

background_options =["Stars", "White_Stars"]  #list of background options
selected_background = background_options[0]  # defualt selected backgorund option
dropdown_open = False  # if dropdown is open or not which is false 
dropdown_rect = pygame.Rect(300,250,200,40)   # main position of the dropdown button



def get_Font(size=24 ,bold=False ,italic=False, font_name=None):
    font_name = font_name or pygame.font.match_font("arial")
    font = pygame.font.SysFont(font_name, size)
    font.set_bold(bold)
    font.set_italic(italic)
    return font

def background_dropdown():
        global dropdown_open, selected_background #golobal variable to be accessed 
        font = get_Font(size = 24, bold = True)    #set font for the dropdown text
        pygame.draw.rect(screen, (50,50,50), dropdown_rect)   #draw main dropdown button
        pygame.draw.rect(screen, (255,255,255), dropdown_rect, 2)  #outline of the dropdown 
        base_x = dropdown_rect.x  #coordinates of the dropdown 
        base_y = dropdown_rect.y  #
        text = font.render(selected_background, True,(255,255,255)) #render the current background 
        screen.blit(text, (base_x +10, base_y +8))  # position text 

        if dropdown_open:
            for i, option in enumerate(background_options):
                 background_rect = pygame.Rect(base_x, base_y + (i+1)*40, dropdown_rect.width, 40)
                 pygame.draw.rect(screen, (80, 80,80), background_rect)
                 pygame.draw.rect(screen, (255,255,255), background_rect, 1)
                 text = font.render(option, True, (255,255,255))
                 screen.blit(text,(background_rect.x + 10, background_rect.y + 8))


def information():
    done = False
    Neon_Image_Button = pygame.image.load(os.path.join(BASE_DIR,"images", "Neon_Button.png")).convert_alpha()
    Neon_Image_Button = pygame.transform.scale(Neon_Image_Button, (200,50)) 
    while not done:
        screen.fill((0,0,0))

        info_font = get_Font(24)
        information1= info_font.render(("To play this game you have to get the tiles in order"), True, (255,255,255))
        information2 = info_font.render(("using the empty tile to help move adjacent tiles to reach orderd grid."), True, (255,255,255))
        information3 = info_font.render(("\n uses arrow/w,a,s,d keys or left mouse click to move tiles to the empty position."), True, (255,255,255))
        
        screen.blit(information1, (100,100))
        screen.blit(information2, (100,130))
        screen.blit(information3, (100,160))

        Back_B=Button(600,500,"Back",font=get_Font(35),base_color=(255,0,255),hovering_color=(255,255,255), image = Neon_Image_Button)
        Back_B.draw(screen)

        Menu_Mouse_Pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Back_B.check_for_input(Menu_Mouse_Pos):
                    done = True
        pygame.display.update()
    
            

   


    

     

        
        


def options():
    global dropdown_open, selected_background
    x=0
    Done=False
    y=0
    
    Neon_Image_Button = pygame.image.load(os.path.join(BASE_DIR,"images", "Neon_Button.png")).convert_alpha()
    Neon_Image_Button = pygame.transform.scale(Neon_Image_Button, (200,50))

    info_image_button = pygame.image.load(os.path.join(BASE_DIR, "images","information.png")).convert_alpha()
    info_image_button = pygame.transform.scale(info_image_button,(64,64))
        
    while not Done:
        y+=1
        if y==height:
            y=0
        clock=pygame.time.Clock() 
        screen.fill((0,0,0))
        screen.blit(background,(x,y))
        screen.blit(background, (x,y-height))
        clock.tick(60)

        
        font3=get_Font(40, bold=True,font_name=None)
        text3=font3.render("option", True, (255,255,255))
        text3_rect=text3.get_rect(center=(400,100))
        screen.blit(text3, text3_rect)

        info_button = Button(650,50,"",font=get_Font(20),base_color=None, hovering_color=None, image= info_image_button, width = 64, height = 64 )
        info_button.draw(screen)


        back_button = Button(600,500, "Back", font=get_Font(35),base_color=(255,0,0), hovering_color=(255,255,255), image=Neon_Image_Button)
        back_button.draw(screen)


        background_dropdown()







        Menu_Mouse_Pos= pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if info_button.check_for_input(Menu_Mouse_Pos):
                     information()
                if back_button.check_for_input(Menu_Mouse_Pos):
                    return selected_background
                if dropdown_rect.collidepoint(Menu_Mouse_Pos):
                    if dropdown_open:
                        dropdown_open = False
                    else:
                            dropdown_open = True
                elif dropdown_open:
                     for i, option in enumerate(background_options):
                          option_rect = pygame.Rect(dropdown_rect.x, dropdown_rect.y + (i+1)*40, dropdown_rect.width, 40)
                          
                          if option_rect.collidepoint(Menu_Mouse_Pos):
                               selected_background = option
                               dropdown_open = False
                               break
                          else:
                            dropdown_open = False

        


        
        pygame.display.update()





for event in pygame.event.get():
    if event.type == pygame.QUIT:
        pygame.quir()
        sys.exit()



