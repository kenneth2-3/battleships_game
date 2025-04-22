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
                    print('X' if self.grid[row][col] == 'S' else self.grid[row][col], end=" ")
            print()
