
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