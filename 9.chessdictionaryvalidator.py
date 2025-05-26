def is_valid_square(square):
    if len(square) != 2:
        return False
    file, rank = square[0], square[1]
    return file in 'abcdefgh' and rank in '12345678'

def is_valid_piece(piece):
    if piece is None:
        return True  # empty square
    if len(piece) != 2:
        return False
    color, p = piece[0], piece[1]
    return color in ('w', 'b') and p in ('K', 'Q', 'R', 'B', 'N', 'P')

def validate_chessboard(board):
    # Count pieces and check keys/pieces
    piece_counts = {'wK': 0, 'bK': 0, 'wP': 0, 'bP': 0}
    for square, piece in board.items():
        if not is_valid_square(square):
            return f"Invalid square: {square}"
        if not is_valid_piece(piece):
            return f"Invalid piece {piece} at {square}"
        
        if piece in piece_counts:
            piece_counts[piece] += 1
        
        # Check pawns on first or eighth rank
