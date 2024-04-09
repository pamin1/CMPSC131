def absolute(value):
    if(value < 0):
        value *= -1
    return value

def manual_multiply(num1, num2):
    total = 0
    a_neg = num1 < 0
    b_neg = num2 < 0
    if(a_neg):
        num1 = -num1
    if(b_neg):
        num2 = -num2

    for i in range(0, num2):
        total += num1
    if(a_neg or b_neg):
        total = -total
    return total

def vector_1(num_x1, num_y1, num_x2, num_y2):
    change_x = (num_x2 - num_x1) ** 2
    change_y = (num_y2 - num_y1) ** 2
    distance = (change_x + change_y) ** 0.5

    return distance

def vector_2(x,y):
    print("(", x, ", ", y, ")", sep="")

def vector_3(num_x1, num_y1, num_x2, num_y2):
    x = num_x2 - num_x1
    y = num_y2 - num_y1
    vector_2(x,y)

def vector_4(num_x1, num_y1, num_x2, num_y2):
    x = num_x2 - num_x1
    y = num_y2 - num_y1

    change_x = (num_x2 - num_x1) ** 2
    change_y = (num_y2 - num_y1) ** 2
    distance = (change_x + change_y) ** 0.5

    norm_x = x / distance
    norm_y = y / distance

    vector_2(norm_x, norm_y)

def times_tables(n1, n2):
    for i in range(n1, n2 + 1):
        for k in range(n1, n2 + 1):
            print(i * k, "\t", end="")
        print()
    
def minimums(list):
    if(len(list) == 0):
        print("error")
        return
    temp_low = list[0]
    for i in range(len(list)):
        if(temp_low > list[i]):
            temp_low = list[i]
    print(temp_low)

def maximums(list):
    if(len(list) == 0):
        print("error")
        return
    temp_high = list[0]
    for i in range(len(list)):
        if(list[i] > temp_high):
            temp_high = list[i]
    print(temp_high)

def min_max(list):
    if len(list) == 0:
        print("error")
        return
    
    temp_high = list[0]
    temp_low  = list[0]

    for i in range(len(list)):
        if(list[i] > temp_high):
            temp_high = list[i]
        elif(list[i] < temp_low):
            temp_low = list[i]

    new = [temp_low, temp_high]
    print(new)

def filter(list,low,high):
    new = []
    for i in range(len(list)):
        if low < list[i] < high:
            new += [list[i]]
    print(new)

def hill(height):
    string = "*"
    for i in range(1, height):
        print(string)
        string += "*"

    for i in range(height, 0, -1):
        string = ""
        for k in range(i, 0, -1):
            string += "*"
        print(string)

def trees(height):
    trunk_spacing = ""
    spacing_start = height - 1
    for i in range(height + 1):

        spacing = ""
        leaves = ""
        branch_length = 2 * i - 1

        for k in range(spacing_start, i - 1, -1):
            spacing += " "
        for j in range(branch_length):
            leaves += "*"
        print(spacing, leaves, sep='')
# print trunk
    for n in range(spacing_start):
        trunk_spacing += " "
    print(trunk_spacing, "=", sep='')

def solution_1365(list):
    less_list = []
    for i in range(len(list)):
        less_list += [solution_1365_sub(list[i], list)]
    print(less_list)    

def solution_1365_sub(num, list):
    count = 0
    for i in range(len(list)):
        if num > list[i]:
            count += 1
    return count

def main():
    trees(4)
if __name__ == "__main__":
    main()