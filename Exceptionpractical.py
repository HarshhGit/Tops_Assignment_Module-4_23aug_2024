#Q.19] How Do You Handle Exceptions With Try/Except/Finally In Python? Explain with coding snippets.

"""Exception handling is a mechanism through which we can handle the runtime errors."""
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
try:
    ans = num1/num2
    print("Answer: ",ans)
except:
    print("Can not devide Number with Zero!!!")
finally:
    print("Finally block will run always")

#Q.20] Write python program that user to enter only odd numbers, else will raise an exception. 
num = int(input("Enter number: "))
try:
    if num % 2 == 1:
        print("Entered number: ",num)
    else:
        raise ValueError("can not use even number!!!!")
except ValueError as e:
    print(e)