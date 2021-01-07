def abs1(n):
    if(n<0):
        n=-n
    return n

def abs2(n):
    if(n < 0): n=-n
    return n

def abs3(n):
    if(n < 0):
        return -n
    return n

def abs4(n):
    return (n < 0)*(-n) + (n>=0)*(n)

def abs5(n):
    if(n >= 0):
        return n
    else:
        return -n

def abs6(n):
    if(n >= 0):
        sign = +1
    else:
        sign = -1
    return sign * n

# all functions do the same thing!
print("abs1(5) =", abs1(5), "and abs1(-5) =", abs1(-5))
print("abs2(5) =", abs2(5), "and abs2(-5) =", abs2(-5))
print("abs3(5) =", abs3(5), "and abs3(-5) =", abs3(-5))
print("abs4(5) =", abs4(5), "and abs4(-5) =", abs4(-5))
print("abs5(5) =", abs5(5), "and abs5(-5) =", abs5(-5))
print("abs6(5) =", abs6(5), "and abs6(-5) =", abs6(-5))

