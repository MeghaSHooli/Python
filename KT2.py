"""
Demonstration of basics of Python to Def Funcations

"""
# Created by: mhooli
# Version -V0.1

#Basic of Def Funcations

def sayhello():
    """ print hello """
    print("hello")
#end of fun
sayhello()  # Call the funcation

def double(value):
    """
    Return twice the input value
    """
    return value * 2

# Call the function and assign the result to a variable
result = double(6)
print(result)

def product(value1, value2, value3):
    """
    Returns the product of the three input values.
    """
    prod = value1 * value3
    prod = prod * value2
    return prod

# Call the function and assign the result to a variable
result = product(7, 44, -55)
print(result)

#Boolean Logic

value1 = True
value2 = True

print(not value1)

print(value2 and value1)
print(value2 or value1)
# Six different arithmetic comparison operators
print("Comparisons")
print("===========")
print(7 > 3)
print(7 < 3)
print(7 >= 3)
print(7 <= 3)
print(7 == 3)
print(7 != 3)

print("")

# Using comparisons to get a boolean value
print("Comparing Variables")
print("===================")
num1 = 7.3
num2 = 8.6

greater = num1 > num2
print(greater)

print("")

# == and != are also useful for non-numeric types
print("Comparing Strings")
print("=================")
name = 'Scott'


# Beware of = and == confusion!
equal = name != "Joe"
print(equal)



