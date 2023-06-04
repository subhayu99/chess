from typing import Literal
from logic.board import ChessBoard
from logic.pieces.base_piece import BasePiece, BP, WP, Coordinate, Color


class Bishop(BasePiece):
    def __init__(
        self, 
        coordinate: Coordinate, 
        color: Literal["W", "B"], 
        board: ChessBoard = None
    ):
        super().__init__(coordinate, color, board)
        self.piece = BP.Bishop if self.color == Color.B else WP.Bishop
        self.set_board()
    
    def get_possible_moves(self) -> list[Coordinate]:
        return self.pos._get_diagonal_coordinates(8)
