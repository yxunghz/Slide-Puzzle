import heapq

class AStarSolver:
    def __init__(self, game_size):
        self.game_size = game_size #e.g 3 for 3x3 so numbers of tiles
        self.goal_state = list(range(1, game_size ** 2)) + [0] #arranges it in a 1d list form where it starts from 1 to 9 and stops at 8
        #it stops at 8 and an array 0 is added at the end to indicate empty tile 
        
    def manhattan_distance(self, state):  #state is the current puzzle configuration and calucaltes how far it is from correct position
        #calcuates herustic cost which approximates by using sum of tile distance from goal position
        total_distance = 0 # toal disance is set to 0 
        for i in range(len(state)): # goes through every state  
            if state[i] != 0:#skips empty tile 
                target_pos = state[i] - 1  #gives the correct postion for each tile  eg (tile 2 ) 2-1 = 1
                target_row = target_pos // self.game_size  #calcualtes the goal row of the tile e.g target pos of tile would be 2 = 1 and game size(e.g 3) 
                #target row = 0 indicates first row 
                target_col = target_pos % self.game_size # calculates the goal column of the tile same example above would be 1%3 = 1(second column) #0 is the first column
                current_row = i // self.game_size #finds the current row of the tile in the unsolved puzzle 
                current_col = i % self.game_size  # finds the current column of the tile in the unsolved puzzle  
                #          0 1 2                             0 1 2 
                #example 0 [1,0,6]                           [0,1,2]
                #        1 [4,2,7]  #if i= 4       ordered:  [3,4,5]  tile 2 would at when i = 4 which would be the row 1 and row 2 
                #        2 [8,5,3]                           [6,7.8] 
                 
                total_distance += abs(current_row - target_row) + abs(current_col - target_col)
        return total_distance

    def get_neighbours(self, state): # takes a state and provides all possible next states after valid moves
        neighbours = [] # neigbours is set to a list
        empty_tile = state.index(0) # empty tile is the index 0
        empty_row, empty_col = empty_tile // self.game_size, empty_tile % self.game_size # gives the position of the empty tile row and col
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]   # up down left or right
        # eg for move left:
        #    0   1   2
        # 0 [2] [0] [6]   empty tile is at index 1 (row 0 , col 1 )
        # 1 [1] [5] [3]   to move up (-1,0) 
        # 2 [8] [7] [4]   new postion = (-1,1)  -1 is invalid move so wont work
        
        for direction in directions: #checks  all 4 possbile by   
            #calcuates where empty tile would move 
            new_row, new_col = empty_row + direction[0], empty_col + direction[1] #the addition i basically done above 
            #checks if its within boundarys 
            if 0 <= new_row < self.game_size and 0 <= new_col < self.game_size: #if row and col are graeter than or equal to 0 and less or equal to the game size 
                new_empty_tile = new_row * self.game_size + new_col # 
                # eg [1,3,0]   empty tile index = 2 row 0 column 2 (0,2) 
                #    [4,2,6]   new positoin = (1,2) so swaps with 6
                #    [7,8,5] empty is at index 0  if we move down 2*3+1 = swaps with index 5 which is 6 
                new_state = state[:] #creates a copy of the current state
                new_state[empty_tile], new_state[new_empty_tile] = new_state[new_empty_tile], new_state[empty_tile]
                #mmakes the adjacent tile move in percpetive of the the user 
                neighbours.append(new_state) # ands the new state to the list
        
        return neighbours
    
    def solve(self, start_state):
        #creates a priorirt queue with starting stae
        open_list = []
        heapq.heappush(open_list, (0, start_state, [start_state]))  
        #total_cost, current state, path_to_here
        visited = set() #tracks vistied to avoid loops 
        visited.add(tuple(start_state)) #converts to hash because list cant be hashed 
        
        while open_list: # while there are states to explore
            #gets states with the lowest cost 
            current_cost, current_state, current_path = heapq.heappop(open_list)
            #checks if we reached the goal or not 
            if current_state == self.goal_state:
                return current_path #returns the solution path 

            for neighbor in self.get_neighbours(current_state):#  # explore all possible moves 
                if tuple(neighbor) not in visited: # if we havent seen this state before 
                    visited.add(tuple(neighbor)) #marks as visited 
                    heuristic = self.manhattan_distance(neighbor) #calculates priority : 
                    #path lenth + estimated distance 
                    total_cost = len(current_path) + heuristic 
                    heapq.heappush(open_list, (total_cost, neighbor, current_path + [neighbor]))
                    #adds the queueu with new path 
        
        return None # if no solution found  it returns none incase 


def show_hint(board, game_size): 
     
    solver = AStarSolver(game_size) #creates solver for current puzzle size
    initial_state = board.grid  #gets current puzzle state 
    solution = solver.solve(initial_state) #finds full solution path 

    if solution and len(solution) > 1: # if solution exisits and (doesnt end game or isnt the start state)
        next_state = solution[1]  #gets the first move from the solution
        board.set_grid(next_state) #updates board to show this move
        board.Moves() 
        print("Hint shown (performed the optimal move).")
    else:
        print("No hint available (already solved or unsolvable).")
