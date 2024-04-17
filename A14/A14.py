# Part 1: Loading and Saving:
def load_data(fn: str) -> tuple[int, list[list[int]]]:
    # exception handling
    try:
        file = open(fn, "r")
    except FileNotFoundError:
        print("Input file does not exist")
        return -1
    # initialize vars, read first line
    out:    list = []
    row:    int  = 0
    count:  int  = 0
    line = file.readline()
    # iterate through csv lines
    while line != "":
        # split line, reset cleaned list
        lst = line.split(",")
        fin: list = []
        # iterate through the line
        for i in range(len(lst)):
            # if formattable to an int, 
            # add it to the cleaned list
            try:
                lst[i] = int(lst[i])
                fin += [lst[i]]
            # otherwise, we have a non-int,
            # print the row and col it was found at
            except ValueError:
                print([row, i])
        # append the cleaned list, iterate the row,
        # and sum integers loaded, read the next line
        out.append(fin)
        row += 1
        count += len(fin)
        line = file.readline()
    # close file and return information as tuple
    file.close()
    return (count, out)

def save_data(fn: str, data: list[tuple[float, float, tuple[int,...]]]) -> None:
    # open file and initialize list
    file = open(fn, "w")
    flat:list = []
    # iterate through data
    for i in range(len(data)):
        # if 
        try:
            first, *rest = data[i]          
            flat.append(first)
            flat.extend(rest)
        except TypeError:
            flat.append(data[i]) 
    for j in range(len(flat)):
        file.write(flat[j])

    file.close()

# Part 2: Processing:
def find_mean(lst: list[int]) -> float:
    sum: float = 0
    for i in range(len(lst)):
        sum += lst[i]
    avg = sum / len(lst)
    avg = round(avg, 1)
    return avg

def find_median(lst: list[int]) -> float:
    length = len(lst)
    for j in range(length):
        for i in range(length - 1):
            if lst[i] > lst[i + 1]:
                temp = lst[i + 1]
                lst[i + 1] = lst[i]
                lst[i] = temp
    
    if len(lst) % 2 == 0:
        left  = (len(lst) // 2) - 1
        right = (len(lst) // 2)
        temp_left = lst[left]
        temp_right = lst[right]
        temp = (temp_left + temp_right) / 2
        return temp
    temp = len(lst) // 2
    return lst[temp]
def find_mode(lst: list[int]) -> tuple[int, ...]:
    freqs: dict[int, int] = {}
    max: list = [0]
    tup_out: tuple = ()
    indiv: list = []
    for i in range(len(lst)):
        if freqs.get(lst[i], 0) == 0: 
            indiv.append(lst[i])

        freqs[lst[i]] = 1 + freqs.get(lst[i], 0)
        if freqs[lst[i]] > max[0]:
            max = [freqs[lst[i]]]

        
    for j in range(len(indiv)):
        if freqs[indiv[j]] == max[0]:
            tup_out += (indiv[j], )
    return tup_out

#Part 3: Analysis:
def analysis(fn_in: str, fn_out: str) -> None:
    file = open(fn_out, "w")
    tup = load_data(fn_in)
    out: list = []

    print("Loaded", str(tup[0]), "integers")

    lst = tup[1]
    for i in range(len(lst)):
        row = lst[i]
        mean = find_mean(row)
        median = find_median(row)
        mode = find_mode(row)
        line = (mean, median, mode)
        out.append(line)
    save_data(fn_out, out)
    file.close()

def main():
    analysis("A14\dataset_1.csv", "A14\out.csv")
    

if __name__ == "__main__":
    main()