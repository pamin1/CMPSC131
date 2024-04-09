def jagged_sum(nums: list[list[int]]):
    out: list = []
    row_max: int = 0
    for k in range(len(nums)):
        if len(nums[k]) > row_max:
            row_max = len(nums[k])
    for w in range(row_max):
        out.append(0)
    for i in range(len(nums)):
        row = nums[i]
        for j in range(len(row)):
            out[j] += row[j]
    return out

def count_substrings(s1, s2):
    if len(s1) < len(s2):
        return 0
    count: int = 0
    for i in range(len(s1) - len(s2) + 1):
        temp: str = "" 
        for j in range(len(s2)):
            temp += s1[i + j]
        if temp == s2:
            count += 1
    return count

def get_name(input):
    if isinstance(input, str) == True:
        print("is string")
    elif isinstance(input, int) == True:
        print("is integer")
    elif isinstance(input, float) == True:
        print("is float")
    elif isinstance(input, list) == True:
        print("is list")

def d_fact(num: int) -> int:
    # tail recursive function...
    # base case:
    if num == 1 or num == 2:
        return num
    temp = num - 2
    if num % 2 == 0:
        return num * d_fact(temp)

    return num * d_fact(temp)

def d_fact_list(lst: list[int]):
    if len(lst) <= 1: 
        return 0
    val = []
    mem = {}
    for i in range(len(lst)):
        val.append(d_fact_list_help(lst[i], mem))
    return val

def d_fact_list_help(num, mem):
    if num < 1:
        return 1
    prev = mem.get(num, None)
    if isinstance(prev, int):
        return prev
    
    mem[num] = d_fact_list_help(num-2, mem) * num
    return mem[num]

def pow_base(base: int, num: int) -> bool:
    if num == 0:
        return False
    if num == 1:
        return True
    if num % base != 0:
        return False
    num //= base
    return pow_base(base, num)
    
def flat(a_list: list[list[int]]) -> list[int]:
    lst_out: list[int] = []

    if len(a_list) == 0:
        return a_list
    
    if isinstance(a_list[0], int):
        lst_out += [a_list[0]]
        lst_out += flat(a_list[1:])

        return lst_out
    elif isinstance(a_list[0], list):
        lst_out += flat(a_list[0])
        lst_out += flat(a_list[1:])
        return lst_out

def fib(num: int):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    elif num == 2:
        return 2
    else:
        return fib(num-1) + fib(num-2)

def fib_dict(num: int, mem: dict[int, int]):
    if mem.get(num, None) != None:
        return mem[num]
    elif num == 0:
        mem[0] = 0
        return 0
    elif num == 1:
        mem[1] = 1
        return 1
    elif num == 2:
        mem[2] = 2
        return 2
    else:
        sum = fib_dict(num - 2, mem) + fib_dict(num - 1, mem)
        mem[num] = sum
        return sum


def main():
    print(fib(8))

if __name__ == "__main__":
    main()