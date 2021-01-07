def yes():
    return True

def no():
    return False

def crash():
    return 1/0 # crashes!
    
print(no() and crash()) # Works!
print(crash() and no()) # Crashes!
print (yes() and crash()) # Never runs (due to crash), but would also crash (without short-circuiting)

print(yes() or crash()) # Works!
print(crash() or yes()) # Crashes!
print(no() or crash())  # Never runs (due to crash), but would also crash (without short-circuiting)