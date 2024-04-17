# Question 1: A Better Frquency:
def frequency_analysis(str):
    seen = []
    freq = []
    
    for i in range(len(str)):
        found = False
        for j in range(len(seen)):
                if str[i] == seen[j]:
                    freq[j] += 1
                    found = True
        if found == False:
            seen += [str[i]]
            freq += [1]

    return [seen,
            freq]

# Question 2: Aux Functions:
def forward_sort(lst):
    length = len(lst)
    for i in range(length - 1):
        if lst[i] > lst[i + 1]:
            temp = lst[i + 1]
            lst[i + 1] = lst[i]
            lst[i] = temp
    return lst

def reverse_sort(lst):
    length = len(lst)
    for i in range(length - 1, 0, -1):
        if lst[i] < lst[i - 1]:
            temp = lst[i - 1]
            lst[i - 1] = lst[i]
            lst[i] = temp
    return lst

# Question 2.1: Bubble Sort
def bubble_sort(lst):
    length = len(lst)
    for i in range(length):
        forward_sort(lst)
    return lst

# Question 2.2: Shaker Sort
def shaker_sort(lst):
    length = len(lst)
    for i in range(length):
        forward_sort(lst)
        reverse_sort(lst)
    return lst

# Question 3: Sorted Frequency List
def sorted_frequencies(str):
    [chars, freq] = frequency_analysis(str)
    length = len(freq)
    for k in range(length):
        for i in range(length - 1):
            if freq[i] > freq[i + 1]:
                temp = freq[i + 1]
                freq[i + 1] = freq[i]
                freq[i] = temp

                char_temp = chars[i + 1]
                chars[i + 1] = chars[i]
                chars[i] = char_temp

    return [chars, freq]
    

def main():
    print(frequency_analysis("Hello World!"))
    print(frequency_analysis("CMPSC-131"))
    print(frequency_analysis("Spring is near"))
    print(frequency_analysis(["D2", "CT", "HK", "D9", "SK"]))
    
    print(forward_sort([5,4]))
    print(shaker_sort([7,3,9,2,1]))

    print(sorted_frequencies("Hello World!"))
    print(sorted_frequencies("CMPSC-131"))
    print(sorted_frequencies("Spring is near"))
    print(sorted_frequencies(""))

if __name__ == "__main__":
    main()