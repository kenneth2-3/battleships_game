import random


class Board:
    def __init__(self, size):
        self.size = size
        self.grid = [['.' for _ in range(size)] for _ in range(size)]
        self.ships = []
        self.missed_guesses = []  # To Track missed guesses


def print_board(self, reveal_ships=False):
    # Print column labels
    print("  ", end="")
    for col in range(self.size):
        print(chr(65 + col), end=" ")  # A, B, C, D...
    print()

    # Print rows with row numbers
    for row in range(self.size):
        print(f"{row + 1:2} ", end="")
        for col in range(self.size):
            if reveal_ships:
                print(self.grid[row][col], end=" ")
            else:
                cell_value = self.grid[row][col]
                if cell_value == 'S':
                    print('X', end=" ")
                else:
                    print(cell_value, end=" ")
        print()

    def place_ship(self, size):
        placed = False
        while not placed:
            row = random.randint(0, self.size - 1)
            col = random.randint(0, self.size - 1)
            direction = random.choice(["horizontal", "vertical"])

            if direction == "horizontal" and col + size <= self.size:
                if all(self.grid[row][col + i] == '.' for i in range(size)):
                    for i in range(size):
                        self.grid[row][col + i] = 'S'
                    placed = True
            elif direction == "vertical" and row + size <= self.size:
                if all(self.grid[row + i][col] == '.' for i in range(size)):
                    for i in range(size):
                        self.grid[row + i][col] = 'S'
                    placed = True

    def guess(self, coord):
        row, col = coord
        if row < 0 or col < 0 or row >= self.size or col >= self.size:
            return "off"  # Out of bounds
        elif self.grid[row][col] == 'S':
            self.grid[row][col] = 'X'  # Hit
            return "hit"
        elif self.grid[row][col] == '.':
            self.grid[row][col] = 'O'  # Miss
            self.missed_guesses.append(coord)  # Track missed guesses
            return "miss"
        else:
            return "repeat"  # Already guessed

    def all_sunk(self):
        return all(cell != 'S' for row in self.grid for cell in row)
