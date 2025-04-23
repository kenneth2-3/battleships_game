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


def start_game():
    print("Welcome to Battleships!")

    while True:
        try:
            size = int(input("Enter grid size (5–10): "))
            if 5 <= size <= 10:
                break
            print("Please enter a number between 5 and 10.")
        except ValueError:
            print("Invalid number. Try again.")

    board = Board(size)
    ship_sizes = [3, 2, 2]  # Example: 3 ships of sizes 3, 2, and 2
    for ship_size in ship_sizes:
        board.place_ship(ship_size)

    turn = 1
    while not board.all_sunk():
        print("\nCurrent Board:")
        board.print_board()

        # Shows how many ship parts are still on the board
        remaining = sum(row.count('S') for row in board.grid)
        print(f"Ship parts remaining: {remaining}")

        print(f"Missed guesses: {board.missed_guesses}")
        guess = input(f"Turn {turn} - Enter your guess (e.g., A3): ").strip()
        coord = parse_input(guess, size)

        if coord is None:
            print("Invalid input. Format should be like A3.")
            continue

        result = board.guess(coord)
        print(f"Result: {result}")

        if result == "off":
            print("Your guess is off the grid. Try again.")
        elif result == "repeat":
            print("You already guessed that. Try again.")
        elif result == "hit":
            print("Hit!")
        elif result == "miss":
            print("Miss!")

        turn += 1

    print("\n You sank all the ships!")
    print(f"Game completed in {turn - 1} turns.")
    board.print_board(reveal_ships=True)
