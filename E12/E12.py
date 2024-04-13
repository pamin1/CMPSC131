# Part 1: Load and Save: 
def load_data(fn: str) -> dict:
    # initialize file
    file = open(fn, "r")
    line = file.readlines()
    file.close()

    # initialize vars
    name: str = line[0].strip("\n")
    board: list[list[int]] = []

    start:list[int] = line[2].split(",")
    start[0] = int(start[0])
    start[1] = int(start[1])

    exits: list[list[int]] = []
    steps: list[str] = []

    line1 = line[1].split(",")

    size: int = int(line1[0])
    num_exits: int = int(line1[1])
    
    board_start = 3 + num_exits
    
    for i in range(3, board_start):
        temp = line[i].split(",")
        for j in range(len(temp)): 
            temp[j] = int(temp[j])
        exits.append(temp)

    for i in range(board_start, len(line)):
        temp = line[i].split(",")
        for j in range(len(temp)):
            temp[j] = int(temp[j])
        board.append(temp)
    
    curr: list = [start[1], start[0]]
    seen: list[list] = []

    # compare distances from start to exit
    dist = distance(start, exits[0])
    index = 0
    for i in range(len(exits)):
        temp = distance(start, exits[i])
        if temp < dist:
            # track the index of the closest exit
            index = i
            dist = temp

    ext = [exits[index][1], exits[index][0]]

    # create dictionary:
    out = {"name" : name,
           "board": board,
           "size" : size,
           "start": start, 
           "exits": exits,
           "steps": steps,
           "curr" : curr,
           "seen" : seen,
           "final": ext
          }
    return out

def save_data(fn: str, data: dict) -> None:
    file = open(fn, "w")

    file.write("name: " + data.get("name") + "\n")
    file.write("size: ")
    file.write(str(data.get("size")))
    file.write("\n")
   
    # writing in size
    start = data["start"]
    x = str(start[0])
    y = str(start[1])
    file.write("Start: ")
    file.write("[" + x + ", " + y  + "]" + "\n")

    # write in steps...
    step_conv: dict = {"U": "UP", "D": "DOWN", "L": "LEFT", "R": "RIGHT"}
    steps = data.get("steps")
    nums = str(len(steps))
    file.write("Steps: " + nums)
    for i in range(len(steps)):
        word = step_conv.get(steps[i])
        file.write("\n" + word)
    file.close()

# Part 2: Recursive solving
def can_move(data: dict, col: int, row: int) -> bool:
    # pull neccessary information:
    board = data.get("board")
    b_col = data.get("size")
    b_row = data.get("size")

    # check out of bounds errors:
    if b_col <= col or col < 0 or b_row <= row or row < 0:
        return False

    # check if the spot is valid:
    if board[row][col] == 0:
        return True
    return False

def solve_helper(data: dict, col: int, row: int) -> None:
    # pull neccessary information:
    seen = data.get("seen")
    steps = data.get("steps")
    final = data.get("final")
    current = data.get("curr")

    # define moveset:
    MOVES = {"U": [-1, 0] , "D": [1, 0] , "L": [0, -1], "R": [0, 1]}

    while current != final:
        # define dictionary for possible moves
        pos_moves = moves(data, col, row)
        for i in range(len(pos_moves)):
            # if we did find some shortest step, we can pair the direction with
            # the corresponding change in x and y
            step = pos_moves[i]
            vector = MOVES.get(step)
            t_row = row + vector[0]
            t_col = col + vector[1]

            # now we update the list of steps and spots seen
            data["steps"] += step
            data["seen"]  += [[row,col]]
            data["curr"] = [t_row, t_col]

            # recurse with updated positions and data
            solve_helper(data, t_col, t_row)

            # update the position to check against base case
            # return out in this event
            current = data.get("curr")
            if current == final:
                return
        
        # if there is no possible move we have hit a dead end
        # in this case we pop the step to remove the direction
        # and we add the recently seen spot to the list of seen locations
        if len(pos_moves) == 0:
            steps.pop()
            seen += [[row, col]]
            return
        
    # return nothing once exit is reached
    return

# Part 3: Combining
def solve(input_fn: str, output_fn: str) -> None:
    # choose the closest exit
    data = load_data(input_fn)

    # get vals to call solve_helper():
    start = data.get("start")
    row = start[1]
    col = start[0]

    # call solver helper:
    solve_helper(data, col, row)

    # save data to file:
    save_data(output_fn, data)

# Helper Methods:
def moves(data: dict, col: int, row: int) -> list:
    # pull neccessary information:
    MOVES = ["U", "D", "L", "R"]
    pos_move: list = []

    # iterate through possible moves, check if the possible move is valid
    for i in range(len(MOVES)):
        if   MOVES[i] == "L":
            temp_r = row
            temp_c = col - 1

            if can_move(data, temp_c, temp_r) and closer(data, temp_c, temp_r):
                pos_move.append(MOVES[i])

        elif MOVES[i] == "R":
            temp_r = row
            temp_c = col + 1

            if can_move(data, temp_c, temp_r) and closer(data, temp_c, temp_r):
                pos_move.append(MOVES[i])

        elif MOVES[i] == "U":
            temp_r = row - 1
            temp_c = col

            if can_move(data, temp_c, temp_r) and closer(data, temp_c, temp_r):
                pos_move.append(MOVES[i])

        elif MOVES[i] == "D":
            temp_r = row + 1
            temp_c = col

            if can_move(data, temp_c, temp_r) and closer(data, temp_c, temp_r):
                pos_move.append(MOVES[i])
    
    # return the list of possible moves
    return pos_move

def distance(curr: list[int], dest: list[int]) -> int:
    curr_x: int = curr[0]
    curr_y: int = curr[1]

    dest_x: int = dest[0]
    dest_y: int = dest[1]  

    dx: int = dest_x - curr_x
    dy: int = dest_y - curr_y

    # quick mafs to find the shortest distance between a spot and the exit
    hyp = (dx**2 + dy**2) ** 0.5

    return hyp

def choose_exit(data: dict, start: list) -> None:
    # pull neccessary information
    exits = data.get("exits")

    # compare distances from start to exit
    dist = distance(start, exits[0])
    for i in range(len(exits)):
        temp = distance(start, exits[i])
        if temp < dist:
            # track the index of the closest exit
            lst = exits[i]

    # add the value to the index and return

    ext = [lst[1], lst[0]]

    data["final"] = ext
    return

def closer(data: dict, col: int, row: int) -> bool:
    seen  = data.get("seen")
    curr  = [row, col]

    # check if the spot has been seen before:
    for i in range(len(seen)):
        if curr == seen[i]:
            return False
    return True

def main():
    input  = "E12/examples/random_9x9.csv"
    output = "E12/output.txt"
    solve(input, output)
    

if __name__ == "__main__":
    main()