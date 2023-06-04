from logic.constants import (
    EMPTY,
    FILES,
    RANKS,
    WhitePieces as WP,
    BlackPieces as BP,
)


class ChessBoard():
    def __init__(self, use_color=False) -> None:
        self.use_color = use_color
        self.board = [[EMPTY]*8 for _ in range(8)]
        self.captured: list[BP|WP|str] = []

    def get_piece_by_file_rank(self, file: str, rank: int):
        return self.board[8 - rank][FILES.index(file)]

    def set_piece_by_file_rank(self, file: str, rank: int, piece) -> None:
        # if self.get_piece_by_file_rank(file, rank) not in (WP.Blank, BP.Blank, EMPTY):
        #     raise ValueError(f"Cannot set piece at {file}{rank} to {piece}. {self.get_piece_by_file_rank(file, rank).piece} already exists.")
        self.board[8 - rank][FILES.index(file)] = piece
        return self
    
    def set_piece(self, piece):
        from logic.pieces import BasePiece
        if not isinstance(piece, BasePiece):
            raise TypeError(f"Expected BasePiece, got {type(piece)}")
        self.board[8 - piece.pos.rank][FILES.index(piece.pos.file)] = piece
        piece.board = self
        return self
        
    def move_piece_by_file_rank(self, from_file: str, from_rank: int, to_file: str, to_rank: int) -> None:
        piece = self.get_piece_by_file_rank(from_file, from_rank)
        to_piece = self.get_piece_by_file_rank(to_file, to_rank)
        if to_piece not in (WP.Blank, BP.Blank, EMPTY):
            self.captured.append(to_piece)
        self.set_piece_by_file_rank(from_file, from_rank, EMPTY)
        self.set_piece(piece)
        return self
        
    def __str__(self) -> str:
        s = ""
        s += "  a b c d e f g h  \n"
        for i in range(8):
            s += f"{8 - i} "
            for j in range(8):
                piece = self.board[i][j]
                piece = piece if isinstance(piece, str) else piece.piece
                s += f"{piece} " if self.use_color else (str(piece)+" ")
            s += f"{8 - i}\n"
        s += "  a b c d e f g h  \n"
        return s
    
    def __repr__(self) -> str:
        return self.__str__()
