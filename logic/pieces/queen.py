from typing import Literal
from logic.board import ChessBoard
from logic.pieces.base_piece import BasePiece, BP, WP, Coordinate, Color


class Queen(BasePiece):
    def __init__(
        self, 
        coordinate: Coordinate, 
        color: Literal["W", "B"], 
        board: ChessBoard = None
    ):
        super().__init__(coordinate, color, board)
        self.piece = BP.Queen if self.color == Color.B else WP.Queen
        self.set_board()
    
    def get_possible_moves(self) -> list[Coordinate]:
        coordinates = [
            *self.pos._get_diagonal_coordinates(8),
            *self.pos._get_horizontal_coordinates(8),
            *self.pos._get_vertical_coordinates(8)
        ]
        return coordinates
