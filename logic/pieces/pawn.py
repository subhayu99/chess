from typing import Literal
from logic.board import ChessBoard
from logic.pieces.base_piece import BasePiece, BP, WP, Coordinate, Color


class Pawn(BasePiece):
    def __init__(
        self, 
        coordinate: Coordinate, 
        color: Literal["W", "B"], 
        board: ChessBoard = None
    ):
        super().__init__(coordinate, color, board)
        self.piece = BP.Pawn if self.color == Color.B else WP.Pawn
        self.set_board()
    
    def get_possible_moves(self) -> list[Coordinate]:
        coordinates = self.pos._get_vertical_coordinates(2) + self.pos._get_diagonal_coordinates(1)
        return list(filter(self._validate_move, coordinates))
    
    def _validate_move(self, coordinate: Coordinate) -> bool:
        rank = coordinate.rank
        file = coordinate.file
        if self.color == Color.W:
            right_diag_piece = self.get_piece_by_diff(1, 1)
            left_diag_piece = self.get_piece_by_diff(-1, 1)
            if self.pos._same_diagonal(coordinate):
                if isinstance(right_diag_piece, BasePiece) and right_diag_piece.color == Color.B:
                    return coordinate == self.pos.shift(1, 1)
                if isinstance(left_diag_piece, BasePiece) and left_diag_piece.color == Color.B:
                    return coordinate == self.pos.shift(-1, 1)
            if self.pos.rank == 2:
                return rank in (3, 4) and file == self.pos.file
            return rank == self.pos.rank + 1 and file == self.pos.file
        else:
            right_diag_piece = self.get_piece_by_diff(1, -1)
            left_diag_piece = self.get_piece_by_diff(-1, -1)
            if self.pos._same_diagonal(coordinate):
                if isinstance(right_diag_piece, BasePiece) and right_diag_piece.color == Color.W:
                    return coordinate == self.pos.shift(1, -1)
                if isinstance(left_diag_piece, BasePiece) and left_diag_piece.color == Color.W:
                    return coordinate == self.pos.shift(-1, -1)
            if self.pos.rank == 7:
                return rank in (6, 5) and file == self.pos.file
            return rank == self.pos.rank - 1 and file == self.pos.file
