# Sample code for our discussion on writing good test functions.
# Your test functions should include as many tests as necessary,
# but not more.  Each test should have a reason to be there,
# covering some interesting edge case or scenario.

def testIsPrime():
    print("Testing isPrime()...")
    # if any of the cases are wrong, an AssertionError is passed
    assert(isPrime(-1) == False)  # negative
    assert(isPrime(0) == False)   # zero
    assert(isPrime(1) == False)   # 1 is quite the special case
    assert(isPrime(2) == True)    # 2, only even prime
    assert(isPrime(3) == True)    # 3, smallest odd prime
    assert(isPrime(4) == False)   # 4, smallest even non-prime
    assert(isPrime(9) == False)   # 9, perfect square of odd prime
    assert(isPrime(987) == False) # somewhat larger non-prime
    assert(isPrime(997) == True)  # somewhat larger prime
    print("Passed!")

def workingIsPrime1(n):
    if (n < 2): return False
    for factor in range(2, n):
        if (n % factor == 0):
            return False
    return True

def workingIsPrime2(n):
    if (n == 2): return True
    if ((n < 2) or (n % 2 == 0)): return False
    for factor in range(2, int(round(n**0.5))+1):
        if (n % factor == 0): return False
    return True

def brokenIsPrime1(n):
    # if (n < 2): return False # broken (commented out)
    for factor in range(2, n):
        if (n % factor == 0):
            return False
    return True

def brokenIsPrime2(n):
    if (n < 1): return False # broken: 2 -> 1
    for factor in range(2, n):
        if (n % factor == 0):
            return False
    return True

def brokenIsPrime3(n):
    if (n < 2): return False
    for factor in range(2, n+1): # broken: n -> n+1
        if (n % factor == 0):
            return False
    return True

def brokenIsPrime4(n):
    if (n < 2): return False
    for factor in range(2, n):
        if (n % factor == 0):
            return False
        else: # broken: no "else", should be after loop
            return True

def brokenIsPrime5(n):
    if (n == 2): return True
    if ((n < 2) or (n % 2 == 0)): return False
    for factor in range(2, int(round(n**0.5))): # broken, omitted +1
        if (n % factor == 0): return False
    return True

def raisesAssertion(f, *args):
    # Helper fn for testing test function.  You are responsible
    # for what this function does, but not how it does it.
    try: f(*args)
    except AssertionError: return True
    return False

def testTestIsPrime():
    print("Testing testIsPrime()...")
    global isPrime
    # Store the "real" function so we can restore it after our tests
    try: realIsPrime = isPrime
    except: realIsPrime = None
    # Now test our working and broken versions
    isPrime = workingIsPrime1
    assert(raisesAssertion(testIsPrime) == False)
    isPrime = workingIsPrime2
    assert(raisesAssertion(testIsPrime) == False)
    isPrime = brokenIsPrime1
    assert(raisesAssertion(testIsPrime) == True)
    isPrime = brokenIsPrime2
    assert(raisesAssertion(testIsPrime) == True)
    isPrime = brokenIsPrime3
    assert(raisesAssertion(testIsPrime) == True)
    isPrime = brokenIsPrime4
    assert(raisesAssertion(testIsPrime) == True)
    isPrime = brokenIsPrime5
    assert(raisesAssertion(testIsPrime) == True)
    # And restore the "real" version
    isPrime = realIsPrime
    print("Passed!")

testTestIsPrime()


# testing Exceptions
print("This is a demonstration of an exception object:")
try:
    print("Here we are just before the error!")
    print("1/0 equals:", (1/0))
    print("This line will never run!")
except Exception as e:
    print("Here's the error: ", e)
print("And that concludes our demonstration.")



# testing Console functions (Incomplete)
def foo():
    number = float(input("Type in a number"))
    print("One divided by this number is", 1/number)

def ioTest(testInput):
    import sys, io
    myOut = io.StringIO()
    myIn = io.StringIO(testInput)
    sys.stdout = myOut
    sys.stdin = myIn
    foo()
    return myOut.getvalue()

def testFoo():
    import sys
    print("Testing foo()...", end="")
    tmpOut = sys.stdout
    tmpIn = sys.stdin
    resultOne = ioTest("Test One Input\n")
    resultTwo = ioTest("Test Two Input\n")
    sys.stdout = tmpOut
    sys.stdin = tmpIn
    assert(resultOne == "Test One Expected Output\n")
    assert(resultTwo == "Test Two Expected Output\n")
    print("Passed.")