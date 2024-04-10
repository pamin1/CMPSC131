SUIT = ["C", "D", "H", "S"]
CARDS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
VALUES = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]


def indiv_cardcheck(card):
    cond_1 = False # This will check the suit of the card
    cond_2 = False # This will check the values of the card

    for i in range(len(SUIT)):
        if card[0] == SUIT[i]:
            cond_1 = True

    for k in range(len(CARDS)):
        if card[1] == CARDS[k]:
            cond_2 = True

    # Finally check if the conditions are met
    if cond_1 and cond_2:
        return True
    else:
        print("Bad Hand")
        return False   

def card_converter(val):
    """
    First initialize the index such that we can keep track of the
    index corresponding to the card value.
    Next we can wrap the char to be a card_listing in order to check against
    a card_listing.
    The character will correspond to a single card_listing in CARDS, 
    the index value will track to the VALUES list,
    Now we can return the corresponding VALUES item
    """
    index = 0
    for i in range(len(CARDS)):
        if (val) == CARDS[i]:
            index = i
    return VALUES[index]

def card_chunker(card_list):
    """
    Initialize a sum variable to track the value of the hand,
               a list to track the list prior to breaking the hand,
               a total list to include all chunked hands.
    Looping through the card_list we can see call card_converter
    to receive an int value, which we add to the sum

    If the sum does not break the pot, we move on to the next hand,
    If the sum does break the pot, we conclude that hand by adding to
    tot_list, then reset the hand_list, and add the current card
    so that the card that breaks the hand starts a new list
    """
    sum = 0
    hand_list = []
    tot_list = []


    for i in range(len(card_list)):
        let_val = card_list[i][1]
        int_val = card_converter(let_val)
        sum += int_val

        if sum <= 21:
            hand_list += [card_list[i]]
        else:
            sum = 0
            tot_list += [hand_list]

            hand_list = []
            sum += int_val
            hand_list += [card_list[i]]


    if len(hand_list) != 0:
        tot_list += [hand_list]


    return tot_list       

def double_checker(card_list):
    seen = []
    duplicates = []

    for i in range(len(card_list)):
        """
        Check if card_list value has been seen before
        Also create conditions for checking repeats of 1 being A
        """
        
        found = False
        for j in range(len(seen)):
            cond1 = card_list[i][1] == 'A' and seen[j][1] == '1'
            cond2 = card_list[i][0] == seen[j][0]
            if card_list[i] == seen[j] or (cond1 and cond2):
                found = True

        """
        In the event there is a repeated value,
        we can check it against a secondary list
        containing all repeated values.
        If the value has not been seen in the 
        list of known duplicates it is added;
        thus double counting of duplicates is removed
        """

        if found == True:
            dup_found = False
            for k in range(len(duplicates)):
                if card_list[i] == duplicates[k]:
                    dup_found = True
                    
            if dup_found == False:
                duplicates += [card_list[i]]
        else:
            seen += [card_list[i]]

    # Output only the duplicate list
    return duplicates

def blackjack_checker(card_list):
    # Loop through the list and check for bad hands via indiv_cardcheck
    for i in range(len(card_list)):
        if (indiv_cardcheck(card_list[i])) == False:
            return []
    # Call necessary functions and return the list of them    
    out1 = card_chunker(card_list)
    out2 = double_checker(card_list)
    
    return [out1, out2]
            

def main():
    print(blackjack_checker(["HT", "DT", "DT", "S2", "S1", "C5"]))
    
if __name__ == "__main__":
    main()
