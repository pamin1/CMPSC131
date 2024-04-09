def fmos(val, c_class, count, const, lst):
    """
    val = class representative;
    c_class = congruence class;
    count = counter for FMO;
    const = val; meant to exponentiate val
    lst = list of all representatives
    """
    # add val to a lst to keep track of representatives
    # iterate a counting variable to keep track of the order
    lst += [val]
    count += 1

    # recursive base case to check if class = 1 at current order;
    # prints/returns order and classes if True
    if val == 1:
        print("Finite Multiplicative Order:\t", count)
        print("List of Representatives Found:\t", lst)
        return count, lst
    
    # otherwise, we must exponentiate the value;
    # we do so via const, which is = to value
    val *= const

    # before we recurse we need to make sure the representative 
    # is less than the congruence class by taking the remainder of the 
    # val when divided by the congruence class
    # recurse at this stage as we have not reached the FMO
    if val > c_class:
        val %= c_class
        return fmos(val, c_class, count, const, lst)
    else:
        return fmos(val, c_class, count, const, lst)
    
            
def main():
    x = str([1,2,3,4])
    print(x)

if __name__ == "__main__":
    main()