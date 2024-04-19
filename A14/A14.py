# Part 1: Loading and Saving:
def load_data(fn: str) -> tuple[int, list[list[int]]]:
    # exception handling
    try:
        file = open(fn, "r")
    except FileNotFoundError:
        print("Input file does not exist")
        return (-1, [])
    
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
                print("Row", row, end="")
                print(", Col", i, end = "")
                print(" was invalid")

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

    # iterate through entire data list
    for i in range(len(data)):
        row = data[i]

        # iterate through each row element
        for j in range(len(row)):
            # if the element is a tuple, we need to iterate through that on its own
            if isinstance(row[j], tuple):
                for k in range(len(row[j])):
                    val = str(row[j][k])
                    file.write(val)
                    if k < len(row[j]) - 1:
                        file.write(",")

            # otherwise we can just write in the value 
            else:
                val = str(row[j])
                file.write(val)

            # separate w/ commas up until the second to last value for formatting
            if j < len(row) - 1:
                file.write(",")
        # start new line after every row finishes
        file.write("\n")         
    file.close()

# Part 2: Processing:
def find_mean(lst: list[int]) -> float:
    # assertion
    assert len(lst) != 0, "List cannot be empty"   

    # perform average calculation over the list elements  
    sum: float = 0
    for i in range(len(lst)):
        sum += lst[i]
    avg = sum / len(lst)

    # multiply avg by ten to get tenths into ones place
    # rounds down for any value with new tenths place < 0.5
    # likewise can round up for tenths >= 0.5
    # divide by 10 to bring value back down to original decimal position
    temp = int(10 * avg - 0.5) + 1
    temp /= 10
    return temp

def find_median(lst: list[int]) -> float:
    # assertion
    assert len(lst) != 0, "List cannot be empty" 

    # bubble sort for the length of the list
    length = len(lst)
    for j in range(length):
        for i in range(length - 1):
            if lst[i] > lst[i + 1]:
                temp = lst[i + 1]
                lst[i + 1] = lst[i]
                lst[i] = temp

    # if the list is even, perform calculations to average the middle two index values
    if len(lst) % 2 == 0:
        left  = (len(lst) // 2) - 1
        right = (len(lst) // 2)
        temp_left = lst[left]
        temp_right = lst[right]
        temp = (temp_left + temp_right) / 2
        return temp
    
    # otherwise return the middle index value
    temp = len(lst) // 2
    return float(lst[temp])

def find_mode(lst: list[int]) -> tuple[int, ...]:
    # assertion
    assert len(lst) != 0, "List cannot be empty" 

    # keep a dictionary of the found frequencies
    freqs: dict[int, int] = {}
    max: int = 0
    tup_out: tuple = ()
    unique: list = []

    # if we havent seen the value before (freq = 0)
    # add it to a lst of unique values
    # then add it to the dict of frequency,
    # add to current value (0 if not found)
    for i in range(len(lst)):
        if freqs.get(lst[i], 0) == 0: 
            unique.append(lst[i])
        freqs[lst[i]] = 1 + freqs.get(lst[i], 0)

        # compare frequency value and max, 
        # update max as necessary
        if freqs[lst[i]] > max:
            max = freqs[lst[i]]

    # iterate through the list of unique values,
    # if the frequency of the value = the max recorded frequency,
    # add it to the tuple to be returned
    for j in range(len(unique)):
        if freqs[unique[j]] == max:
            tup_out += (unique[j], )
    return tup_out

#Part 3: Analysis:
def analysis(fn_in: str, fn_out: str) -> None:
    # intitialize
    tup = load_data(fn_in)
    out: list = []

    # first print statement
    print("Loaded", tup[0], "integers")

    # iterate and apply functions through the data list
    lst = tup[1]
    for i in range(len(lst)):
        row = lst[i]
        mean = find_mean(row)
        median = find_median(row)
        mode = find_mode(row)
        line = (mean, median, mode)
        out.append(line)

    # save the data and close
    save_data(fn_out, out)

def main():
    analysis("A14\dataset_3.csv", "A14\out.csv")
    

if __name__ == "__main__":
    main()