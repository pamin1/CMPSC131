PLAYER_DATA: dict[int, tuple[str, str]] = {
   0: ("X", "Player 1: input row and column: X> "),
   1: ("O", "Player 2: input row and column: O> "),
}

def init() -> list[list[str]]:
   """Creates a new, empty board.

    Returns:
        list[list[str]]: An empty 3x3 board.
    """
   board = []
   for _ in range(3):
       row = []
       for _ in range(3):
           row.append("")
       board.append(row)
   return board

def show(board: list[list[str]]) -> None:
   """Displays the board on the console.

    Args:
        board (list[list[str]]): The board to display.
    """
   LINE = "+---+---+---+"

   print("\n", LINE, sep="")
   for i in range(3):
       t0, t1, t2 = board[i]
       print(f"| {t0:1} | {t1:1} | {t2:1} |\n", LINE, sep="")
   print()

# Completed 1
def put(player: int, row: int, col: int, board: list[list[str]]) -> None:
    """Puts a token on the board.

    Args:
        player (str): The player to place; `0` for player one and `1` for
        player two.
        row (int): The row to place the token on.
        col (int): The column to place to token on.
        board (list[list[str]]): The board.

    Exceptions:
        Assert when trying to place a token in an invalid cell.
    """
    assert row >= 0 and row < 3, "invalid row"
    assert col >= 0 and col < 3, "invalid column"
    assert board[row][col] == '', "spot taken, try again"
    data_tup = PLAYER_DATA[player]

    board[row][col] = data_tup[0]
# Completed 2
def get(player: int) -> tuple[int, int]:
    """Gets and converts user input into a row/col pair.

    Args:
        player (str): The player to prompt; `0` for player one and `1` for
        player two.

    Returns:
        tuple[int, int]: The row and column selected by the user.
    """
    data = PLAYER_DATA[player][1]
    coor = input(data)
    temp = coor.split()

    try:
        assert int(temp[0]) < 3  or int(temp[1]) < 3, "invalid row and column"
        assert int(temp[0]) >= 0 and int(temp[0]) < 3, "invalid row"
        assert int(temp[1]) >= 0 and int(temp[1]) < 3, "invalid column"
    except ValueError:
        print("(invalid input, input contains c)haracters")

    return (int(temp[0]),int(temp[1]))
# Completed 3
def won(player: int, row: int, col: int, board: list[list[str]]) -> bool:
    """Check if the player has won after taking the row and column specified.

    Args:
        player (str): The player to prompt; `0` for player one and `1` for
        player two.
        row (int): The row that was just taken.
        col (int): The column that was just taken.
        board (list[list[str]]): The board.

    Returns:
        bool: If the token won (has three in a row).
    """
    data = PLAYER_DATA[player]
    char = data[0]
    won = False
    for val in board[row]:
        if val == char:
            won = True
    if won == True:
        return True
    
    for i, val in enumerate(board[i][col]):
        if val == char:
            won = True
    if won == True:
        return True
    
    for i in range(len(board)):
        if board[i][i] == char:
            won = True
    if won == True:
        return True
    
    return False
def tic_tac_toe_loop() -> None:
   """The game loop for our application. Handles a single round of tic-tac-toe.
    """
   has_won = False
   while has_won == False:
       for i in range(0,2):
           coor_tup = get(i)
           
def tic_tac_toe():
   """An application for playing tic-tac-toe. Calls the game loop and then asks
    if you'd like to play again.
    """
def main():
    board = init()
    put(0, 1, 1, board)
    print(get(0))
    show(board)

if __name__ == "__main__":
    main()