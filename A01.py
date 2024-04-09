################################################################################
# 1.) Hello, Me!
# 
# Implement the following:
#   - A variable named 'first' and assign it a literal string containing your first name.
#   - A variable named 'last' and assign it a literal string containing your last name.
#   - Using these two variables print out "Hello first last".
#

# TODO:
first = "Prachit"
last  = "Amin"
print("Hello", first, last)
################################################################################
# 2.) Operator Practice
# 
# Print out the result of each of the following equations:
#   p2_1: 'a' plus 'b' raised to the second power.
#   p2_2: 'b' plus 'c' all modulo by 'x'.
#   p2_3: The sum of 'a', 'b', and 'c' subtracted from 'x' divided by 'y'.
#   p2_4: The remainder (integer division) of x by y.
#   p2_5: The product of all the variables divided by the remainder of ('a' to the 'b' power) by 7.
# 
# Make sure to think of some values to test and make sure that your algorithms work!
# 

# Use these variables to control your algorithms.
a = 1
b = 2
c = 3
x = 5
y = 4
z = 6
# TODO: Your Code Down Below

p2_1 = a + b**2
p2_2 = (b + c) % x
p2_3 = (x - (a + b + c)) / y
p2_4 = x / y - x // y
p2_5 = a * b * c * x * y * z / ((a ** b) % 7)
print("p2_1:", p2_1, "\n" + 
      "p2_2:", p2_2, "\n" + 
      "p2_3:", p2_3, "\n" + 
      "p2_4:", p2_4, "\n" + 
      "p2_5:", p2_5)

################################################################################
# 3.) Bottle Factory
# 
# Implement the algorithm from Problem 3 of the Design Document.
#   For your inputs and outputs, create the following variables:
#       - `b` should be called 'bottlesPerHour'
#       - `r` should be called 'lbOfMaterial'
#       - `t` should be called 'numOfMinutes'
#       - The required ounces of material should be called 'ozOfMaterial'
#       - The produced number of bottles should be called 'numBottles'
#
# After you've implemented the algorithm, make sure that all three tests produce
# the expected outputs.
# 
#Inputs:
bottlesPerHour = 1000
lbOfMaterial = 0.4
numOfMinutes = 2

# TODO: Your Code Here
numBottles = numOfMinutes / 60      # Alter units of time from Minutes to Hours
numBottles *=  bottlesPerHour       # Find the # of bottles in the given time
numBottles = int(numBottles)        # Coerce numBottles to resemble how many bottles would realistically be produced
#                                     (No fractional bottles)
ozOfMaterial = numBottles // 100    # Find the amount of integer sets produced
ozOfMaterial += 1                   # Add 1 case because there will always be a set produced for any time, numOfMinutes
ozOfMaterial *= lbOfMaterial * 16   # Multiply the sets by the lbOfMaterial used per set, then Alter units from Pounds to Ounces 

# These print statements will display your inputs and outputs.
# TODO: When you are ready, uncomment the next two lines.
print("For", bottlesPerHour, "bottles/hr,", lbOfMaterial, "lb/100-bottles, and running for", numOfMinutes, "minutes,")
print("    the factory produces", numBottles, "bottles and consumes", ozOfMaterial, "oz of material")

################################################################################
# 4.) Snowy Lot
# 
# Implement the algorithm from Problem 4 of the Design Document.
#   For your inputs and outputs, create the following variables:
#       - `l` should be called 'lotLengthFt'
#       - `s` should be called 'minutesPerIn'
#       - `t` should be called 'numHoursSnowed'
#       - The total volume of snow should be called 'cubicYdOfSnow'
# 
# Print out the final result with the message "The lot contains cubicYdOfSnow yd^3 of snow"
# 
# After you've implemented your algorithm, make sure to use your tests to verify
# that your algorithm produces the expected results.
# 
# Inputs:
lotLengthFt = 15
minutesPerIn = 5
numHoursSnowed = 3

# TODO: Your Code Here

cubicYdOfSnow = numHoursSnowed * 60 # Convert units of time from Hours to Minutes
cubicYdOfSnow /= minutesPerIn * 12  # Convert the Minutes/in of snow to Minutes/ft of snow, 
#                                     Simulatneously divide by this to get a Total Height of snowfall
cubicYdOfSnow *= lotLengthFt**2     # Multiply the Height of the snow by the Area of the lot, this is Volume in ft^3
cubicYdOfSnow /= 27                 # Convert Volume in ft^3 to yd^3

print("For a square lot length of", lotLengthFt, "feet,", minutesPerIn, "minutes per inch of snow, and snowfall for", numHoursSnowed, "hours,")
print("    the volume of snow in the lot will be", cubicYdOfSnow, "yd^3")