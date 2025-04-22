import random
import string


class Board:
    def __init__(self, size):
        self.size = size
        self.grid = [["." for _ in range(size)] for _ in range(size)]
        self.ships = []
        self.hits = set()

    def print_board(self, reveal_ships=False):
        print("  " + " ".join(string.ascii_uppercase[:self.size]))
        for idx, row in enumerate(self.grid):
            display_row = []
            for col in row:
                display_row.append(col)
            print(f"{idx+1:2} {' '.join(display_row)}")

    def place_ship(self, ship_size):
        while True:
            is_horizontal = random.choice([True, False])
            if is_horizontal:
                row = random.randint(0, self.size - 1)
                col = random.randint(0, self.size - ship_size)
                coords = [(row, col + i) for i in range(ship_size)]
            else:
                row = random.randint(0, self.size - ship_size)
                col = random.randint(0, self.size - 1)
                coords = [(row + i, col) for i in range(ship_size)]

            if all(self.grid[r][c] == "." for r, c in coords):
                for r, c in coords:
                    self.grid[r][c] = "S"
                self.ships.append(set(coords))
                break

    def guess(self, coord):
        row, col = coord
        if not (0 <= row < self.size and 0 <= col < self.size):
            return "off"
        if self.grid[row][col] == "S":
            self.grid[row][col] = "X"
            self.hits.add((row, col))
            return "hit"
        elif self.grid[row][col] == ".":
            self.grid[row][col] = "O"
            return "miss"
        return "repeat"

    def all_sunk(self):
        for ship in self.ships:
            if not ship.issubset(self.hits):
                return False
        return True
