
'''

Two number sum :

def addTwo(a,b):
    return a+b

a = int(input("Enter first number"))
b = int(input("Enter second number"))
print(addTwo(a,b))



Find Greatest between three numbers:

def maximum(a, b, c):
    if (a>=b) and (a>=c):
        largest = a
    elif(b>=a) and (b>=c):
            largest = b
    else:
        largest = c
        return largest


a = int(input(" Enter number one "))
b = int(input(" Enter number two "))
c = int(input(" Enter number three"))
print(maximum(a,b,c))

'''

#Pracical 1 : write a program to determine whether the given number is Prime or not.

def checkPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
        return True

num = int(input("Enter number -> "))
result = checkPrime(num)

if result:
    print("Number is Prime")
else:
    print("Number is not prime")
