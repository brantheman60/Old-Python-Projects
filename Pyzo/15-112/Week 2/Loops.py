# for loop
def sumFromMToN(m, n):
    total = 0
    # note that range(x, y) includes x but excludes y
    for x in range(m, n+1):
        print(x)
        total += x
    return total
print(sumFromMToN(5, 10))

# or simply...
def sumFromMToN(m, n):
    return sum(range(m, n+1))
print(sumFromMToN(5, 10))

# 1 parameter
def sumToN(n):
    total = 0
    for x in range(n+1):
        total += x
    return total
print(sumToN(5)) #1+2+3+4+5

# 3 parameters
def sumEveryKthFromMToN(m, n, k):
    total = 0
    for x in range(m, n+1, k):
        total += x
    return total
print(sumEveryKthFromMToN(5, 20, 7)) #5+12+19

# nested for loops
def printCoordinates(xMax, yMax):
    for x in range(xMax+1):
        for y in range(yMax+1):
            print("(", x, ",", y, ")  ", end="")
        print()
printCoordinates(4, 5)

# while loops
def leftmostDigit(n):
    n = abs(n)
    while (n >= 10):
        n = n//10
    return n
print(leftmostDigit(72658489290098) == 7)

# break and continue
for n in range(200):
    if (n % 3 == 0):
        continue # skips rest of this pass
    elif (n == 8):
        break # skips rest of entire loop
    print(n, end=" ")
print()