# ------ Variables --------

# board

board = ['-', '-', '-',
         '-', '-', '-', 
         '-', '-', '-']

# the game still playing
game_not_over = True
current_player = "X"

winner = None

took_positions = [i for i in range(11)]

# functions

def display_board(): # shows the board

    print('|' + board[0] + '|' + board[1] + '|' + board[2] + '|')
    print('|' + board[3] + '|' + board[4] + '|' + board[5] + '|')
    print('|' + board[6] + '|' + board[7] + '|' + board[8] + '|')

def inital_turn(): # main turn 

    print(f"it's {current_player} turn")
    position = input("chose a position from 1-9: ")

    valid = True
    while valid:
        
        # check if the position is valid
        
        while not position in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("chose a position from 1-9: ")
        
        position = int(position) - 1 

        # now check if the space is avaliable

        if board[position] == "-":
            board[position] = current_player
            valid = False
        else:
            print("you can't go there, try again")
        
        display_board()

def flip_player(): # change who plays
    global current_player

    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

def check_game_over():
    check_if_win()
    check_if_tie()

def check_if_win():
    global winner 

    # check the rows
    row_win = check_rows()

    # check the cols
    colum_win = check_colums()

    #check the diagonals
    diagonal_win = check_diagonals()

    if row_win:
        winner = row_win
    elif colum_win:
        winner =  colum_win
    elif diagonal_win:
        winner = diagonal_win
        
        

def check_rows():
    #seting the end of the game
    global game_not_over
    
    row_1 = board[0] == board[1] == board[2] != '-'
    row_2 = board[3] == board[4] == board[5] != '-'
    row_3 = board[6] == board[7] == board[8] != '-'

    # return the winner value 
    if row_1 or row_2 or row_3:
        game_not_over = False
    if row_1:
        return board[0]
    elif row_2: 
        return board[3]
    elif row_3:
        return board[6]

def check_colums():
    #seting the end of the game
    global game_not_over
    
    col_1 = board[0] == board[3] == board[6] != '-'
    col_2 = board[1] == board[4] == board[7] != '-'
    col_3 = board[2] == board[5] == board[8] != '-'

    # return the winner value 
    if col_1 or col_2 or col_3:
        game_not_over = False
    if col_1:
        return board[0]
    elif col_2: 
        return board[3]
    elif col_3:
        return board[6]


def check_diagonals():
    
    #seting the end of the game
    global game_not_over
    
    col_1 = board[0] == board[4] == board[8] != '-'
    col_2 = board[6] == board[4] == board[2] != '-'

    # return the winner value 
    if col_1 or col_2:
        game_not_over = False
    if col_1:
        return board[0]
    elif col_2: 
        return board[6]

def check_if_tie():
    global game_not_over
    if '-' not in board:
        game_not_over = False



def play_game(): # main function
    
    display_board() #display the board
    
    while game_not_over:     
        value = inital_turn() # ask the user for a position from 1-9
        
        check_game_over()
        
        flip_player() 

    # the game end
    if winner == "X" or winner == "O":
        print(f"{winner} wins")
    elif winner == None:
        print("it's a tie")
        
if __name__  == '__main__':
    play_game()
    
