#main file 
import pygame
import os 
import sys 
from timer import Timer 
from board import Board
from Options import options, background_image, background_options
from Button import Button
from AStarSolver import AStarSolver, show_hint
BASE_DIR = os.path.dirname(__file__)

pygame.init()
pygame.font.init()

width, height = 800, 600  #window dimension
screen = pygame.display.set_mode((width,height))  #create the surface
pygame.display.set_caption("Think Smarter") 

selected_background = "Stars"  # selected background for initial
background = pygame.transform.scale(background_image[selected_background], (width,height)) #scale the background image with the dimensions of the screen 


def get_Font(size=24 ,bold=False ,italic=False, font_name=None):   
    font_name = font_name or pygame.font.match_font("arial")  #defualt font or arial 
    font = pygame.font.SysFont(font_name, size) # create font
    font.set_bold(bold)  #bold or not 
    font.set_italic(italic) #allows italics if mentioned 
    return font 

def scrolling_background(selected_background,x,y):  #background scrolling effect
    if selected_background == "White_Stars":  #if background is the option white/stars
        return 0,0  #dont scroll 
    else:  #otherwise 
        y+= 1   #move background 1 pixel down
        if y >= height: 
            y=0   #when scrolled to full, height its reset
        return x,y
    

def information():
    done = False
    Neon_Image_Button = pygame.image.load(os.path.join(BASE_DIR,"images", "Neon_Button.png")).convert_alpha()
    Neon_Image_Button = pygame.transform.scale(Neon_Image_Button, (200,50)) 
    while not done:
        x,y = 0,0 
        x,y = scrolling_background(selected_background,x,y)  #create the scrolling background
        screen.blit(background,(0,y))
        screen.blit(background, (0,y-height))

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
    
            



    
    



def Menu():
    x=0
    y=0
    while True:
        x , y = scrolling_background(selected_background, x,y )  #constantly updates a scroll
        #draw two scrolling background for seamless looping 
        screen.blit(background, (0,y)) 
        screen.blit(background, (0,y-height))   

        #title is created and positioned 
        font = get_Font(40, bold=True, font_name=None)   
        heading = font.render(( "Welcome To Number slide puzzle"), True, (255,255,255))       
        heading_rect= heading.get_rect(center=(400,100))
        #text is created and postioned 
        font2 = get_Font(40, italic=True, font_name=None)
        text1 = font2.render(("Press Any Key To Start"), True, (255,255,255))
        text2_rect = text1.get_rect(center=(400,300))
        #drawn so they can be displayed 
        screen.blit(heading, heading_rect)
        screen.blit(text1, text2_rect)
        
        #event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit
            if event.type == pygame.KEYDOWN: #if any key is pressed
                create_Menus() #move to main menu
        pygame.display.update()  #updates the display screen


def create_Menus(): 
    global background, selected_background  #access global variable backgorund 
    Done=False  
    x=0
    y=0
    #neon buttons  image are loaded and scaled 
    Neon_Image_Button = pygame.image.load(os.path.join(BASE_DIR,"images", "Neon_Button.png")).convert_alpha()
    Neon_Image_Button = pygame.transform.scale(Neon_Image_Button, (200,50)) 
    while not Done:
        #scrolling effect again 
        x , y = scrolling_background(selected_background, x,y )
        screen.blit(background, (0,y))
        screen.blit(background, (0,y-height))



        #create neon buttons for menu
        Play_B= Button(300,200,"Play", font=get_Font(80),base_color=(255,0,0), hovering_color=(255,255,255), image=Neon_Image_Button)
        Option_B = Button(300,300, "Option", font = get_Font(80), base_color=(0,0,128), hovering_color=(255,255,255), image=Neon_Image_Button)
        Quit_B = Button(300,400, "Quit",font=get_Font(80), base_color=(255,0,0), hovering_color=(255,255,255), image= Neon_Image_Button)
        #updates button colour based on mouse position
        Menu_Mouse_Pos = pygame.mouse.get_pos()
        Play_B.color(Menu_Mouse_Pos, (0,0,0), (255,255,255))
        Option_B.color(Menu_Mouse_Pos, (255,0,0), (255,255,255))
        Quit_B.color(Menu_Mouse_Pos,(0,0,0), (255,255,255))

        #draw button on screen
        Play_B.draw(screen)
        Option_B.draw(screen)
        Quit_B.draw(screen)
        #evemt handiling
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN: #if mouse is clicked 
                if Play_B.check_for_input(Menu_Mouse_Pos): # check if its hovered on  play 
                    play() #goes play procedure which get the user to set diffuclty 
                if Option_B.check_for_input(Menu_Mouse_Pos):
                    selected_background = options() # go to option menu basically goes to setting screen
                    background  = pygame.transform.scale(background_image[selected_background], (width,height) ) #update the background after you leave option
                    
                if Quit_B.check_for_input(Menu_Mouse_Pos):
                    pygame.quit()
                    sys.exit()
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

