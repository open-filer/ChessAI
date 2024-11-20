# to display the chess board
import chess
board = chess.Board()
print(board)
print("\n")

#function to take moves from user 

def make_move():
    legal_moves = board.legal_moves
    print(legal_moves,"\n")
    move = input("Enter your move : ")
    board.push_san(move)
    print(board)
    print("\n")
    make_move()

make_move()