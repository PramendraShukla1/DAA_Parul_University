'''
#Practical 1 : write a program to determine whether the given number is Prime or not.
def checkPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
        return True


num = int(input("Enter a number ->"))
result = checkPrime(num)

if result:
    print("Number is Prime")
else:
    print("Number is not Prime")



#Question 1: Write a program to count numbers which are prime in a given range

def checkPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
        return True

def countPrime(num):
    count = 0
    for i in range (0, num):
        if checkPrime(i):
            count += 1
    return count


num = int(input("Enter number"))
result = countPrime(num)
print(result)


LeetCode Problem 1:
1051. Height Checker
Link: https://leetcode.com/problems/height-checker/description/?envType=daily-question&envId=2024-06-10


def heightChecker(heights):
    copyHeights = sorted(heights)
    count = 0
    for i in range (len(heights)):
        if heights[i] != copyHeights[i]:
            count+=1
    return count

a = [1,1,4,2,1,3]
print(heightChecker(a))

'''
