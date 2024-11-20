# Function for chess board creation
import chess
board  = chess.Board()
print(board)
print("\n")

# Making a move1 (white)
board.push_san("e2e4")
print(board)
print("\n")
# Checking legal move for black
legal_moves = board.legal_moves
print(legal_moves)
print("\n")

# Making a move1 (black)
board.push_san("e7e5")
print(board)
print("\n")
# Checking legal move for white
legal_moves = board.legal_moves
print(legal_moves)
print("\n")
