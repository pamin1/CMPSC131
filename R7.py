def rc_sum(lst):
    count = 0
    sum_col = 0
    sum_row = 0
    row_sums = []
    col_sums = []

    if len(lst) != 0:
        for i in range(len(lst[0])):
            count += 1

    for i in range(len(lst)):
        sum_col = 0
        for j in range(len(lst)):
            sum_col += lst[j][i]
        col_sums += [sum_col]  

    for i in range(len(lst)):
        sum_row = 0
        for j in range(len(lst[i])):
            sum_row += lst[i][j]
        row_sums += [sum_row]

    print(count, row_sums, col_sums)

def band_aid(lst):
    band_combos = []
    for i in lst[0]:
        for j in lst[1]:
            for k in lst[2]:
                band = [i,j,k]
                band_combos += [band]
    print(band_combos, "\n")

def find_peaks(lst):
    peaks = []
    for i in range (len(lst)):
        for j in range (len(lst)):
            value = lst[i][j]

            has_above = i > 0
            has_below = i < len(lst) - 1
            has_left = j > 0
            has_right = j < len(lst[0]) - 1       

def main():
    # band_aid([
    #     ["A", "B"],
    #     ["C", "D"],
    #     ["E", "F"],
    # ])
    rc_sum([
        [1,2,3],
        [4,5,6]
        ]
    )

if __name__ == "__main__":
    main()