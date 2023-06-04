from logic.constants import BlackPieces as BP, WhitePieces as WP, Color, FILES, RANKS, Notations
from logic.coordinate import Coordinate
from logic.pieces import King, Queen, Bishop, Rook, Knight, Pawn
from logic.board import ChessBoard


board = ChessBoard()

(
board
    .set_piece(Pawn(Coordinate("a", 2), "W"))
    .set_piece(Pawn(Coordinate("b", 2), "W"))
    .set_piece(Pawn(Coordinate("c", 2), "W"))
    .set_piece(Pawn(Coordinate("d", 2), "W"))
    .set_piece(Pawn(Coordinate("e", 2), "W"))
    .set_piece(Pawn(Coordinate("f", 2), "W"))
    .set_piece(Pawn(Coordinate("g", 2), "W"))
    .set_piece(Pawn(Coordinate("h", 2), "W"))
    
    .set_piece(Pawn(Coordinate("a", 7), "B"))
    .set_piece(Pawn(Coordinate("b", 7), "B"))
    .set_piece(Pawn(Coordinate("c", 7), "B"))
    .set_piece(Pawn(Coordinate("d", 7), "B"))
    .set_piece(Pawn(Coordinate("e", 7), "B"))
    .set_piece(Pawn(Coordinate("f", 7), "B"))
    .set_piece(Pawn(Coordinate("g", 7), "B"))
    .set_piece(Pawn(Coordinate("h", 7), "B"))
    
    .set_piece(King(Coordinate("e", 1), "W"))
    .set_piece(King(Coordinate("e", 8), "B"))
    
    .set_piece(Queen(Coordinate("d", 1), "W"))
    .set_piece(Queen(Coordinate("d", 8), "B"))
    
    .set_piece(Bishop(Coordinate("c", 1), "W"))
    .set_piece(Bishop(Coordinate("f", 1), "W"))
    .set_piece(Bishop(Coordinate("c", 8), "B"))
    .set_piece(Bishop(Coordinate("f", 8), "B"))
    
    .set_piece(Knight(Coordinate("b", 1), "W"))
    .set_piece(Knight(Coordinate("g", 1), "W"))
    .set_piece(Knight(Coordinate("b", 8), "B"))
    .set_piece(Knight(Coordinate("g", 8), "B"))
    
    .set_piece(Rook(Coordinate("a", 1), "W"))
    .set_piece(Rook(Coordinate("h", 1), "W"))
    .set_piece(Rook(Coordinate("a", 8), "B"))
    .set_piece(Rook(Coordinate("h", 8), "B"))
)



print(board.get_piece_by_file_rank("a", 1).get_possible_moves_board())
