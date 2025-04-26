import string
from board import Board
from colorama import Fore, init

init(autoreset=True)  # This automatically resets the color after each print


def parse_input(user_input, size):
    """
    Parses the user's input (e.g., 'A3') into grid coordinates.

    Args:
        user_input (str): The guess entered by the player.
        size (int): The size of the game grid.

    Returns:
        tuple: (row, col) coordinates if valid, or None if input is invalid.
    """
    try:
        col = string.ascii_uppercase.index(user_input[0].upper())
        row = int(user_input[1:]) - 1
        if row < 0 or col >= size:
            raise ValueError("Out of bounds")
        return row, col
    except (ValueError, IndexError):
        return None


def start_game():
    """
    Starts and controls the main flow of the Battleships game.

    - Sets up the game board.
    - Places ships randomly.
    - Accepts user guesses.
    - Displays hits, misses, and the board after each guess.
    - Ends the game when all ships are sunk.
    """
    print(Fore.CYAN + "Welcome to Battleships!\n")

    while True:
        try:
            size = int(input("Enter grid size (5–10): "))
            if 5 <= size <= 10:
                break
            print(Fore.YELLOW + "Please enter a number between 5 and 10.")
        except ValueError:
            print(Fore.RED + "Invalid number. Try again.")

    board = Board(size)
    ship_sizes = [3, 2, 2]  # Example: 3 ships of sizes 3, 2, and 2
    for ship_size in ship_sizes:
        board.place_ship(ship_size)

    turn = 1
    while not board.all_sunk():
        print(Fore.MAGENTA + "\n Current Board:")
        board.print_board()
        print(Fore.YELLOW + f"Ship parts remaining: {board.remaining_ships()}")
        print(Fore.BLUE + f"Missed guesses: {board.missed_guesses}")
        prompt = Fore.CYAN + f"Turn {turn} - Enter your guess (e.g., A3): "
        guess = input(prompt).strip()
        coord = parse_input(guess, size)

        if coord is None:
            print(Fore.YELLOW + "Invalid input. Format should be like A3.")
            continue

        result = board.guess(coord)
        if result == "off":
            print(Fore.BLUE + "Your guess is off the grid. Try again.")
        elif result == "repeat":
            print(Fore.YELLOW + "You already guessed that. Try again.")
        elif result == "hit":
            print(Fore.GREEN + "Hit!")
        elif result == "miss":
            print(Fore.RED + "Miss!")

        turn += 1

    print(Fore.GREEN + "\n You sank all the ships!")
    print(Fore.CYAN + f"Game completed in {turn - 1} turns.\n")
    print(Fore.MAGENTA + "Final Board (ships revealed):")
    board.print_board(reveal_ships=True)
