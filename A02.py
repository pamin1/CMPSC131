# Question 1:
def greatest_of_four(number1, number2, number3, number4):
    if(number1 > number2):
        greatest_num = number1
    else:
        greatest_num = number2

    if(greatest_num < number3):
        greatest_num = number3

    if(greatest_num < number4):
        greatest_num = number4

    print(greatest_num)
    return(greatest_num)
#-----------------------------------------#
# Question 2:    
def collision_equation(vol_a, vol_b, distance):     # Serparate algorithm to calculate crash time
    time = distance / (vol_a - vol_b)
    time *= 1000 / 60
    return time

def determine_crash(vol_a, vol_b, distance):
    vol_temp = vol_a - vol_b
    if(vol_temp <= 0):                          
        print("Trains are fine")        # Conditional determined from the collision_equation, note at end of function
    else:
        print("Trains will crash in",
              collision_equation(vol_a, vol_b, distance),
              "minutes")
#-----------------------------------------#       
''' Crash condition determined from collision_equation, 
    where time must be (+) for a crash to occur,
    and time will only be (+) for a-b > 0'''
#-----------------------------------------#
# Question 3:
def clamping_algorithm(category):       # Effective clamping to return per category input
    if(category > 1):
        return 1
    elif(category < 0):
        return 0
    else:
        return category

def letter_grade(dec_grade):
    if(dec_grade > 1):
        print("I")        # Series of top-down if cases to check for highest grade possible
    elif(dec_grade >= 0.94):
        print("A")
    elif(dec_grade >= 0.90):
        print("A-")
    elif(dec_grade >= .87):
        print("B+")
    elif(dec_grade >= 0.84):
        print("B")
    elif(dec_grade >= 0.80):
        print("B-")
    elif(dec_grade >= 0.77):
        print("C+")
    elif(dec_grade >= 0.70):
        print("C")
    elif(dec_grade >= 0.60):
        print("D")
    elif(dec_grade >= 0):
        print("F")
    else:
        print("I")

def final_percentage(assignments, exercises, DD, KC, exams, final):
        # Clamp and Weigh the respective category percentage
    assignments = clamping_algorithm(assignments) * .14
    exercises = clamping_algorithm(exercises) * .16
    DD = clamping_algorithm(DD) * .15
    KC = clamping_algorithm(KC) * .05
    exams = clamping_algorithm(exams) * .25
    final = clamping_algorithm(final) * .25
        # Take the sum of the weighted percentages
    dec_grade = assignments + exercises + DD + KC + exams + final
    perc_grade = dec_grade * 100.0
        # Computations complete and ready to print
    print(perc_grade, end='')
    print("%")
    return dec_grade
#-----------------------------------------#
def main():
    greatest_of_four(-410.5056384176101, 489.16701522293965, -52.36985748485937, 17.75475518679614)
    greatest_of_four(0, 0, 0, 0)
    greatest_of_four(3, 5, 4, 1)
    print(end='\n')

    determine_crash( 0, 0, 0.1)
    determine_crash( 0, 1, 0.1)
    determine_crash(-1, 0, 0.1)
    determine_crash( 0.0023462379054817184, 2.561567005239391, 1.1463859542117572)
    print(end='\n')

    final_percentage(1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
    final_percentage(0.5, 0.5, 0.5, 0.5, 1.0, 1.0)
    final_percentage(1.0, 1.0, 1.0, 1.0, 0.5, 0.0)
    final_percentage(0.6, 0.73, 0.2, 99.9, .85, 2.0)
    print(end='\n')

    
    letter_grade(0.9333)
    letter_grade(0.94)
    letter_grade(.59)
#-----------------------------------------#   
if __name__ == "__main__":
    main()