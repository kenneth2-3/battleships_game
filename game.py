import string
from board import Board


def parse_input(user_input, size):
    try:
        col = string.ascii_uppercase.index(user_input[0].upper())
        row = int(user_input[1:]) - 1
        if row < 0 or col >= size:
            raise ValueError("Out of bounds")
        return row, col
    except (ValueError, IndexError):
        return None
