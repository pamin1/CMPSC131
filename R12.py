def _color(code: str, line: str) -> str:
    if code == "":
        return line
    return "\033[" + code + "m" + line + "\033[0m"

def _color_dict(code: str, data: dict[str, str]) -> None:
    if code != "":
        keys = list(data.keys())
        for i in range(len(data)):
            data[keys[i]] = "\033[" + code + "m" + data[keys[i]] + "\033[0m"

def print_path(board: list[list[int]], start: list[int], instr: list[str]):
    """Prints the indicated path along the provided board.

    Args:
        board (list[list[int]]): A square 2D list of integers; `0`, `1`, or `2`.
        start (list[int]): The starting point; `[column, row]`.
        instr (list[str]): A list of instructions; `'U'`, `'D'`, `'L'`, `'R'`.
    """

    # If you don't want colors, uncomment the other dictionary
    COLORS = {"BOR": "1;90", "PAT": "1;94", "EXT": "0;95"}
    # COLORS = {"BOR": "", "PAT": "", "EXT": ""}

    TOKENS = {"U": "↑", "R": "→", "D": "↓", "L": "←"}
    _color_dict(COLORS["PAT"], TOKENS)
    OFFSETS = {"U": [0, -1], "R": [1, 0], "D": [0, 1], "L": [-1, 0]}
    BORDER_LIN = _color(COLORS["BOR"], "#" * (len(board) + 2))
    BORDER_BIT = _color(COLORS["BOR"], "#")

    # Convert the board into a board of strings
    _game_board: list[list[str]] = []
    for i in range(len(board)):
        _game_board_row: list[str] = []
        for j in range(len(board)):
            if board[i][j] == 1:
                _game_board_row.append(BORDER_BIT)
            else:
                _game_board_row.append(" ")
        _game_board.append(_game_board_row)

    # Print out the instructions
    col = start[0]
    row = start[1]
    for i in range(len(instr)):
        _game_board[row][col] = _color(COLORS["PAT"], TOKENS[instr[i]])

        offset = OFFSETS[instr[i]]
        col += offset[0]
        row += offset[1]
    _game_board[row][col] = _color(COLORS["EXT"], "X")

    # Print out board with a border
    print(BORDER_LIN)
    for i in range(len(_game_board)):
        print(BORDER_BIT, "".join(_game_board[i]), BORDER_BIT, sep="")
    print(BORDER_LIN)

def fib(num: int) -> int:
    if num <= 0:
        return 0
    elif num == 1:
        return 1
    elif num == 2:
        return 2
    else:
        return fib(num - 1) + (num - 2)
    
def fib_dict(num: int, mem: dict[int, int]):
    if num <= 0:
        return 0
    if num == 1:
        return 1
    elif num == 2:
        return 2
    
    val = mem.get(num, -1)
    if val == -1:
        fib_sum = fib_dict(num - 1, mem) + fib_dict(num - 2, mem)
        mem[num] = fib_sum
        return fib_sum
    else:
        return mem[num]
    
def solve(board: list[list[int]], start: list[int]):
    instructions = []
    solve_helper(board, instructions, start[0], start[1])


def is_exit(board, row, col):
    if board[row][col] == 2:
        return True
    else:
        return False
    
def is_oob(board, row, col):
    if(
        not 0 <= row < len(board) or
        not 0 <= col < len(board) or
        not board[row][col] == -1
    ):
        return False
    return True

def solve_helper(board, instructions, row, col):
    
    if is_exit(board, row, col):
        return True
    
    board[row][col] = -1

    ALL_MOVES = [
        ["U", -1, 0],
        ["R", 0, 1],
        ["D", 1, 0], 
        ["L", 0, -1]
    ]

    for i in range(len(ALL_MOVES)):
        MOVE = ALL_MOVES[i]

        new_row = row + MOVE[1]
        new_col = col + MOVE[2]

        if is_oob(board, new_row, new_col):
            instructions.append(MOVE[0])
            if solve_helper(board, instructions, new_row, new_col):
                board[row][col] = 0
                return True
            else:
                instructions.pop()
    board[row][col] = 0
    return False

    
def main():
    print(fib_dict(5, {}))
    

if __name__ == "__main__":
    main()