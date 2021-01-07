
employee_file = open("employees.txt", "a")
#r is read, w is write, a is append, r+ is read and write

employee_file.write("Toby - Human Resources")
employee_file.write("\nKelly - Customer Service")

employee_file = open("employees.txt", "w")
employee_file.write("Brandon - Sole Employee")

new_file = open("anotherfile.txt","w")