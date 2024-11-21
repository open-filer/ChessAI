import chess

board = chess.Board()

def check_state():
    if board.is_checkmate():
        print("Checkmate ! Game Over ")
        return True
    elif board.is_fifty_moves():
        print("Draw by 50 move rule")
        return True
    elif board.is_fivefold_repetition():
        print("Draw by 5 fold repetition")
        return True
    elif board.is_insufficient_material():
        print("Draw by insufficient material")
        return True
    elif board.is_stalemate():
        print("Draw by stalemate")
        return True
    return False

# to make a move
def move():
    while not check_state():
        try:
            move = input("Enter a move : ")
            board.push_san(move)
            print(board)
        except ValueError:
            print("invalid move try again ")
        except Exception as E :
            print(f"Error {E} try again ")

#start game 
print(board)
move()