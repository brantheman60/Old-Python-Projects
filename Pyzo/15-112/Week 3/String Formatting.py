breed = "beagle"
print("Did you see a %s?" % breed)

dogs = 42
print("There are %d dogs." % dogs)

grade = 87.385
print("Your current grade is %f!" % grade)
print("Your current grade is %0.1f!" % grade)

dogs = 42
cats = 3
exclamation = "Wow"

print("There are %d dogs and %d cats. %s!!!" % (dogs, cats, exclamation))
# format right-aligned with %[minWidth]
print("%10s %10s" % ("dogs", "cats"))
print("%10d %10d" % (dogs, cats))      
# format left-aligned with %-[minWidth] 
print("%-10s %-10s" % ("dogs", "cats"))
print("%-10d %-10d" % (dogs, cats))
