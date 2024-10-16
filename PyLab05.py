# -*- coding: utf-8 -*-
"""

  Program: CSC115/170 Lab 05
 ----------------------------
  Partner 1:  Dean Morgan
  Partner 2: Chris Bayer
  Date: 10/11/2024
      
      
  **To get full credit:**
        * The code must run without errors
        * You must check for valid swallows and numbers
        * Your code must implement the four functions listed with correct arguments and return values
        * The code must calculate the carry weight, number of coconuts and number of swallows correctly
        * The code will continue running until the user chooses to end (while loop)
        * You must comment your code well
        * You must work as a group
        * You must turn the lab in on time

  
      
      
"""
# Put any import statements here
import inputValid

#Dean Morgan
#done and tested
# ###########################################################
# get_swallows() function header
# - arguments: none
# - returns: swallow type and swallow number
# ###########################################################
def get_swallows():
    """
    Gets input from the user for a type of swallow in the list bellow and a number of swallows.
    ensures that the number of swallows is above 0
    type_list = ["african", "cliff", "european", "fanti", "mosque", "tree", "welome"]
    """
    type_list = ["african", "cliff", "european", "fanti", "mosque", "tree", "welome"]
    sw_type = input("Enter a swallow type: ").lower()
    while not sw_type in type_list:
        sw_type = input("\tUnknown type \'{}\'. Enter a different type: ".format(sw_type).lower())
    sw_num = inputValid.inputValidationToIntMin(input("Enter number of {} swallows: ".format(sw_type)), 1)
    return sw_type, sw_num


#Chris Bayer
# ###########################################################
# carry_weight( sw_type, num ) function header
# - parameters: swallow type and number
# - returns: carry weight in grams
# ###########################################################
def carry_weight(sw_type, num):
    return 0



#Dean Morgan
# ###########################################################
# num_coconuts( weight, avg_coconut ) function header
# - parameters: carry load, weight of 1 coconut in grams
# - returns: fraction of coconuts that can be carried
# ###########################################################
def num_coconuts(weight, avg_coconut):
    coconut_percent = weight/avg_coconut
    return coconut_percent



#Chris Bayer
# ###########################################################
# num_swallows ( sw_type, avg_coconut ) function header
# - parameters: type of swallow and weight of 1 coconut in grams
# - returns: the number of swallows needed
# ###########################################################
def num_swallows(sw_type, avg_coconut):
    return 0



#Dean Morgan
# ###########################################################
# main code while loop
# ###########################################################
print("Swallow Payoad Calculator")
print("-"*40, "\n")
done = False
coconut_weight = 1
while not done:
    sw_type, sw_num = get_swallows()
    print("\nResults for {} {} swallows \n".format(sw_num, sw_type))
    sw_weight = carry_weight(sw_type, sw_num)
    carry_percent = num_coconuts(sw_weight, coconut_weight)
    print("{} {} swallows can carry {:.1f}g which is {:.3f} {}lb coconuts\n".format(sw_num, sw_type, sw_weight, carry_percent, coconut_weight))
    carry_swallow = num_swallows(sw_type, coconut_weight)
    print("to carry a {}lb coconut you will need {} {} swallows\n".format(coconut_weight, carry_swallow, sw_type))
    usrInput = input("Would you like to try another swallow (y/n)? ")
    usrInput = usrInput.lower()
    if  usrInput == 'y':
        print("Sounds good. Hold onto your swallows.\n\n")

    done = True



#tests
#sw_type, sw_num = get_swallows()
#print(num_coconuts(1, 0.5))


