def greetings(names):
    if(len(names) == 0):
        print("no names to greet")
        return
    
    for i in range(len(names)):
        print("Hello, ", names[i], "!", sep='')
    return

def summation(nums):
    sum = 0
    if(len(nums) == 0):
        print("error")
    for i in range(len(nums)):
        sum += nums[i]
        print(sum)

def seperator(char, string):
    if(len(string) > 0):
        print(string[0], end="")
        for i in range(1, len(string)):
            print(char, string[i], sep='', end='')
    print("")

def trim(nums):
    new_nums = []
    if(len(nums) > 0):
        for i in range (1, len(nums) - 1):
            new_nums += [nums[i]]
        print(new_nums)
    else:
        print("error")
        return []
    
def names_scores(names, scores):
    if len(names) != len(scores):
        print("invalid sets")
        return -1
    for i in range(len(names)):
        if(scores[i] >=0 and scores[i] <= 1):
            score = scores[i] * 100
            name = names[i]
            print(name, " got a ", score, "%", sep='')
        else:
            print("invalid input")

def adjancency_sum(ints):
    totals = []
    if(len(ints) == 1):
        print(ints[0])
        return
    for i in range(len(ints)):
        if(i == 0 ):
            totals += [ints[i] + ints[i + 1]]
        elif(i == len(ints) - 1):
            totals += [ints[i] + ints[i - 1]]
        else:
            totals += [ints[i] + ints[i - 1] + ints[i + 1]]
    print(totals)

def detector(int):
    sum = 0
    for i in range(int - 1, 0, -1):
        if(int % i == 0):
            sum += i
    if sum == int:
        return True
    else:
        return False
    
def main():
    greetings(["Alex", "Beth", "Carol"])
    summation([])
    seperator("-", [])
    trim([1,2,3,4])
    names_scores(["Alex", "Beth", "Carol"], [0.95, 0.97, 1.1])
    adjancency_sum([])
    print(detector(6))

if __name__ == "__main__":
    main()