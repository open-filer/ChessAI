def evaluate_with_game_state(board):
    if board.is_checkmate():
        return float('-inf') if board.turn else float('inf')  # Favor the winning side
    elif board.is_stalemate() or board.is_insufficient_material():
        return 0  # Draw
    else:
        return evaluate_board_with_position(board)

print("Final Evaluation:", evaluate_with_game_state(board))
