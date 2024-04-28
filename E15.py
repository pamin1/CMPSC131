PLAYER_MOVES = {1: ("X", "Player 1 moves to "), 2: ("O", "Player 2 moves to ")}

def render(board: list[list[str]], winner: set[tuple[int, int]] | None) -> None:
    """Renders the game board to the console.

    ----------------------------------------------------------------------------

    ## The Board

    The `board` must be a list with as many rows as the final, square rendered
    output should be. It must also be in column-major order, meaning that each
    row in the list represents a column in the rendered output. For example, a
    list that looks like this:

    ```python
    board = [
        ["X", "X"],
        ["X", "O", "X"],
        ["O"],
        [],
        ["O"],
    ]
    ```

    Would map to an output that looks like this:
    ```text
        +---+---+---+---+---+
        |   |   |   |   |   |
        +---+---+---+---+---+
        |   |   |   |   |   |
        +---+---+---+---+---+
        |   | X |   |   |   |
        +---+---+---+---+---+
        | X | O |   |   |   |
        +---+---+---+---+---+
        | X | X | O |   | O |
        +---+---+---+---+---+
    ```

    The board can be a jagged list, with missing entries assumed to be blank.

    Each token in the board should be a single character wide; e.g. length = 1.

    ----------------------------------------------------------------------------

    ## Winning Cells

    When a winner has been found, you can pass in a set of (row, column) pairs
    indicating which of cells should be rendered with emphasis to highlight the
    winner. The `row` and `column` pairs should refer to the row and column of
    the list, **not** the final rendered product.

    As an example, if player one won with this board:

    ```text
        +---+---+---+---+---+
        |   |   |   |   |   |
        +---+---+---+---+---+
        |   |   |   | X |   |
        +---+---+---+---+---+
        |   |   | X | O |   |
        +---+---+---+---+---+
        |   | X | X | O |   |
        +---+---+---+---+---+
        | X | O | O | O | X |
        +---+---+---+---+---+
    ```

    We could highlight the winning cells using a set with the following values:

    ```python
    winner = { (0, 0), (1, 1), (2, 2), (3, 3) }
    ```

    This would produce a board that looks as follows:
        ```text
        +---+---+---+---+---+
        |   |   |   |   |   |
        +---+---+---+---+---+
        |   |   |   |(X)|   |
        +---+---+---+---+---+
        |   |   |(X)| O |   |
        +---+---+---+---+---+
        |   |(X)| X | O |   |
        +---+---+---+---+---+
        |(X)| O | O | O | X |
        +---+---+---+---+---+
    ```

    ----------------------------------------------------------------------------

    Args:
        board (list[list[str]]): A column-major list of the tokens to render.
        winner (set[tuple[int, int]] | None): A set of row/column pairs marking\
            the winning cells of the board. Each tuple should be a (row, col)\
            pair, where the `row` and `col` are the respective values **in the\
            list, not render**. If there is no winner, this should be `None`.

    Exceptions:
        Asserts if the size of the board is not at least 4.
    """
    size = len(board)  # Make sure length makes sense...
    assert size >= 4, f"The board size must be >= 4, not {size}"

    # Make winner an empty set it if was None
    if not isinstance(winner, set):
        winner = set[tuple[int, int]]()

    for R in range(size - 1, -1, -1):  # Rows (for printing)
        print("    ", "+---" * size, "+", sep="")

        print("    ", end="")
        for C in range(size):  # Columns (for printing)
            if R < len(board[C]):  # Check if there's really data
                # Note that `C` is first; column-major order!
                token = board[C][R]

                # Note that `(R, C)` is about the list itself, not the render!
                if winner.issuperset(((R, C),)):
                    print(f"|({token:1})", end="")  # Winner!
                else:
                    print(f"|{token:^3}", end="")

            else:  # Jagged; assume blank
                print("|   ", end="")
        print("|")
    print("    ", "+---" * size, "+", sep="")


