def in_list(n, l1):
    for i in l1:
        if(n == i):
            return True
    return False

def filter_list(l1, l2):
    filtered = []
    for i in range(0, len(l2)):
        for j in range(0, len(l1)):
            if(l1[j] != l2[i]):
                holder = l2[i]
                print(holder)
        filtered += [holder]
    print(filtered)

def age_gate(ages, names):
    gate = []
    if(len(ages) < len(names)):
        limit = len(ages)
    else:
        limit = len(names)
    for i in range(0, limit):
        if(ages[i] >= 18.0):
            gate += [names[i]]
    print(gate)   
def main():
    age_gate([17, 18.1, 19], ["a", "b", "c", "d"])
if __name__ == "__main__":
    main()
