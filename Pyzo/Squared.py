def squared(x):
    r = x[0] ** 2
    x[0] = 0
    return r
    
x = [5, 3, 1]
ret = squared(x)
print(ret)
print(x)