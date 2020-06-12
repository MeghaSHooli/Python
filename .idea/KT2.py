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