def mark_winner(player: int, cells: set[tuple[int, int]] | None) -> None:
    """A special function for the Ag to know who won a match. If no one won as
    there was a tie, you should indicate player `0` won and provide an empty
    set.

    For your code, this doesn't do anything, but it will have special meaning to
    the Ag. You do not need to write any code for this function.

    Args:
        player (int): The player who won; either `1` or `2`. If no one won,\
            this should be `0`.
        cells (set[tuple[int, int]] | None): The cells that caused the win, as\
            a set of (row, col) pairs into the list, not the rendered board. If
            no one won, this should be `None`.
    """
    pass


def get_size():
    size: str = input(f"Size of Board? ")

    if size == "":
        print("default size")
        size = 7

    condition: bool = True
    while condition:
        try:
            size = int(size)
            if size < 4:
                print(f"Size must be greater than 4. Try Again: ")
                size: str = input(f"Size of Board? ")
            else:
                condition = False

        except ValueError:
            print(f"Size must be an integer. Try Again: ")
            size: str = input(f"Size of Board? ")

    board: list = []
    for i in range(size):
        board.append([])
    return board


def move(player: int, board: list[list[str]]):
    move: str = input(f"Player {player} move:")
    try:
        y = int(move)
    except ValueError:
        print("invalid move, try again")
        return False
    
    if y >= 0 and y < len(board) and len(board[y]) < len(board):
        board[y].append(PLAYER_MOVES[player][0])
    else:
        print("invalid move, try again")
        return False
    return board


def full(board: list[list[str]]) -> bool:
    condition = False
    count = 0
    for R in range(len(board)):
        if len(board[R]) == len(board):
            count +=1
        else:
            count = 0
    if count == len(board):
        condition = True
    return condition

def connect_four() -> None:
    board = get_size()
    render(board, {})
    while not full(board):
        for i in range(1,3):
            temp = move(i, board)
            while temp == False:
                temp = move(i, board)
            winning_set = checker(i, board)
            render(temp, winning_set)
            if isinstance(winning_set, set):
                mark_winner(i, winning_set)
                print(f'Player {i} wins!')
                return
            
            elif full(board):
                mark_winner(0, None)
                print(f'Player 0 wins')
                return
            
        if isinstance(winning_set, set) or full(board):
            return


def checker(player: int, board: list[list[str]]) -> tuple[tuple[int,int]]:
    char = PLAYER_MOVES[player][0]

    # note that each row in the board list represents a column
    
    # checking rows:
    row_out: list = []
    for C in range(len(board)):
        for R in range(len(board)):
            try:
                val = board[R][C]
                if char == val:
                    row_out.append((R,C))
                else:
                    row_out.clear()

                if len(row_out) == 4:
                    return set(row_out)
            except IndexError:
                row_out.clear()
        row_out.clear()

        if len(row_out) == 4:
            return set(row_out)

    # checking cols:
    col_out: list = []
    for R in range(len(board)):
        for C in range(len(board[R])):
            try:
                val = board[R][C]
                if char == val:
                    col_out.append((R,C))
                else:
                    col_out.clear()

                if len(col_out) == 4:
                    return set(col_out)
            except IndexError:
                col_out.clear()
        col_out.clear()
    
    # checking diagonals
    diag_out: list = [] 
    for R in range(len(board) - 3):
        for C in range(len(board) - 3):
            try:
                if board[R][C] == char and board[R+1][C+1] == char and board[R+2][C+2] == char and board[R+3][C+3] == char:
                    diag_out.append((R,C))
                    diag_out.append((R+1,C+1))
                    diag_out.append((R+2,C+2))
                    diag_out.append((R+3,C+3))
                else:
                    diag_out.clear()

                if len(diag_out) == 4:
                    return set(diag_out)
                
            except IndexError:
                diag_out.clear()      
        
    for R in range(3,len(board)):
        for C in range(len(board) - 3):
            try:
                if board[R][C] == char and board[R-1][C+1] == char and board[R-2][C+2] == char and board[R-3][C+3] == char:
                    diag_out.append((R,C))
                    diag_out.append((R-1,C+1))
                    diag_out.append((R-2,C+2))
                    diag_out.append((R-3,C+3))
                else:
                    diag_out.clear()

                if len(diag_out) == 4:
                    return set(diag_out)
                
            except IndexError:
                diag_out.clear()
        

def main():
    connect_four()


if __name__ == "__main__":
    main()
