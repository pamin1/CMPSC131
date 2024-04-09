def countdown(start, step):
    if(start <= 0 or step <= 0):
        print("Parameters invalid")
    elif(start < step):
        print(start)
    else:
        for number in range(start, -1, -step):
            print(number,"", end='')

def sum_multiples(num):
    sum = 0
    count = 0
    if(num < 0):
        print("invalid input")

    for i in range(0, num, 1):
        if(i % 3 == 0 and i % 7 == 0):
            sum += i
            count += 1
    print("Sum:", sum)
    print("Count:", count)
    print("")

def sum_multiples_xor(num):
    sum = 0
    count = 0
    if(num < 0):
        print("invalid input")

    for i in range(0, num, 1):
        if(i % 3 == 0 and i % 7 == 0):
            sum += i
            count += 1

    print("Sum:", sum)
    print("Count:", count)

def fizzbuzz(start, end):
    for i in range(start, end + 1, 1):
        if(i % 5 == 0 and i % 3 == 0):
            print("fizzbuzz", end='')
        elif(i % 3 == 0):
            print("fizz", end='')
        elif(i % 5 == 0):
            print("buzz", end='')
        else:
            print(i, end='')
        print(" ", end='')
           
def detector(number):
    sum = 0
    if(number <= 0 ):
        return "Invalid Input"
    
    for i in range(1, number - 1, 1):
        if(number % i == 0):
            sum += i
    if (sum == number):
        return True
    else:
        return False

def main():
    sum_multiples(7)
    sum_multiples(77)
    sum_multiples(250)
    sum_multiples(-10)


    print("")
    
    #sum_multiples_xor(7)
    print("")

    fizzbuzz(3,6)
    print("")

    print(detector(6))
    print(detector(9))
    print(detector(10))
if __name__ == "__main__":
    main()