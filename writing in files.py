
employee_file=open("employee.txt", "a")
employee_file.write("\nToby-Human Resources")
employee_file.write("\nKelly-Customer service")

#the "w" overwrites everything
employee_file=open("employee.txt", "w")
employee_file.write("\nToby-Human Resources")
employee_file.write("\nKelly-Customer service")

employee_file.close()