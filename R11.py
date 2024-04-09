def rc_sum(lst: list):
    rows: list = []
    cols: list = []

    for l in range(len(lst)):
        rows.append(0)
    for w in range(len(lst[0])):
        cols.append(0)

    for i in range(len(lst)):
        row = lst[i]
        for j in range(len(row)):
            cols[j] += row[j]
            rows[i] += row[j]
            
    return [rows, cols]
    
def main():
    lst = [
        [1,2,3],
        [4,5,6]
    ]
    print(rc_sum(lst))

if __name__ == "__main__":
    main()