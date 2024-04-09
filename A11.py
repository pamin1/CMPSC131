# Question 1: collatz_chain and collatz_depth
def chain_helper(val: int, sum: int, out: list[int]):
    sum += val
    out.append(val)

    # Base Case:
    if val == 1:
        for i in range(len(out)):
            print(out[i], end=" ")
        print()
        return sum
    
    # Recursive Steps:
    if val % 2 == 0:
        val //= 2
        return chain_helper(val, sum, out)
        
    else:
        val *= 3
        val += 1
        return chain_helper(val, sum, out)

def collatz_chain(val: int):
    sum: int = 0
    out: list = []
    # Check Validity:
    if val <= 0:
        print("Invalid Input")
        return -1
    
    return(chain_helper(val, sum, out))

def depth_helper(val: int, sum: int, out: list[int], count: int):
    sum += val

    if val % 2 != 0:
        out.append(val)
    
    # Base Case:
    if val == 1:
        for i in range(len(out)):
            print(out[i], end=" ")
        print()
        print("Skipped", count, "even numbers")
        return sum
    
    # Recursive Steps:
    if val % 2 == 0:
        count += 1
        val //= 2
        return depth_helper(val, sum, out, count)
        
    else:
        val *= 3
        val += 1
        return depth_helper(val, sum, out, count)

def collatz_depth(val: int):
    sum: int = 0
    out: list = []
    count: int = 0
    # Check Validity:
    if val <= 0:
        print("Invalid Input")
        return -1
    
    return depth_helper(val, sum, out, count)

# List Splicer for Q2 and Q3:
def list_split(lst, mid, side):
    out_lst = []
    if side == "l":
        for i in range(0, mid):
            out_lst.append(lst[i])
    elif side == "r":
        for j in range(mid, len(lst)):
            out_lst.append(lst[j])
    return out_lst
    
# Question 2: binary_search
def binary_search(list, val):
    if len(list) == 0:
        return -1
    b_low = 0
    b_high = len(list) - 1
    
    mid = (b_high - b_low) // 2
    if len(list) <= 2:
        if list[0] == val:
            return 0
        
        elif len(list) == 2 and list[1] == val:
            return 1
        else:
            return -1
        
    if list[mid] == val:
        return mid
    
    if list[mid] < val:
        list = list_split(list, mid, "r")
        if binary_search(list, val) == -1:
            return -1
        else: 
           
            return mid + binary_search(list,val)
    
    elif list[mid] > val:
        list = list_split(list, mid, "l")
        if binary_search(list, val) == -1:
            return -1
        else: 
            return binary_search(list, val)

# Question 3: merge_sort
def merge_sort(lst: list):
    # base case:
    if len(lst) > 1:
        mid = len(lst) // 2
        l = list_split(lst, mid, "l")
        r = list_split(lst, mid, "r")

        merge_sort(l)
        merge_sort(r)


        l_count = 0
        r_count = 0
        m_count = 0

        while l_count < len(l) and r_count < len(r):
            if l[l_count] < r[r_count]:
                lst[m_count] = l[l_count]
                l_count += 1
            else:
                lst[m_count] = r[r_count]
                r_count += 1
            m_count += 1
        while l_count < len(l):
            lst[m_count] = l[l_count]
            l_count += 1
            m_count += 1

        while r_count < len(r):
            lst[m_count] = r[r_count]
            r_count += 1
            m_count += 1

    return lst
        
def main():
    print(merge_sort([2,4,3,5,6]))

if __name__ == "__main__":
    main()