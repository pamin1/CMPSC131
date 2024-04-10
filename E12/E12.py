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
    
    true_start = start.copy()
    temp_y = true_start[0]
    true_start[0] = true_start[1]
    true_start[1] = temp_y
    

    exits: list[list[int]] = []
    steps: list[str] = []

    line1 = line[1].split(",")
    size: int = int(line1[0])
    num_exits: int = int(line1[1])
    if len(line) > 3:
        for i in range(3, 3 + num_exits):
            temp = line[i].split(",")
            for j in range(len(temp)): 
                temp[j] = int(temp[j])
            exits.append(temp)

    board_start = 3 + num_exits
    for i in range(board_start, len(line)):
        temp = line[i].split(",")
        for j in range(len(temp)):
            temp[j] = int(temp[j])
        board.append(temp)
    curr: list = start
    seen: list[list] = []

    most_rec: list = []

    # create dictionary:
    out = {"name" : name,
           "board": board,
           "size" : size,
           "start": start, 
           "exits": exits,
           "steps": steps,
           "curr" : curr,
           "seen" : seen,
           "inter": most_rec,
           "true_s": true_start
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

    # check for edge case:
    if board == []:
        return False
    
    # check out of bounds errors:
    if b_col <= col or col < 0 or b_row <= row or row < 0:
        return False

    # check if the spot is valid:
    if board[row][col] == 0:
        return True
    return False

def solve_helper(data: dict, col: int, row: int) -> None:
    # pull neccessary information:
    start = data.get("true_s")
    choose_exit(data, start)
    final = data.get("final")
    current = [row, col]
    curr_row = row
    curr_col = col
    data["curr"] = current
    hyp_dict: dict = {}

    # define moveset:
    MOVES = [["U", -1, 0] , ["D", 1, 0] , ["L", 0, -1], ["R", 0, 1]]

    while current != final:
        # pick an arbitrary int value for the current distance to exit
        # arbitrary in case path is not linearly approaching exit
        curr_hyp = 1000

        # define dictionary for possible moves
        hyp_dict = moves(data, col, row)
        index = 0
        # for all possible moves, find the best one
        for i in range(len(MOVES)):
            if hyp_dict.get(MOVES[i][0], 10000) <= curr_hyp:
                index = i 
                curr_hyp = hyp_dict.get(MOVES[i][0])

        # we previously tracked the index value of the shortest path step
        # using this index; if we have no viable option we need to backtrack
        if index == 0:
            backup = backtrack(data)
            return solve_helper(data, backup[1], backup[0])
        
        # if we did find some shortest step, we can pair the direction with
        # the corresponding change in x and y
        t_row = curr_row + MOVES[index][1]
        t_col = curr_col + MOVES[index][2]

        # now we update the list of steps and spots seen
        data["steps"] += [MOVES[index][0]]
        data["seen"]  += [[row,col]]

        # recurse with updated positions and data
        return solve_helper(data, t_col, t_row)
    
    # return nothing once exit is reached
    return

# Part 3: Combining
def solve(input_fn: str, output_fn: str) -> None:
    # choose the closest exit
    data = load_data(input_fn)

    # get vals to call solve_helper():
    start = data.get("true_s")
    row = start[0]
    col = start[1]

    # call solver helper:
    solve_helper(data, col, row)

    # save data to file:
    save_data(output_fn, data)

# Helper Methods:
def moves(data: dict, col: int, row: int) -> dict:
    # pull neccessary information:
    exits = data.get("exits")
    curr_row = row
    curr_col = col
    hyp_dict: dict = {}
    count = 0
    MOVES = ["U", "D", "L", "R"]

    # iterate through possible moves, check if the possible move is valid
    # then find the distance between that spot and the exit
    # add move-length correspondance to dictionary 
    for i in range(len(MOVES)):
        if   MOVES[i] == "L":
            temp_r = curr_row
            temp_c = curr_col - 1

            if can_move(data, temp_c, temp_r) and closer(data, temp_c, temp_r):
                count += 1
                l_weight = distance([temp_r, temp_c], exits[0])
                hyp_dict["L"] = l_weight

        elif MOVES[i] == "R":
            temp_r = curr_row
            temp_c = curr_col + 1

            if can_move(data, temp_c, temp_r) and closer(data, temp_c, temp_r):
                count += 1
                r_weight = distance([temp_r, temp_c], exits[0])
                hyp_dict["R"] = r_weight

        elif MOVES[i] == "U":
            temp_r = curr_row - 1
            temp_c = curr_col

            if can_move(data, temp_c, temp_r) and closer(data, temp_c, temp_r):
                count += 1
                u_weight = distance([temp_r, temp_c], exits[0])
                hyp_dict["U"] = u_weight

        elif MOVES[i] == "D":
            temp_r = curr_row + 1
            temp_c = curr_col

            if can_move(data, temp_c, temp_r) and closer(data, temp_c, temp_r):
                count += 1
                d_weight = distance([temp_r, temp_c], exits[0])
                hyp_dict["D"] = d_weight
    
    # simultaneously check if the current spot is an "intersection"
    # a.k.a are there multiple paths available
    # works as a "checkpoint" where we can restart from in backtrack()
    if count >= 2:
        data["inter"] = [row, col]
    
    # return our precious values *golum imitation*
    return hyp_dict

def distance(curr: list[int], dest: list[int]) -> int:
    curr_x: int = curr[0]
    curr_y: int = curr[1]

    dest_x: int = dest[0]
    dest_y: int = dest[1]  

    dx: int = dest_x - curr_x
    dy: int = dest_y - curr_y

    hyp = (dx**2 + dy**2) ** 0.5
    # quick mafs to find the shortest distance between a spot and the exit
    return hyp

def backtrack(data: dict) -> None:
    # pull neccessary information:
    seen  = data.get("seen")
    steps = data.get("steps")
    inter = data.get("inter")

    # remove our intersection point from seen spots
    # as it will be our new start point
    seen.remove(inter)

    # remove the corresponding steps from the end of the steps list
    while len(seen) != len(steps):
        steps.pop()

    # need to pop one final step to even the lengths properly
    steps.pop()

    # resulting seen list is closed at deadend paths on intersections
    return inter

def choose_exit(data: dict, start: list):
    # pull neccessary information
    exits = data.get("exits")

    # compare distances from start to exit
    dist = distance(start, exits[0])
    index = 0
    for i in range(len(exits)):
        temp = distance(start, exits[i])
        if temp < dist:
            # track the index of the closest exit
            index = i
            dist = temp

    # add the value to the index and return
    ext = exits[index]
    temp_y = ext[0]
    ext[0] = ext[1]
    ext[1] = temp_y

    data["final"] = ext
    return

def closer(data: dict, col: int, row: int):
    seen  = data.get("seen")
    curr  = [row, col]

    # check if the spot has been seen before:
    for i in range(len(seen)):
        if curr == seen[i]:
            return False
    return True

def main():
    input  = "E12/examples/random_5x5.csv"
    output = "est.txt"
    solve(input, output)
    

if __name__ == "__main__":
    main()