# Creating Lists
a = [2, 3, 5, 7]
b = list()
c = ["mixed types", True, 42]
d = list(range(5))
e = [0] * 10
f = [i for i in range(10)]
g = [(i*100) for i in range(20) if i%5 == 0]

print(len(a), a)
print(len(b), b)
print(len(c), c)
print(len(d), d)
print(len(e), e)
print(len(f), f)
print(len(g), g)

# List Properties
print("a = ", a)
print("len =", len(a))
print("min =", min(a))
print("max =", max(a))
print("sum =", sum(a))

# Accessing Elements
a = [2, 3, 5, 7, 11, 13]
print("a        =", a)
print("a[0]     =", a[0])
print("a[2]     =", a[2])
print("a[-1]    =", a[-1])
print("a[-3]    =", a[-3])

print("a[0:2]   =", a[0:2])
print("a[1:4]   =", a[1:4])
print("a[1:6:2] =", a[1:6:2])

# List Aliases
a = [ 2, 3, 5, 7 ]
b = a

a[0] = 42
b[1] = 99
print(a)
print(b)
print(a is b) #b and a refer to the same list!

# List Copies
import copy
a = [ 2, 3, 5, 7 ]
b = copy.copy(a)

a[0] = 42
b[1] = 99
print(a)
print(b)
print(a is b) #b and a are different lists!

# Finding Elements
a = [ 2, 3, 5, 2, 6, 2, 2, 7 ]
print("2 in a =", (2 in a))
print("4 not in a =", (4 not in a))
print("a.count(1) =", a.count(1))
print("a.count(2) =", a.count(2))

print("a.index(6)   =", a.index(6))
print("a.index(2)   =", a.index(2))
print("a.index(2,1) =", a.index(2,1))
#print("a.index(9) =", a.index(9)) # crashes! passes ValueError

# Adding Elements
a = [2, 3]
a.append(5)
a += [6, 7]
a.extend([8, 9])
a.insert(2, 4)
print(a)

# Removing Elements
a               = [2, 3, 5, 3, 7, 6, 5, 11, 13]
a.remove(5)     # [2, 3, 3, 7, 6, 5, 11, 13]
a.remove(5)     # [2, 3, 3, 7, 6, 11, 13]
a.pop(4)        # [2, 3, 3, 7, 11, 13]
a.pop()         # [2, 3, 3, 7, 11]
a[2:4] = [ ]    # [2, 3, 11]
del a[1:3]      # [2]

# Swapping Elements
a = [1, 2, 3, 4]
temp = a[0]
a[0] = a[1]
a[1] = temp
print("a=",a)

a = [1, 2, 3, 4]
a[0],a[1] = a[1],a[0]
print("a=",a)

# Looping Over Lists
a = [ 2, 3, 5, 7 ]

for item in a:
    print(item)
        
for index in range(len(a)):
    print("a[", index, "] =", a[index])

for item in reversed(a):
    print(item)

# Comparing Lists
a = [ 2, 3, 5, 3, 7 ]
b = [ 2, 3, 5, 3, 7 ]   # same as a
c = [ 2, 3, 5, 3, 8 ]   # differs in last element
d = [ 2, 3, 5 ]         # prefix of a

print("a =", a)
print("b =", b)
print("c =", c)
print("d =", d)

print("------------------")
print("a == b", (a == b))
print("a == c", (a == c))
print("a != b", (a != b))
print("a != c", (a != c))

print("------------------")
print("a < c", (a < c))
print("a < d", (a < d))

# Sorting Lists
a = [ 7, 2, 5, 3, 5, 11, 7 ]
print("At first, a =", a)
a.sort()
print("After a.sort(), a =",a)

a = [ 7, 2, 5, 3, 5, 11, 7 ]
print("At first, a =", a)
b = sorted(a)
print("After b = sorted(a), b =", b)

a = [ 10, 2, -5, 8, -3, 7, 1 ]
print(sorted(a))
print(sorted(a, key=abs))

# Tuples
t = (1, 2, 3)
print(type(t), len(t), t)

a = [1, 2, 3]
t = tuple(a)
print(type(t), len(t), t)

#t[0] = 2 # error!

# Parallel Tuple Assignment
(x, y) = (1, 2)
print("x =", x,",\ty =", y)

(x, y) = (y, x)
print("x =", x,",\ty =", y)

(x, y, z) = (1, 2, 3)
print("x =", x,",\ty =", y, "\tz =",z)

(x, y, z) = (y, z, x)
print("x =", x,",\ty =", y, "\tz =",z)

# Singleton Tuple
t = (42)
print(type(t), t*5)

t = (42,)
print(type(t), t*5)

# Converting Between Lists and Strings
a = list("wahoo!")
print(a)

a = "How are you doing today?".split(" ")
print(a)

s = "".join(a)
print(s)

a = ["parsley", " ", "is", " ", "gharsley"] # by Ogden Nash!
s = "".join(a)
print(s)