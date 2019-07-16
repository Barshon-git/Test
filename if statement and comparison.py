def max(num1, num2, num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    else:
        return num3


num1=input("Enter the first number: ")
num2=input("Enter the second number: ")
num3=input("Enter the third number: ")

print(max(num1,num2,num3))