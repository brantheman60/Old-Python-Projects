
employee_file = open("employees.txt", "r")
#r is read, w is write, a is append, r+ is read and write

print(employee_file.readable())

for employee in employee_file.readlines():
    print(employee)
#print(employee_file.read())
#print(employee_file.readlines())
#print(employee_file.readlines()[2])
'''
print(employee_file.readline())
print(employee_file.readline())
print(employee_file.readline())
print(employee_file.readline())
'''

employee_file.close()
