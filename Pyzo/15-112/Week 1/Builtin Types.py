import math
def f():
    print("This is a user-defined function")
    return 42

print("Some basic types in Python:")
print(type(2))           # int
print(type(2.2))         # float
print(type("2.2"))       # str  (string)
print(type(2 < 2.2))     # bool (boolean)
print(type(math))        # module
print(type(math.tan))    # builtin_function_or_method
print(type(f))           # function (user-defined function)
print(type(type(42)))    # type

print("#####################################################")

print("And some other types we will see later in the course...")
print(type(Exception())) # Exception
print(type(range(5)))    # range
print(type([1,2,3]))     # list
print(type((1,2,3)))     # tuple
print(type({1,2}))       # set
print(type({1:42}))      # dict (dictionary or map)
print(type(2+3j))        # complex  (complex number)

print("Type conversion functions:")
print(bool(0))   # convert to boolean (True or False)
print(float(42)) # convert to a floating point number
print(int(2.8))  # convert to an integer (int)

print("And some basic math functions:")
print(abs(-5))   # absolute value
print(max(2,3))  # return the max value
print(min(2,3))  # return the min value
print(pow(2,3))  # raise to the given power (pow(x,y) == x**y)
print(round(2.354, 1)) # round with the given number of digits



print("The / operator does 'normal' float division:")
print(" 5/3  =", ( 5/3))
print()
print("The // operator does integer division:")
print(" 5//3 =", ( 5//3))
print(" 2//3 =", ( 2//3))
print("-1//3 =", (-1//3))
print("-4//3 =", (-4//3))



print(type("abc") == str)
print(isinstance("abc", str))

import numbers
def isNumber(x):
    return isinstance(x, numbers.Number) # works for any kind of number
print(isNumber(1), isNumber(1.1), isNumber(1+2j), isNumber("wow"))