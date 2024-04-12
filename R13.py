def zipper(strs: list[str],
           ints: list[int]) -> list[tuple[str,int]]:
    tup: tuple = ()
    out: list = []
    for i in range(len(strs)):
        for j in range(len(ints)):
            tup = (strs[i], ints[j])
            out.append(tup)
    return out

def file_exists(fn: str) -> bool:
    try: 
        open(fn, "r")
        return True
    except FileNotFoundError:
        return False

def recursive_count(tup: tuple) -> int:
    if len(tup) == 0:
        return 0
    
    count = 0
    for i in range(len(tup)):
        if isinstance(tup[i], tuple):
            count += recursive_count(tup[i])
        else:
            count += 1
    return count

def clean_unpackaging(lst):
    out = []

    for i in range(len(lst)):
        try:
            first, *rest = lst[i]          
            out.append(first)
            out.extend(rest)
        except TypeError:
            out.append(lst[i])
    return out

def cleaner(lst: list) -> list[int]:
    if len(lst) == 0:
        return []

    cleaned = []
    for i in range(len(lst)):
        try:
            sample = int(lst[i])
            cleaned += [sample]
        except TypeError:
            cleaned += cleaner(lst[i])
    return cleaned

def main():
    print(zipper(["a", "b", "c"], [1,2]))
    print(file_exists(""))
    print(recursive_count((1,(((2))),3)))
    print(clean_unpackaging([1,2,(3,4),5]))
    print(cleaner([1,2,((3,),4),5,6,(((7,),),),(8,9),()]))


if __name__ == "__main__":
    main()