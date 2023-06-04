from enum import Enum


EMPTY = "."

FILES = ["a", "b", "c", "d", "e", "f", "g", "h"]
RANKS = [1, 2, 3, 4, 5, 6, 7, 8]

WHITE_COLOR_CODE = "\033[0;37;40m"
BLACK_COLOR_CODE = "\033[5;30;47m"
NORMAL_COLOR_CODE = "\033[0;37;40m"

class WhitePieces(str, Enum):
    King = "K"
    Queen = "Q"
    Bishop = "B"
    Knight = "N"
    Rook = "R"
    Pawn = "P"
    Blank = "."
    def __repr__(self):
        return f'{WHITE_COLOR_CODE}{self.value}{NORMAL_COLOR_CODE}'
    def __str__(self):
        return self.value
    def __format__(self, spec):
        return f'{WHITE_COLOR_CODE}{self.value}{NORMAL_COLOR_CODE}'

class BlackPieces(str, Enum):
    King = "k"
    Queen = "q"
    Bishop = "b"
    Knight = "n"
    Rook = "r"
    Pawn = "p"
    Blank = "."
    def __repr__(self):
        return f'{BLACK_COLOR_CODE}{self.value}{NORMAL_COLOR_CODE}'
    def __str__(self):
        return f'{self.value}'
    def __format__(self, spec):
        return f'{BLACK_COLOR_CODE}{self.value}{NORMAL_COLOR_CODE}'

class Color(str, Enum):
    W = "White"
    B = "Black"
    
class Notations(str, Enum):
    Check = "+"
    Checkmate = "#"
    Capture = "x"
    Promotion = "="
    KingsideCastle = "O-O"
    QueensideCastle = "O-O-O"
    EnPassant = "e.p."
