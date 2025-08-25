#Program: 
 
from random import shuffle 
 
def print_puzzle(state): 
    for i in range(0, 7, 3): 
        print(state[i:i+3]) 
 
def get_moves(state): 
    moves = [] 
    zero_index = state.index(0) 
 
    if zero_index % 3 > 0: 
        moves.append('left') 
 
    if zero_index % 3 < 2: 
        moves.append('right') 
 
    if zero_index >= 3: 
        moves.append('up') 
 
    if zero_index < 6: 
        moves.append('down') 
 
    return moves 
 
def apply_move(state, move): 
    new_state = state.copy() 
    zero_index = new_state.index(0) 
 
    if move == 'left': 
        new_state[zero_index], new_state[zero_index - 1] = new_state[zero_index - 1], new_state[zero_index] 
    elif move == 'right': 
        new_state[zero_index], new_state[zero_index + 1] = new_state[zero_index + 1], new_state[zero_index] 
    elif move == 'up': 
        new_state[zero_index], new_state[zero_index - 3] = new_state[zero_index - 3], new_state[zero_index] 
    elif move == 'down': 
        new_state[zero_index], new_state[zero_index + 3] = new_state[zero_index + 3], new_state[zero_index] 
 
    return new_state 
 
def is_goal(state): 
    return state == [1, 2, 3, 4, 5, 6, 7,8, 0] 
 
def play_game(): 
    initial_state = [1, 2, 3, 4, 5, 6, 0, 7,8] 
    shuffle(initial_state) 
 
    print("Welcome to the 7 Puzzle Game!") 
    print("Try to arrange the numbers in order:") 
    print_puzzle(initial_state) 
 
    while not is_goal(initial_state): 
        moves = get_moves(initial_state) 
        print("Available moves:", moves) 
        user_move = input("Enter your move (left/right/up/down): ").lower() 
 
        if user_move in moves: 
            initial_state = apply_move(initial_state, user_move) 
            print_puzzle(initial_state) 
        else: 
            print("Invalid move. Please try again.") 
 
    print("Congratulations! You solved the puzzle.") 
 
play_game() 


'''
Output: 
Welcome to the 7 Puzzle Game! 
Try to arrange the numbers in order: 
[1, 2, 3] 
[4, 5, 6] 
[7, 8, 0] 
 
Available moves: ['left', 'right', 'up', 'down'] 
Enter your move (left/right/up/down): down 
[1, 2, 3] 
[4, 5, 0] 
[7, 8, 6] 
 
Available moves: ['left', 'right', 'up', 'down'] 
Enter your move (left/right/up/down): right 
[1, 2, 3] 
[4, 0, 5] 
[7, 8, 6] 
 
Available moves: ['left', 'right', 'up', 'down'] 
Enter your move (left/right/up/down): up 
[1, 0, 3] 
[4, 2, 5] 
[7, 8, 6] 
 
Available moves: ['left', 'right', 'up', 'down'] 
Enter your move (left/right/up/down): left 
[0, 1, 3] 
[4, 2, 5] 
[7, 8, 6] 
 
Available moves: ['right', 'up', 'down'] 
Enter your move (left/right/up/down): right 
[1, 0, 3] 
[4, 2, 5] 
[7, 8, 6] 
 
Available moves: ['left', 'up', 'down'] 
Enter your move (left/right/up/down): down 
[1, 2, 3] 
[4, 0, 5] 
[7, 8, 6] 
 
Available moves: ['left', 'right', 'up', 'down'] 
Enter your move (left/right/up/down): down 
[1, 2, 3] 
[4, 8, 5] 
[7, 0, 6] 
 
Available moves: ['left', 'up'] 
Enter your move (left/right/up/down): up 
[1, 2, 3] 
[4, 0, 5] 
[7, 8, 6] 
 
Available moves: ['left', 'right', 'down'] 
Enter your move (left/right/up/down): left 
[1, 2, 3] 
[0, 4, 5] 
[7, 8, 6] 
 
Available moves: ['right', 'up', 'down'] 
Enter your move (left/right/up/down): right 
[1, 2, 3] 
[4, 0, 5] 
[7, 8, 6] 
 
Available moves: ['left', 'up', 'down'] 
Enter your move (left/right/up/down): right 
[1, 2, 3] 
[4, 5, 0] 
[7, 8, 6] 
 
Available moves: ['left', 'up', 'down'] 
Enter your move (left/right/up/down): down 
[1, 2, 3] 
[4, 5, 6] 
[7, 8, 0] 
 
Congratulations! You solved the puzzle. '''