#Button file
import pygame

class Button():
    def __init__(self,x_pos, y_pos, text_input, font=None, base_color=(0,255,255), hovering_color=(255,255,255), image=None, width  = 200, height = 50):
        
        self.x_pos = x_pos #horizontal positon 
        self.y_pos = y_pos  #vetical postion
        self.text_input = text_input  # textt for dipslay
        self.font = font if font else pygame.font.Font(None,30)   #specifc font if not use the defualt pygame font 
        self.base_color = base_color      #inital colour
        self.hovering_color=hovering_color  #hovering state colour 
        self.image=image  # image for the button or none 
        self.text_color=base_color #initail colour of the text 
        self.width= width   # width of the button in pixel
        self.height= height  # height of the button in pixels 

        if self.image:  #if there is an image 
            self.image = pygame.transform.scale(self.image, (self.width,self.height)) # scale image with the dimesion given)
            self.rect = self.image.get_rect(topleft=(x_pos, y_pos)) # gets the rectngle collsion dection  for mouse  using thoes positioning 
        else: # if not 
            self.rect = pygame.Rect(x_pos, y_pos, self.width,self.height) #create the colsion with the dimension without image 

        
    def draw(self, screen): 
        if self.image: # if there is an image 
            screen.blit(self.image, (self.x_pos, self.y_pos)) #place the button image at the x and y psition 
        else: # if not 
            pygame.draw.rect(screen, self.base_color, self.rect) #raw a solid rectangle with the inital colour 
        if self.text_input: # if there is a text input 
            text_surface = self.font.render(self.text_input, True, self.text_color)  #rednder the text with its colour  and if bold set to ture 
            text_rect = text_surface.get_rect(center=self.rect.center) #places button on the centre of the text 
            screen.blit(text_surface, text_rect)  #draws the text with its colour on the screen
    
    
        
        
        
    def check_for_input(self,position):  
        if self.rect.left<= position[0] <=self.rect.right and self.rect.top <= position[1] <= self.rect.bottom:  #if mouse position is within the bonds of the button 
            return True #return true 
        return False #return false 



    def color(self, position,normal_color,hovering_color):
        self.text_color = hovering_color if self.check_for_input(position) else normal_color  # set to hovering colour if true othewise noram color 
