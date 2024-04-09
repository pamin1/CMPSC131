ALL_TYPES = ["A", "E", "DD", "KC", "X", "F"]
"""All of the assignment types."""

MAX_TYPES = [7, 4, 10, 10, 2, 1]

def get_weights(scores):
    scale = 0.0
    weights = [0.14, 0.16, 0.15, 0.05, 0.25, 0.25]

    # Detect which weights should be zeroed out
    for i in range(len(weights)):
        if scores[i] >= 0.0:
            # Keep a total for scaling
            scale += weights[i]
        else:
            weights[i] = 0.0

    # Scale the weights
    if scale > 0.0:
        for i in range(len(weights)):
            weights[i] /= scale

    return weights

def display_data(score, scores):

    TITLES = [
        "Assignments      : ",
        "Exercises        : ",
        "Design Documents : ",
        "Knowledge Checks : ",
        "Exams            : ",
        "Final            : ",
    ]

    # Display each section in the order of `ALL_TYPES`
    for i in range(len(TITLES)):
        print(TITLES[i], end="")

        value = scores[i] * 100.0
        if value < 0.0:
            print("\tNo data")

        else:
            print(
                letter_grade(value),
                "\t",
                round_one(value),
                "%",
                sep="",
            )

    # Display the final entry
    value = score * 100.0
    print(
        "\nOverall          : ",
        letter_grade(value),
        "\t",
        round_one(value),
        "%",
        sep="",
    )

def round_one(value):
    ones = value // 1
    tenths = (value % 1) // 0.1 / 10
    hundreths = value % .1
    if(hundreths >= 0.05):
        tenths += 0.1
        value = ones + tenths
    else:
        value = ones + tenths
    return value  

def letter_grade(value):
    if(value >= 94):
        letter = "A"
    elif(value >= 90):
        letter = "A-"
    elif(value >= 87):
        letter = "B+"
    elif(value >= 84):
        letter = "B"
    elif(value >= 80):
        letter = "B-"
    elif(value >= 77):
        letter = "C+"
    elif(value >= 70):
        letter = "C"
    elif(value >= 60):
        letter = "D"
    else:
        letter = "F"

    return letter

def drop_lowest(lst):
    new_list = []
    l_index = 0
    if(lst == []):
        return []
    low = lst[0]
    for i in range (0, len(lst) - 1):
        if (low > lst[i+1]):
            low = lst[i+1]
            l_index = i + 1
    for k in range (0, len(lst)):
        if(k != l_index):
            new_list += [lst[k]]
    return new_list

def points_to_percents(name, names, earned, listed):
    list_perce = []
    if(len(names) != len(earned) != len(listed)):
        print("error")
        return
    for i in range(len(names)):
        if(names[i] == name):
            list_perce += [earned[i]/listed[i]]
    return list_perce

def unweighted_score(scores, length):
    sum = 0
    while len(scores) > length:
        scores = drop_lowest(scores)
    for i in range(len(scores)):
        sum += scores[i]
    if(len(scores) < length):
        avg = sum / (i + 1)
    else:
        avg = sum / length
    return avg

def weighted_score(scores):
    w_score = 0
    weights = get_weights(scores)
    for i in range(len(scores)):
        w_score += scores[i] * weights[i]
    return w_score

def get_grades(types, earned, listed):
    scores = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    for i in range(len(ALL_TYPES)):
        percents = []
        percents += points_to_percents(ALL_TYPES[i], types, earned, listed)

        if len(percents) == 0:
            scores[i] = -1.0
        else:
            scores[i] = unweighted_score(percents, MAX_TYPES[i])
    display_data(weighted_score(scores), scores)

def main():
    types = ["A", "A", "A", "A" 
             "E", 
             "DD", "DD", "DD", "DD", "DD",
             "KC", "KC", "KC", "KC", "KC", "KC", "KC", "KC", 
             "X"]
    earned = [10, 12, 10, 10, 
              20,
              20, 20, 20, 20, 20,
              10, 10, 10, 10, 10, 10, 10, 6, 
              70]
    listed = [10, 10, 10, 10, 
              20,
              20, 20, 20, 20, 20, 
              10, 10, 10, 10, 10, 10, 10, 10,
              100]
    get_grades(types, earned, listed)

if __name__ == "__main__":
    main()