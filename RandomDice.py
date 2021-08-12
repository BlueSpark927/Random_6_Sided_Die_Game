#import module RANDOM
import random

print("6 sided dice game")

#sets the minimum and the maximum for the six sided die
min_value = 1
max_value = 6

#starts variable with yes
ROLL = "yes"

#while loop
while ROLL == "yes" or "Yes" or "YES":
    print("Rolling The Dices...")
    print("The Values are :")
    
    #generating a random number from 1 to 6 and then prints it
    print(random.randint(min_value, max_value))
    
    #Generate the loop again
    ROLL = input("Roll the Dices Again? (type yes)") 
