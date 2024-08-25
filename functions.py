# Defining a function
def welcome(name):
    print("Welcome {}".format(name))
    
print(welcome('Deepak'))
welcome('Rahul')

# defining a function with default value
def welcome(name = 'there'):
    print("Welcome {}".format(name))
    
welcome()
welcome('Deepak')

# function with Doc String
def add(num1, num2):
    """This function adds two values."""
    return num1 + num2

add(5, 2)
help(add)


# Example
def odd_or_even(num):
    """This function determines if a number is odd or even."""
    if num % 2 == 0:
        return 'Even'
    else:
        return 'Odd'
    
print(odd_or_even(5))
print(odd_or_even(16))

