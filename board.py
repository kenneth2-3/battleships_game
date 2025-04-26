import random


class Board:
    """A class representing the Battleships game board."""

    def __init__(self, size):
        """
        Initialize the game board with a given size.

        Args(Argument):
            size (int): Size of the board (number of rows and columns).
        """
        self.size = size
        self.grid = [['.' for _ in range(size)] for _ in range(size)]
        self.ships = []
        self.missed_guesses = []  # To track missed guesses

    def print_board(self, reveal_ships=False):
        """
        Print the current state of the board.

        Args:
            reveal_ships (bool): If True, shows all ships;
            otherwise hides ships.
        """
        # Print column labels
        print("  ", end="")
        for col in range(self.size):
            print(chr(65 + col), end=" ")
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
                        print('X', end=" ")  # To hide ships during the game
                    else:
                        print(cell_value, end=" ")
            print()

    def place_ship(self, size):
        """
        Randomly place a ship of given size on the board.

        Args:
            size (int): Size of the ship to place.
        """
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
        """
        Handle a player's guess on the board.

        Args:
            coord (tuple): A tuple (row, col) of the guessed coordinates.

        Returns:
            str: Result of the guess ("hit", "miss", "off", or "repeat").
        """
        row, col = coord
        if row < 0 or col < 0 or row >= self.size or col >= self.size:
            return "off"  # Guess is out of bounds
        elif self.grid[row][col] == 'S':
            self.grid[row][col] = 'X'  # Mark a hit
            return "hit"
        elif self.grid[row][col] == '.':
            self.grid[row][col] = 'O'  # Mark a miss
            self.missed_guesses.append(coord)  # Track missed guesses
            return "miss"
        else:
            return "repeat"  # Already guessed this cell

    def all_sunk(self):
        """
        Check if all ships have been sunk.

        Returns:
            bool: True if all ships are sunk, False otherwise.
        """
        return all(cell != 'S' for row in self.grid for cell in row)

    def remaining_ships(self):
        """
        Count the number of remaining (not yet hit) ship parts.

        Returns:
            int: Number of remaining ship parts.
        """
        return sum(cell == 'S' for row in self.grid for cell in row)
