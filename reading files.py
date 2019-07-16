employee_file=open("employee.txt", "r")
print(employee_file.read())
#comment out the previous line to see the latter results
print(employee_file.readline())
print(employee_file.readline())

#comment out the previous line to see the latter result
print(employee_file.readlines())

employee_file=open("employee.txt", "r")
for employee in employee_file.readlines():
    print(employee)
employee_file.close()


