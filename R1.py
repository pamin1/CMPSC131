def min_of_two(number1, number2):
    if(number1 < number2):
        return number1
    else:
        return number2
    
def min_of_three(num1, num2, num3):
    if(num1 < num2):            # Take smallest of the first two numbers
        first_minimum = num1
    else:
        first_minimum = num2
    
    if(first_minimum < num3):   # Take the smallest of the first two and now the third as well
        return first_minimum
    else:
        return num3

def long_div(num1, num2):
    if(num2 == 0):
        print(num1, "by", num2, "produces a divide by 0 error")
        return
    else:
        quotient = num1 // num2     # // --> produces integer quotient
        remainder = num1 % num2     # %  --> produces integer remainder
        print(num1, "by", num2, "is equal to", quotient, "r", remainder)


def goldilocks_conds(temp):
    if(temp >= 100):
        print("way too hot")
        
    elif(temp >= 60):
        print("too hot")
        
    elif(temp >= 21):
        print("just right")
        
    elif(temp >= 5):
        print("too cold")
        
    else:
        print("way too cold")
        
    

def main():
    print(min_of_two(3,3),
          min_of_two(1,-1),
          min_of_two(0,3))
    
    print(min_of_three(-1,0,1),
          min_of_three(2,1,3),
          min_of_three(-10,-9,-11))
    
    long_div(3,2)
    long_div(0,2)
    long_div(79, 0)
    
    goldilocks_conds(20.9999999)
    goldilocks_conds(0)
    goldilocks_conds(100)

if __name__ == "__main__":
    main()
