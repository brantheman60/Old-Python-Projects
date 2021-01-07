# Quotes
print('single-quotes')
print("double-quotes")
print('''triple single-quotes''')
print("""triple double-quotes""")

# Newlines
print("abc\ndef")  # \n is a single newline character
print("""abc
def""")

print("""\
You can use a backslash at the end of a line in a string to exclude
the newline after it. This should almost never be used, but one good
use of it is in this example, at the start of a multi-line string, so
the whole string can be entered with the same indentation (none, that is).
""")

# Escape sequences
print("abc\tdef\tg\nhi\tj\\\tk\n---")

# Some String constants
import string
print(string.ascii_letters)   # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.ascii_lowercase) # abcdefghijklmnopqrstuvwxyz
print("-----------")
print(string.ascii_uppercase) # ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)          # 0123456789
print("-----------")
print(string.punctuation)     # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
print(string.whitespace)      # space + tab + linefeed + return + ...
print("-----------")
print(string.printable)       # digits + letters + punctuation + whitespace

# Some String Operators
print("abc" + "def")
print("abc" * 3)
print("ring" in "strings")
print("wow" in "amazing!")

s = "abcdefgh"
print(s)
print(s[1])
print(s[-1])
print(s[2:6])
print(s[3:])
print(s[:3])
print(s[:])
print(s[1:7:2])
print(s[0:8:3])
print(s[::-1])
print("".join(reversed(s)))

# Looping over Strings
s = "abcd"
for i in range(len(s)):
    print(i, s[i])

s = "abcd"
for c in s:
    print(c)

names = "fred,wilma,betty,barney"
for name in names.split(","):
    print(name)
    
quotes = """\
Dijkstra: Simplicity is prerequisite for reliability.
Knuth: If you optimize everything, you will always be unhappy.
Dijkstra: Perfecting oneself is as much unlearning as it is learning.
Knuth: Beware of bugs in the above code; I have only proved it correct, not tried it.
Dijkstra: Computer science is no more about computers than astronomy is about telescopes.
"""
for line in quotes.splitlines():
    if (line.startswith("Knuth")):
        print(line)
        
# Built-in String functions
print(str(1))
print(len("Hello!"))
print(ord("A"))
print(chr(70))
print(eval("3+4*5"))

# Character Type Functions Table
def p(test):
    print("True     " if test else "False    ", end="")
def printRow(s):
    print(" " + s + "  ", end="")
    p(s.isalnum()) # has only letters and numbers
    p(s.isalpha()) # has only letters
    p(s.isdigit()) # has only numbers
    p(s.islower()) # has letters, which are all lowercase
    p(s.isupper()) # has letters, which are all uppercase
    p(s.isspace()) # has only spaces
    print()
def printTable():
    print("  s   isalnum  isalpha  isdigit  islower  isupper   isspace")
    for s in "ABCD,ABcd,abcd,ab12,1234,    ,AB?!".split(","):
        printRow(s)
printTable()

# Some String methods
print("This is nice. Yes!".lower())
print("So is this? Sure!!".upper())
print("   Time to strip!    ".strip())
print("This is nice. Really nice.".replace("nice", "sweet"))
print("This is nice. Really nice.".replace("nice", "sweet", 1))
print("This is a history test".count("is")) # 3
print("Dogs and cats!".startswith("Do"))    # True
print("Dogs and cats!".endswith("!"))       # True
print("Dogs and cats!".find("and"))         # 5
print("Dogs and cats!".find("or"))          # -1
print("Dogs and cats!".index("and"))        # 5
print("Dogs and cats!".index("or"))         # crash!