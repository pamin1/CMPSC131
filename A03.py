#---------------------------#
# Question 1:
def is_prime(integer):
    limit = integer ** 0.5
    i = 2
    if(integer <= 1):
        return False
    while(i <= limit):
        if(integer % i == 0):
            return False
        i += 1
    return True
#---------------------------#
# Question 2:
def collatz_chain(integer):
    if (integer < 1):
        print("invalid input")
        return -1
    print(integer, end=' ')
    sum = integer
    while(integer != 1):
        if(integer % 2 == 0):
            integer //= 2
        else:
            integer *= 3
            integer += 1
        print(integer, end=' ')
        sum += integer        
    print("")
    return sum

def collatz_chain_skips(integer):
    if (integer < 1):
        print("invalid input")
        return -1
    if(integer % 2 == 0):
        sum = 0
    else:
        print(integer, end=' ')
        sum = integer
    while(integer != 1):
        if(integer % 2 == 0):
            integer //= 2
        else:
            integer *= 3
            integer += 1
        if(integer % 2 != 0):
            print(integer, end=' ')
            sum += integer            
    print("")
    return sum   
#---------------------------#
# Question 3:
def input_check(init_pop, change_rate, carry_capacity):
    if(init_pop % 1 != 0):
        print("Starting population must be a positive, whole number.")
    if(change_rate < 0 or change_rate > 1.0):
        print("Rate of change must be between 0.0 and 1.0, inclusive.")
    if(carry_capacity % 1 != 0):
        print("Carrying capacity must be a positive, whole number.")
    if(init_pop % 1 != 0 or change_rate < 0 or change_rate > 1.0 or carry_capacity % 1 != 0):
        return -1

def rounder(input):
    if(input % 1 < 0.5):
        input //= 1
    else:
        input //= 1
        input += 1
    return input
    
def population_sim(init_pop, change_rate, carry_capacity):
    if(input_check(init_pop, change_rate, carry_capacity) == -1):
        return -1
    count = 1
    population = init_pop
    perc_change = 1
    while(perc_change > 0.01):
        init_pop = population
        pop_change = change_rate * init_pop * (1 - init_pop / carry_capacity)
        population += pop_change
        perc_change = (population - init_pop) / init_pop
        temp_final = rounder(population)
        temp_init = rounder(init_pop)
        print(count, ":", temp_init, "->", temp_final)
        count += 1   
    return init_pop    

def main():
    # print(is_prime(0))
    # print(is_prime(101))
    # print(is_prime(3001))
    # print(is_prime(16))
    # print("")

    # collatz_chain(3)
    # collatz_chain(46)
    # collatz_chain(0)
    # collatz_chain(-1)
    # print("")

    collatz_chain_skips(3)
    collatz_chain_skips(458)
    collatz_chain_skips(729)
    collatz_chain_skips(881)
    print("")
    
    # population_sim(1000.0, 0.05, 5000.0)
    # population_sim(15.5, -3.0, 2.2)
    # population_sim(15.0, -3.0, 2.0)
    # population_sim(50, 0.8, 500)


if __name__ == "__main__":
    main()