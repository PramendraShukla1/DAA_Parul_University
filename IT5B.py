# Write a program to check if a given number is prime or not
'''


def checkPrime(num):
    for i in range (2, num):
        if num % i ==0:
            return False
    return True

num = int(input("Enter a number -> "))
result = checkPrime(num)

if result == True:
    print("The number is prime")
else:
    print("The number is not prime")
'''


