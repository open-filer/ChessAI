# Importing Libaries
import chess
import random

# Creating board
board = chess.Board()

#pawn table
pawn_table = [
    0,  0,  0,  0,  0,  0,  0,  0,
    5, 10, 10,-20,-20, 10, 10,  5,
    5, -5,-10,  0,  0,-10, -5,  5,
    0,  0,  0, 20, 20,  0,  0,  0,
    5,  5, 10, 25, 25, 10,  5,  5,
    10, 10, 20, 30, 30, 20, 10, 10,
    50, 50, 50, 50, 50, 50, 50, 50,
    0,  0,  0,  0,  0,  0,  0,  0
]

# function for board evaluation
def eval_board(board):

    piece_val = {
        chess.PAWN : 1,
        chess.ROOK : 5 ,
        chess.BISHOP : 3 ,
        chess.KNIGHT : 3 ,
        chess.QUEEN : 9 ,
        chess.KING : 0
    }                   
    

    score = 0 
    for piece_type in piece_val :
        score += len(board.pieces(piece_type, chess.WHITE)) * piece_val[piece_type]
        score -= len(board.pieces(piece_type, chess.BLACK)) * piece_val[piece_type]
    
    return score

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
        print("Evaluation score : " ,eval_board(board))
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

# evaluation wrt position
def evaluate_board_with_position(board):
    piece_values = {
        chess.PAWN: 1,
        chess.KNIGHT: 3,
        chess.BISHOP: 3,
        chess.ROOK: 5,
        chess.QUEEN: 9,
        chess.KING: 0
    }

    # Use the piece-square table
    score = 0
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            piece_type = piece.piece_type
            value = piece_values[piece_type]
            if piece.color == chess.WHITE:
                score += value + pawn_table[square]
            else:
                score -= value + pawn_table[chess.square_mirror(square)]
    
    return score


# eval with game state
def evaluate_with_game_state(board):
    if board.is_checkmate():
        return float('-inf') if board.turn else float('inf')  # Favor the winning side
    elif board.is_stalemate() or board.is_insufficient_material():
        return 0  # Draw
    else:
        return evaluate_board_with_position(board)

# Start the game U_U....(finally I reached here)
play()
# to chaliye suru krteee hian Oo.