#diffculty selection menu
def play():
    Done=False
    x=0
    y=0
    Neon_Image_Button = pygame.image.load(os.path.join(BASE_DIR,"images", "Neon_Button.png")).convert_alpha()
    Neon_Image_Button = pygame.transform.scale(Neon_Image_Button, (200,50))
    while not Done:
        x , y = scrolling_background(selected_background, x,y )
        screen.blit(background, (0,y))
        screen.blit(background, (0,y-height))
        #title text
        font3= get_Font(24, bold=True, font_name=None)
        text3= font3.render("Think Smarter", True, (255,255,255))
        text3_rect= text3.get_rect(center=(400,100))
        screen.blit(text3, text3_rect)

        #creates diffculty buttons 

        Back_B=Button(600,500,"Back",font=get_Font(35),base_color=(255,0,255),hovering_color=(255,255,255), image = Neon_Image_Button)
        Back_B.draw(screen)

        Easy_B= Button(300,200,"Easy(3*3)", font=get_Font(35), base_color=(255,0,172), hovering_color=(255,255,255), image=Neon_Image_Button )
        Medium_B = Button(300,300,"Medium(4*4)", font=get_Font(35),base_color=(255,000,172), hovering_color = (255,255,255), image=Neon_Image_Button)
        Hard_B = Button(300,400, "Hard(5*5)",font=get_Font(35), base_color=(255,0,175), hovering_color=(255,255,255),image=Neon_Image_Button)
        Custom_B= Button(300,500,"Custom", font=get_Font(35), base_color=(255,255,255), hovering_color=(255,255,255), image=Neon_Image_Button )
        #draws buttons
        Easy_B.draw(screen)
        Hard_B.draw(screen)
        Medium_B.draw(screen)
        Custom_B.draw(screen)

        #event handling 
        Menu_Mouse_Pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Easy_B.check_for_input(Menu_Mouse_Pos):
                    Game(100,3,screen)   #starts a 3x3
                    
                    
                if Medium_B.check_for_input(Menu_Mouse_Pos):
                
                    Game(90,4,screen)  #starts a 4x4 
                    
                    
                if Hard_B.check_for_input(Menu_Mouse_Pos):
                    Game(70,5,screen)   #starts 5x5
                    
                
                if Back_B.check_for_input(Menu_Mouse_Pos):
                    return #returns to main menu
                
                    

                if Custom_B.check_for_input(Menu_Mouse_Pos):  
                    custom = False  #custom is set to false
                    while not custom:  # while not false / while True
                        try: # try 
                            size = int(input('enter board size (6-10): ')) #size which only except intergers which user inputs
                            if size > 5 and size <= 10: #if size is greater than 5 and less that or equal to 10 than 
                                scale_size = int(100*(3/size)) #scale the size of the board
                                custom = True
                            else:
                                print("enter a integer between thoes boundaries")
                        except ValueError:
                            print("enter a a valid number")
                    Game(scale_size, size, screen)
                
        pygame.display.update()
                


