import chess

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

board = chess.Board()
print("Board Evaluation:", eval_board(board))