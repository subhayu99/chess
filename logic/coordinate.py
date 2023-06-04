from logic.constants import FILES, RANKS
from logic.board import ChessBoard


class Coordinate():
    def __init__(self, file: str, rank: int):
        if file not in FILES or rank not in range(1, 9):
            raise ValueError(f"Invalid coordinate: {file}{rank}")
        self.file = file
        self.rank = rank
        
    def _get_adjascent_coordinates(self) -> list["Coordinate"]:
        coordinates = set()
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == j == 0:
                    continue
                coordinate = self.shift(j, i)
                if coordinate is not None:
                    coordinates.add(coordinate)
        coordinates.discard(self)
        return coordinates
    
    def _get_diagonal_coordinates(self, length: int) -> list["Coordinate"]:
        coordinates = set()
        for i in range(-length, length + 1):
            coordinate = self.shift(i, i)
            if coordinate is not None:
                coordinates.add(coordinate)
        for i in range(-length, length + 1):
            coordinate = self.shift(-i, i)
            if coordinate is not None:
                coordinates.add(coordinate)
        coordinates.discard(self)
        return list(filter(lambda x: not(self._same_file(x) or self._same_rank(x)), coordinates))
    
    def _get_horizontal_coordinates(self, length: int) -> list["Coordinate"]:
        coordinates = set()
        for i in range(-length, length + 1):
            coordinate = self.shift(i, 0)
            if coordinate is not None:
                coordinates.add(coordinate)
        coordinates.discard(self)
        return list(filter(self._same_rank, coordinates))
    
    def _get_vertical_coordinates(self, length: int) -> list["Coordinate"]:
        coordinates = set()
        for i in range(-length, length + 1):
            coordinate = self.shift(0, i)
            if coordinate is not None:
                coordinates.add(coordinate)
        coordinates.discard(self)
        return list(filter(self._same_file, coordinates))
    
    def _get_knight_coordinates(self) -> list["Coordinate"]:
        coordinates = set()
        for i in range(-2, 3):
            for j in range(-2, 3):
                if abs(i) + abs(j) != 3:
                    continue
                coordinate = self.shift(j, i)
                if (
                    self.distance(coordinate) < 2 
                    or self._same_file(coordinate) 
                    or self._same_rank(coordinate)
                    or self._same_diagonal(coordinate) 
                ):
                    continue
                if coordinate is not None:
                    coordinates.add(coordinate)
        coordinates.discard(self)
        return coordinates
    
    def _same_file(self, coordinate: "Coordinate") -> bool:
        return self.file == coordinate.file
    
    def _same_rank(self, coordinate: "Coordinate") -> bool:
        return self.rank == coordinate.rank
    
    def _same_diagonal(self, coordinate: "Coordinate") -> bool:
        return abs(self.rank - coordinate.rank) == abs(FILES.index(self.file) - FILES.index(coordinate.file))
    
    def _can_move_horizontal(self, value: int) -> bool:
        new_file_index = FILES.index(self.file) + value
        if new_file_index < 0 or new_file_index > 7:
            return False
        return True
    
    def _can_move_vertical(self, value: int) -> bool:
        new_rank = self.rank + value
        if new_rank < 1 or new_rank > 8:
            return False
        return True
        
    def out_of_bounds(self, coordinate: "Coordinate") -> bool:
        if coordinate.file not in FILES or coordinate.rank not in RANKS:
            return True
        return False
        
    def from_notation(self, notation: str):
        if len(notation) != 2:
            raise Exception("Invalid notation")
        self.file = notation[0]
        self.rank = int(notation[1])
        
    def shift(self, horizontal: int, vertical: int, none_if_out_of_bounds: bool = False, inplace: bool = False):
        vertical, horizontal = self._get_validated_shift_positions(horizontal, vertical)
        file = FILES[FILES.index(self.file) + horizontal]
        rank = self.rank + vertical
        if none_if_out_of_bounds and (vertical == 0 or horizontal == 0):
            return None
        if inplace:
            self.file, self.rank = file, rank
        else:
            return Coordinate(file, rank)

    def _get_validated_shift_positions(self, horizontal: int, vertical: int):
        if not self._can_move_horizontal(horizontal):
            horizontal = 0
        if not self._can_move_vertical(vertical):
            vertical = 0
        return vertical, horizontal
        
    def __repr__(self) -> str:
        return f"{self.file}{self.rank}"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __eq__(self, __value: "Coordinate") -> bool:
        return self.rank == __value.rank and self.file == __value.file
    
    def __hash__(self) -> int:
        return hash((self.file, self.rank))
    
    def to_tuple(self) -> tuple[str, int]:
        return (self.file, self.rank)
    
    def to_dict(self) -> dict[str, int]:
        return {"file": self.file, "rank": self.rank}

    def board(self, piece: str = "X") -> "ChessBoard":
        board = ChessBoard()
        board.set_piece(self.file, self.rank, piece)
        return board
    
    def distance(self, coordinate: "Coordinate") -> int:
        return max(abs(ord(self.file) - ord(coordinate.file)), abs(self.rank - coordinate.rank))