def Game(tile_size,game_size,screen): #arguments are passed for the board 
    
    Done=False
    x=0
    y=0
    
    timer = Timer()  #timer is initialised 

     #first move is made is set to false 
    #loads neon button images 

    Neon_Button_Image= pygame.image.load(os.path.join(BASE_DIR,"images", "Neon_Button.png")).convert_alpha()
    Neon_Button_Image = pygame.transform.scale(Neon_Button_Image, (200,50))

    
    info_image_button = pygame.image.load(os.path.join(BASE_DIR, "images","information.png")).convert_alpha()
    info_image_button = pygame.transform.scale(info_image_button,(64,64))
    # initalises components of the puzzle board based on diffculty or custom
    board=Board(game_size,tile_size, screen)
    game_won= False #game one is set to false
    first_move_made = False
    shuffled = False
    #main Game loop
    while not Done:  
        #updates background 
        x , y = scrolling_background(selected_background, x,y )
        screen.blit(background, (0,y))
        screen.blit(background, (0,y-height))
        
        #draws the game board 
        board.draw_grid()
        board.draw_tiles()
        #creates and displays the buttons need for the game  
        Back_B=Button(600,500,"Back",font=get_Font(35),base_color=(255,0,255),hovering_color=(255,255,255), image = Neon_Button_Image)
        Back_B.draw(screen)

        info_button = Button(650,50,"",font=get_Font(20),base_color=None, hovering_color=None, image= info_image_button, width = 64, height = 64 )
        info_button.draw(screen)



        Reset_button = Button(600,100,"Reset", font=get_Font(35),base_color=(255,0,0), hovering_color=(255,255,255), image=Neon_Button_Image)
        Reset_button.draw(screen)


        Shuffle_button = Button(600,400,"Shuffle", font=get_Font(35),base_color=(255,0,0), hovering_color=(255,255,255), image=Neon_Button_Image)
        Shuffle_button.draw(screen)

        solve_button = Button(600,200,"Solve", font=get_Font(35),base_color=(255,0,0), hovering_color=(255,255,255), image=Neon_Button_Image)
        solve_button.draw(screen)
        hint_button = Button(600,150,"Hint", font=get_Font(35),base_color=(255,0,0), hovering_color=(255,255,255), image=Neon_Button_Image)
        hint_button.draw(screen)
        #draws time components for the game 
        time_display= timer.time()  #Time is loaded from timer file/module 
        font = pygame.font.Font(None,24) #sets font
        #displays the time  
        time_text = font.render(f"Time: {time_display}", True,(255,255,255))
        screen.blit(time_text, (640,340))
        #renders best time text and displays from timer module thats been imported 

        Best_Time_text = font.render(f"Best Time: {timer.best_time_display()}", True, (255,255,255))
        screen.blit(Best_Time_text, (640,360))

        #renders moves made  and draws it ; from board module 
        move_made = font.render(f"Moves Made: {board.moves_made}", True, (255,255,255))
        screen.blit(move_made, (640, 300))
        #renders best move made  text and displays from board module thats been imported

        best_moves_made = font.render(f"Best Moves: {board.best_moves if board.best_moves>0 else '--'}", True, (255,255,255))
        screen.blit(best_moves_made, (640,320))


        #if game is won, it displays a win text at the top saying you win "win"
        if game_won:
            win_text = font.render("You win", True, (0,255,255))
            screen.blit(win_text,(screen.get_width() // 2 - 50, 60)) #draws win at top centre of the screen, ((800//2 + 50),60)

        

        Menu_Mouse_Pos = pygame.mouse.get_pos() #gets the position of the mouse constanly as its a loop and is updates 
        
        for event in pygame.event.get():
            
            if event.type==pygame.MOUSEBUTTONDOWN:  #if clicked 
                if info_button.check_for_input(Menu_Mouse_Pos):
                    information()
                if Reset_button.check_for_input(Menu_Mouse_Pos):
                    board.reset_best_moves()
                    timer.reset_best_time()
                if Back_B.check_for_input(Menu_Mouse_Pos): #and mouse is on back button 
                    return #returns to diffculty 
            
                if Shuffle_button.check_for_input(Menu_Mouse_Pos): #if clicked on shuffle button 
                    board.shuffle() #board is shuffled 
                    timer.reset()  #timer is reset 
                    first_move_made = False  #fors move made is false 
                    game_won = False # game won is set to true 
                    shuffled = True
                
                if hint_button.check_for_input(Menu_Mouse_Pos) and shuffled and not game_won: # if hint button pressed 
                    show_hint(board, game_size)  #use the procedure imported from AStarSolver module that will move optimal tile
                    if board.check_win(): #if board is goal state  if check win on baord module is true 
                        game_won = True #game won is set to ture to prompt true 
                        timer.stop_time() #timer is stopped
                if solve_button.check_for_input(Menu_Mouse_Pos): #check if mouse is on solve button when clicked 
                    solver = AStarSolver(game_size)  #initalise solver for the puzzle size
                    current_state = board.get_current_state() #gets the current state/postions of tile/grid 
                    solution = solver.solve(current_state) #finds the best solution of the current state and is stored in list of steps to solve
                    
                    if solution: # if there is a solution
                        for state in solution: #goes/loops through each of the steps/states
                            board.set_grid(state)  # Updates the grid to the new state 
                            pygame.time.wait(300)  # Wait a bit for animation effect
                            screen.fill((0,0,0)) #set the whole screen to black 
                            board.draw_grid() #draws the grid again
                            board.draw_tiles() #draws the tile 
                            pygame.display.update()

                        game_won = True #game won is set to true 
                        timer.stop_time() #timer is stopped 


                
                if event.button == 1:  #if left button is clicked 
                    button_clicked  = False  # button clicked is flagged to check if UI button are pressed or not
    
                    for button in [Back_B, Shuffle_button, solve_button, hint_button]:  #  for each of the buttons 
                        
                        if button.check_for_input(Menu_Mouse_Pos):  #if mouse is over the button
                            button_clicked = True #set the button click to True 
                            break  #eixt out of the loop

                        if not button_clicked and shuffled and not game_won: # if no buttons were pressed and shuffled and not won
                            mouse_pos = pygame.mouse.get_pos() #set mouse poisition to a varible
                            
                            if board.mouse_handling(mouse_pos): #calls on the mouse handling from board module to handle the posiotin of the mouse 
                                if not first_move_made: #if first move is not made 
                                    timer.start_time() # it starts time 
                                    first_move_made = True # first move is set to true 
                                if board.check_win(): #if won from board module 
                                    game_won = True  #game won is set to true 
                                    timer.stop_time()#time is stopped  #cant move tiles 
                            
                
                
            
            

            
                
            if event.type == pygame.KEYDOWN and shuffled and not game_won:
                    moved = False 

                    if (event.key == pygame.K_UP) or (event.key == pygame.K_w): #if key pressed is up arrow or w
                        board.Move_Up() #board module moves the adjacent tile up to the empty
                        moved = True 
                    elif (event.key == pygame.K_DOWN) or (event.key == pygame.K_s): #if key pressed is down arrow or s
                        board.Move_Down() # moves adjacent tile down
                        moved = True
                    elif (event.key == pygame.K_RIGHT) or (event.key == pygame.K_d): # if key pressed is right arrow or d
                        board.Move_Right() #borad module moves tile to the right to the empty tile
                        moved = True 
                    elif (event.key == pygame.K_LEFT) or (event.key == pygame.K_a) : # if right arrow is pressed  or a 
                        board.Move_Left() #move the tile to the left thats adjacent to  the tile the empty tile
                        moved = True
                    if moved: 
                        if not first_move_made:
                            timer.start_time()
                            first_move_made = True
                
                        if board.check_win(): #if won
                            game_won = True #game_won  is set to true 
                            timer.stop_time() #timer stops 
           
           
           
            
                

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update() #updates/refreshes the screen
    


if __name__ == "__main__":
    Menu()



