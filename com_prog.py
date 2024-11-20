# Importing Libaries
import chess
import random

# Creating board
board = chess.Board()

# Function for user move
def user_move():
    while True :
        print("Legal moves : ", list(board.legal_moves), "\n")
        move = input("Enter your move : ")

        try:
            board.push_san(move)
            print(board)
            print("\n")
            break 
        except ValueError:
            print(f"Invalid move! : {move} || please try again ")
        except Exception as E :
            print(f"{E} has occured")

#function for computer move 
def com_move():
    legal_moves = list(board.legal_moves)
    move = random.choice(legal_moves)
    board.push(move)
    print("Computer's move :")
    print(board)
    print("\n")

# Main game btw comp(black) and user(white) 
def play():
    print(board)
    print("\n")

    while not board.is_game_over(): # game over ---> false || not false ---> true 
        #playing until game is over ( When game is over boolean becomes false and loop breaks)   
        print("Your turn ! ")
        user_move()

        if board.is_game_over(): # check if game is over 
            break # if game is over it should break

        print("Computer's move ! ")
        com_move() 
        # now if computer make a move and its game over,
        # While loop wont run cuz the boolean will be false !!
    
    # Checking how is the game over i.e. by checkmate, stalemate or Insufficient material
    if board.is_checkmate():
        print("checkmate")
        print("The winner is","Computer" if board.turn else "User")
    elif board.is_stalemate():
        print("Stalemate")
    elif board.is_insufficient_material():
        print("Insufficient material")
    elif board.is_fivefold_repetition():
        print("draw due to three fold repetition")
    elif board.is_fifty_moves():
        print("Draw by 50 move rule")

# Start the game U_U....(finally I reached here)
play()
# to chaliye suru krteee hian Oo.