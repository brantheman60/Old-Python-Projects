# function composition
def f(w):
    return 10*w

def g(x, y):
    return f(3*x) + y

def h(z):
    return f(g(z, f(z+1)))

print(h(1)) # hint: try the "visualize" feature


# helper functions
def onesDigit(n):
    return n%10

def largerOnesDigit(x, y):
    return max(onesDigit(x), onesDigit(y))

print(largerOnesDigit(134, 672)) # 4
print(largerOnesDigit(132, 674)) # Still 4


# test functions
def testOnesDigit():
    print("Testing onesDigit()...", end="")
    assert(onesDigit(5) == 5)
    assert(onesDigit(123) == 3)
    assert(onesDigit(100) == 0)
    assert(onesDigit(999) == 9)
    assert(onesDigit(-123) == 3) # Added this test
    print("Passed!")
testOnesDigit() # Crashed!  So the test function worked!


# default arguments
def j(x, y=10):
    return x + y
print(j(5)) # 15
print(j(5,1)) # 6