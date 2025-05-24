#Program: 
 
import random 
 
def print_board(board): 
    for row in board: 
        print(" | ".join(row)) 
        print("-" * 9) 
 
def check_winner(board, player): 
    # Check rows, columns, and diagonals for a winner 
    for i in range(3): 
        if all(cell == player for cell in board[i]) or all(board[j][i] == player for j in range(3)): 
            return True 
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)): 
        return True 
    return False 
 
def is_board_full(board): 
    # Check if the board is full 
    for row in board: 
        if ' ' in row: 
            return False 
    return True 
 
def get_empty_cells(board): 
    # Return a list of coordinates for empty cells 
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' '] 
 
def is_valid_move(board, row, col): 
    # Check if the move is valid 
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ' 
 
def make_ai_move(board, user_symbol): 
    # AI tries to block the user from winning 
    for i in range(3): 
        for j in range(3): 
            if is_valid_move(board, i, j): 
                board[i][j] = user_symbol 
                if check_winner(board, user_symbol): 
                    board[i][j] = 'O' 
                    return 
                board[i][j] = ' ' 
 
    # If no immediate threat, make a random move 
    empty_cells = get_empty_cells(board) 
    if empty_cells: 
        row, col = random.choice(empty_cells) 
        board[row][col] = 'O' 
 
def play_game(): 
    board = [[' ' for _ in range(3)] for _ in range(3)] 
    user_symbol = input("Choose your symbol (X/O): ").upper() 
    ai_symbol = 'X' if user_symbol == 'O' else 'O' 
 
    while True: 
        print_board(board) 
 
        if is_board_full(board): 
            print("It's a draw!") 
            break 
 
        user_row = int(input("Enter your move (row 0-2): ")) 
        user_col = int(input("Enter your move (col 0-2): ")) 
 
        if is_valid_move(board, user_row, user_col): 
            board[user_row][user_col] = user_symbol 
        else: 
            print("Invalid move. Please try again.") 
            continue 
 
        if check_winner(board, user_symbol): 
            print_board(board) 
            print("Congratulations! You win!") 
            break 
 
        print_board(board) 
        print("Bot's Turn") 
 
        make_ai_move(board, user_symbol) 
 
        if check_winner(board, ai_symbol): 
            print_board(board) 
            print("AI wins!") 
            break 
 
play_game() 
 
 
'''Output: 
 
Choose your symbol (X/O): x 
  |   |   --------- 
  |   |   --------- 
  |   |   --------- 
Enter your move (row 0-2): 0 
Enter your move (col 0-2): 0 
X |   |   --------- 
  |   |   --------- 
  |   |   --------- 
Bot's Turn 
X |   |   --------- 
  |   |   --------- 
  |   | O --------- 
Enter your move (row 0-2): 1 
Enter your move (col 0-2): 1 
X |   |   --------- 
  | X |   --------- 
  |   | O --------- 
Bot's Turn 
X |   |   --------- 
  | X |   --------- 
  | O | O --------- 
Enter your move (row 0-2): 2 
Enter your move (col 0-2): 0 
X |   |   --------- 
  | X |   --------- 
X | O | O --------- 
Bot's Turn 
X |   | O --------- 
  | X |   --------- 
X | O | O --------- 
Enter your move (row 0-2): 1 
Enter your move (col 0-2): 2 
X |   | O --------- 
  | X | X --------- 
X | O | O --------- 
Bot's Turn 
X |   | O --------- 
O | X | X --------- 
X | O | O --------- 
Enter your move (row 0-2): 0 
Enter your move (col 0-2): 1 
X | X | O --------- 
O | X | X --------- 
X | O | O --------- 
Bot's Turn 
X | X | O --------- 
O | X | X --------- 
X | O | O --------- 
It's a draw!

'''