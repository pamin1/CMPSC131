#-------------------------#
# Question 1: List Utilities
def copy_list(list_a):
    list_b = []
    for i in range(len(list_a)):
        list_b += [list_a[i]]
    print(list_b)
    return list_b

def reverse_list(list_a):
    list_b = []
    for i in range(len(list_a) - 1, -1, -1):
        list_b += [list_a[i]]
    print(list_b)
    return list_b

def modify_list(num, list_a):
    list_b = []
    for i in range(len(list_a)):
        list_b += [num + list_a[i]]
    print(list_b)
    return list_b

def combine_lists(list_a, list_b):
    list_sum = []
    limit = 0
    if(len(list_a) < len(list_b)):
        limit = len(list_a)
    else:
        limit = len(list_b)
    for i in range(limit):
        list_sum += [list_a[i] + list_b[i]]
    print(list_sum)
    return list_sum
#-------------------------#
# Question 2: Blackjack
def bust(hand):
    sum = 0
    for i in range(len(hand)):
        sum += hand[i]        
        if(sum > 21):
            i += 1
            return i
    
def blackjack(hand):
    sum = 0
    for i in range(len(hand)):
        if(hand[i] % 1 != 0 or hand[i] < 1 or hand[i] > 11):
            print("cheating")
            return 
        sum += hand[i]
    if(sum > 21):
        count = bust(hand)
        print("total:", sum, "is a bust!",
              "blame card", count)
        return
    else:
        print("total:", sum)
        return
#-------------------------#
# Question 3: Merging Lists
def merge_lists(list_a, list_b):
    new_list = []
    i = 0
    j = 0
    while(i < len(list_a) and j < len(list_b)):
        if(list_a[i] < list_b[j]):
            new_list += [list_a[i]]
            i += 1
        else:
            new_list += [list_b[j]]
            j += 1

    if(i != len(list_a)):
        for k in range(i, len(list_a)):
            new_list += [list_a[k]]
    else:
        for k in range(j, len(list_b)):
            new_list += [list_b[k]]
    print(new_list)
    return new_list
#-------------------------#
# Question 4: Lists of Instructions
def sum_indices(index, list_a):
    sum = 0
    for i in range(0, len(index)):
        if(index[i] > len(list_a) - 1 or index[i] < 0):
            print("Index", i, "caused an error")
            return 0
        else:
            sum += list_a[index[i]]
    print(sum)
    return sum
#-------------------------#
# Extra Credit Question:
def windowed_averages(n, list_a):
    window = 2 * n
    size = window + 1
    window_avg = []
    if(n > 0.5 * len(list_a) or n < 0 ):
        print("invalid window")
        return []
    for i in range(0, (len(list_a) - window)):
        avg = 0
        total = []
        for i in range(i, i+size):
            total += [list_a[i]]
        for k in range(0, len(total)):
            avg += total[k]
        avg /= size
        window_avg += [avg]
    print(window_avg)
# TO DO:
def main():
    a = [1, 2, 3, 4, 5]
    b = [5, 4, 3, 2, 1]
    print("Question 1: List Utilities")
    copy_list(a)
    reverse_list(a)
    modify_list(1, a)
    combine_lists(a,b)
    print(" ")
    print("Question 2: Blackjack")
    blackjack([1, 2, 10, 3, 5])
    blackjack([6, 4, 10, 10, 3])
    blackjack([])
    blackjack([1, 2, 12, 4])
    print(" ")
    print("Question 3: Merge Lists")
    merge_lists([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
    merge_lists([1, 3], [2])
    merge_lists([-10, 6, 12], [-4, 0, 0, 4])
    merge_lists([2, 4, 8, 8, 10], [5, 6, 8, 10, 11])
    print(" ")
    print("Question 4: List of Instructions")
    sum_indices([1, 0, 3, 1], [1.0, 2.0, -3.0, 4.0])
    sum_indices([2, 2, 1], [3.4, 5.6, 7.0])
    sum_indices([], [3.0, 1.0, -4.0])
    sum_indices([3, 2, 5], [4.2, 5.6, 3.1, 3.0])
    print(" ")
    print("Extra Credit:")
    windowed_averages(1, [4.6,6.4,1.0,-8.0,-7.7])
    windowed_averages(0, [])
    windowed_averages(1, [])
    windowed_averages(3, [1,2,3,4,5,6,7,8])
if __name__ == "__main__":
    main()