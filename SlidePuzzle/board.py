#board file 
import pygame
import random
import os

class Board:
    def __init__(self,game_size, tile_size, screen ):
        self.game_size= game_size   #size of the board  for (3x3) it would be 3 
        self.tile_size = tile_size  # size of the tiles 
        self.screen = screen   #the screen to draw the baoard such as the grids and tiles
        self.grid = self.create_grid() #creates the grid 
        self.moves_made = 0      #counts number of moves mades
        self.best_moves = 0    #stores best move


    def create_grid(self):
        grid = list(range(1,self.game_size**2))+[0]    #creates a list from 1 to (Games_size^2) -1 so 1 - 8 and adds a 0 to indicate an empty tile 
        return grid 
        
    def draw_grid(self):
        for row in range(self.game_size + 1):   #for row in range (3+1) so 0-4 so 4 lines with 
            pygame.draw.line(self.screen, (255,255,255),   #255,255,255 for the colour of the line , screen for the pygame surface
                             (250+ (row * self.tile_size), 150),   # the coordinates of the starting line (tile size is positon of the tile) row is incremented 
                             (250+(row * self.tile_size), 150+(self.game_size * self.tile_size))) # this is to indicate the position of the last line 
            #drwa lines for the row 
        
        for col in range(self.game_size+1):  #does the same for the columns but inversed co ordinates 
            pygame.draw.line(self.screen,(255,255,255), 
                             (250,(col*self.tile_size)+150), 
                             (250+ (self.game_size*self.tile_size),(col * self.tile_size)+150))      #draw lines for the columns 
    
    def draw_tiles(self):
            for row in range(self.game_size):  #so each row 0-2 which would be the coordinates
                for col in range(self.game_size): #so for each column which i used to indcate the coordinate
                    i = row * self.game_size + col      #convert the coordiantes to 1d so (0,0) 0*3*0 so first index 0 till you reach 3 
                    tile_value = self.grid[i] #this gets the tiles at the index so index 0 would be 1 
                    
                    if tile_value != 0:  #while its not empty draw the tiles 
                        x=250+col*self.tile_size #calcautes the  posiotn x coordiante of the tile 
                        y=150+row*self.tile_size  #clculates the positonn y coordiate of the tile 
                        pygame.draw.rect(self.screen, (255,255,255),(x,y, self.tile_size, self.tile_size)) #draws the box with the x and y being the coordiante for the top left then the tiles size being the width and height of the rectanlge 
                        pygame.draw.rect(self.screen, (0,0,0), (x,y,self.tile_size, self.tile_size),3) # and this is for the border of the tile showng 3 as the thickness of the nlack outlien 
                        
                        font=pygame.font.Font(None, 70)
                        text = font.render(str(tile_value), True, (190,0,250))
                        text_rect = text.get_rect(center=(x+self.tile_size/2, y + self.tile_size // 2))
                        self.screen.blit(text, text_rect)

    def get_empty_tile(self):
        empty_tile = self.grid.index(0)     # find the index of 0 which would be 8
        row= empty_tile//self.game_size     # if game_Size  is 3 , you would  8 // 3 =  2 so row = 2 
        col = empty_tile % self.game_size    # same for column
        return row,col  #return these two co ordinates 
    
    def check_move(self, direction):
        empty_row ,empty_col = self.get_empty_tile()     # (2,2)
        if direction == "up" and empty_row < self.game_size-1:   #if direction is up and if # empty row = 2 is less than 2 which is false #as empty tile isnt at the top its at the bottom im moving tiles adjacent to it 
            return empty_row+1 , empty_col   #move the tile above empty tile so empty tile would move down 
        elif direction == "down" and empty_row >0 :  # if the empty tile is not at the top 
            return empty_row-1, empty_col  #basically move the tile below and the empty tile above 
        elif direction == "left" and empty_col < self.game_size -1 :  #if the empty tile is not at the right most which would be 2  so less than 2 
            return empty_row, empty_col+1  #basically move the tiles to the left so empty tile moves right 
        elif direction == "right" and empty_col> 0:  #checks if the empty tile is  at the right most  so not at the left most
            return empty_row, empty_col-1  #tiles basically move to right as empty tile moevs to the left 
        
        return None
    
    def Move_Up(self):
        move_pos = self.check_move("up") #check if you can move up so if empty_index was(2,2) it would be the tuple (1,2)
        if move_pos:  #if not none 
            empty_index = self.grid.index(0)  #get index of the empty tile so if (8)
            swap_index = move_pos[0] * self.game_size + move_pos[1]  #so (1,2)  would 1*3+2 = 5 so swap index is 5 
            self.grid[swap_index], self.grid[empty_index] = self.grid[empty_index], self.grid[swap_index] #so swap 5 and 9
        
            self.Moves()
    #similar thing for the other moves 
    def Move_Down(self):
        move_pos = self.check_move("down")
        if move_pos:
            empty_index = self.grid.index(0) 
            swap_index = move_pos[0] * self.game_size+ move_pos[1]
            self.grid[swap_index], self.grid[empty_index] = self.grid[empty_index], self.grid[swap_index]
            self.Moves()
    
    def Move_Left(self):
        move_pos = self.check_move("left")
        if move_pos:
            empty_index = self.grid.index(0)
            swap_index = move_pos[0] * self.game_size + move_pos[1]
            self.grid[swap_index], self.grid[empty_index] = self.grid[empty_index], self.grid[swap_index]
            self.Moves()
    
    def Move_Right(self):#
        move_pos = self.check_move("right")
        if move_pos:
            empty_index = self.grid.index(0)
            swap_index = move_pos[0] * self.game_size + move_pos[1]
            self.grid[swap_index], self.grid[empty_index] = self.grid[empty_index], self.grid[swap_index]
            self.Moves()
    
    #create a mouse handling
    def mouse_handling(self, mouse_pos):
        mouse_pos_x,mouse_pos_y = mouse_pos  #gets coordiantes of the mouse posiotion and sets its to each of the varible 

        tile_col = (mouse_pos_x - 250) // self.tile_size # finds the grid coordiatnte using the offset 250 and 150 
        tile_row = (mouse_pos_y -150)  // self.tile_size  #example  if cicked at (350,250) for 3x3
        # 350 - 250 // 100 = 1 and 250-150// = 1 therofore it would be at row 1 col 1
        if (0<= tile_col<self.game_size and 0<= tile_row <self.game_size): #ensure that its within the board 
            #by evaualting time grid cooridante where it must be bigger or equal to 0 and less or equal to maxium row,col
            #eg 3x3   0<tile_col<3
            empty_index = self.grid.index(0)  #index 0 on the grid is the empty tile which it set to index
            #find the positon of the empty index  #eg index 4 on 3x3
            empty_row = empty_index // self.game_size  # 4//3 = 1
            empty_col = empty_index % self.game_size   # 4 % 3 = 1 row 1 col 1

            #calcualtes the distance  eg  empty 2,1 and tile 1,1  so adjacent would be 
            adjacent_row = abs(tile_row - empty_row) #1 abs makes sure there are no negatives 
            adjacent_col = abs(tile_col - empty_col) #0   
            #must be (0,1) or (1,0)   basically must be able to move in a direction     
            if (adjacent_row == 1 and adjacent_col == 0) or (adjacent_col == 1 and adjacent_row == 0 ):
                if tile_row < empty_row:   #if its above so [1] e.g(1,3) so row 1 
                    self.Move_Down()                       #[x]     (2,3) so row 2 so it calls move down 
                elif tile_row > empty_row:  
                    self.Move_Up()                          #logic is similar but to their respecitve positions
                elif tile_col < empty_col :
                    self.Move_Right()
                elif tile_col > empty_col:
                    self.Move_Left()
            
                return True  #returns true showing that tile has moveed
            return False # other wise tile hasnt moved 
                

                








    def shuffle(self):
        for i in range(100): # shuffles the board 100 times
            direction = random.choice(["up","down","left","right"]) #direction is set to a random move every time till for loop ends
            #moves correspoinding to the random choice 
            if direction == "up":
                self.Move_Up()
            if direction == "down":
                self.Move_Down()
            if direction == "left":
                self.Move_Left()
            if direction == "right":
                self.Move_Right()
            
            self.reset_Moves_Made()


    def check_win(self):
        solved = list(range(1, self.game_size ** 2))+[0]
        if self.grid == solved:  #if list grid  == solved list 
            self.best_moves_made() #calcuate call on best move Made  and return true 
            return True 
        return False
    
    def Moves(self): #counts moves made 
        self.moves_made += 1 #increments moves made every time moves procedure is called 
        return self.moves_made #updates moves mades each time and returns it
    
    def reset_Moves_Made(self):
        self.moves_made = 0  #resets moves made by eqauting it to 0
    
    def best_moves_made(self):
        if self.best_moves == 0 or self.best_moves > self.moves_made: # if best move = 0 or  moves made is less than best moves 
            self.best_moves = self.moves_made # equates moves made to best moves made if the condition is met  
    
    def reset_best_moves(self):
        self.best_moves = 0

    def get_current_state(self):
        return self.grid.copy() #returns of current grid 
    

    
    def set_grid(self, new_state):
        self.grid = new_state #set the grid to new stae   

    
