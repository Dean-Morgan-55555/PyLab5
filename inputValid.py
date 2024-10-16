#functions to validate that the user has input a number
#will only check a string

#function to validate that a user inputs a number
def inputValidationToInt(validate):
    "number to validate"
    if type(validate) == str:
        while not validate.isdigit():
            validate = input("Please enter a number: ")
        return eval(validate)
    else:
        raise Exception("Please input a string")


#overloads function to check that the user inputs a int and that it is between two values
def inputValidationToIntMinMax(validate,minNum, maxNum):
    "number to validate, minimum value inclusive, maximum value inclusive"
    if type(validate) == str and type(maxNum) == int and type(minNum) == int:
        validate = inputValidationToInt(validate)
        while not(validate >= minNum and validate <= maxNum):
            validate = input("please enter a number between {} and {}: ".format(minNum, maxNum))
            validate = inputValidationToInt(validate)
        return validate
    else:
        raise Exception("Please input valid data types (String, int, int)")

#function to validate input with a min number
def inputValidationToIntMin(validate,minNum):
    "number to validate, minimum number inclusive"
    if type(validate) == str and type(minNum) == int:
        validate = inputValidationToInt(validate)
        while not(validate >= minNum):
            validate = input("please enter a number greater than or equal to {}: ".format(minNum))
            validate = inputValidationToInt(validate)
        return validate
    else:
        raise Exception("Please input valid data types (String, int, int)")

#function to validate that a number enterd is a num that is less than another num
def inputValidationToIntMax(validate, maxNum):
    "number to validate, maximum number inclusive"
    if type(validate) == str and type( maxNum) == int:
        validate = inputValidationToInt(validate)
        while not(validate <=  maxNum):
            validate = input("please enter a number less than or equal to {}: ".format( maxNum))
            validate = inputValidationToInt(validate)
        return validate
    else:
        raise Exception("Please input valid data types (String, int, int)")
