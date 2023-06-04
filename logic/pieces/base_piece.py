from dataclasses import dataclass
from typing import Literal

from logic.coordinate import Coordinate
from logic.board import ChessBoard
from logic.constants import (
    BlackPieces as BP,
    WhitePieces as WP,
    Color,
    FILES,
    RANKS,
)


class BasePiece():
    def __init__(
        self, 
        coordinate: Coordinate, 
        color: Literal["W", "B"], 
        board: ChessBoard = None
    ):
        self.piece: BP|WP = "O" if color == "W" else "o"
        self.pos: Coordinate = coordinate
        self.color: Color = Color[color]
        self.board: ChessBoard = board or ChessBoard()
    
    def set_board(self):
        self.board.set_piece(piece=self)
    
    def get_possible_moves(self) -> list[Coordinate]:
        return []
    
    def out_of_bounds(self, coordinate: Coordinate = None) -> bool:
        file = coordinate.file if coordinate is not None else self.pos.file
        rank = coordinate.rank if coordinate is not None else self.pos.rank
        if file not in FILES or rank not in RANKS:
            return True
        return False
    
    def get_possible_moves_board(self) -> ChessBoard:
        moves = self.get_possible_moves()
        board = self.coordinate.board(self.piece) if self.board is None else self.board
        for move in moves:
            board.set_piece_by_file_rank(move.file, move.rank, "+")
        return board
    
    def is_valid_move(self, coordinate: Coordinate) -> bool:
        return True
    
    def move(self, coordinate: Coordinate):
        pass
    
    def get_piece_by_diff(self, horizontal: int, vertical: int) -> "BasePiece":
        coordinate = self.pos.shift(horizontal, vertical, none_if_out_of_bounds=True)
        if coordinate is None:
            return None
        return self.board.get_piece_by_file_rank(coordinate.file, coordinate.rank)
    
    def __repr__(self) -> str:
        return self.piece
    
    def __str__(self) -> str:
        return self.piece
    
    def __format__(self, __format_spec: str = "%c %P at %f%r") -> str:
        """
        Use the following format specifiers:
        
        %p: piece
        %P: piece full name
        %c: color
        %f: file
        %r: rank
        """
        return (__format_spec
            .replace("%p", self.piece.value)
            .replace("%P", self.piece.name)
            .replace("%c", self.color.value)
            .replace("%f", self.pos.file)
            .replace("%r", str(self.pos.rank))
        )
    
    def __eq__(self, other: object) -> bool:
        pass
        
    @property
    def coordinate(self) -> Coordinate:
        return self.pos