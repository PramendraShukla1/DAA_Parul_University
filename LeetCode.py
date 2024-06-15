
'''
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
#--------------------------------------------------#
'''
26. Remove Duplicates from Sorted Array
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

def removeDuplicates(nums):
    left = 1

    for right in range(1,len(nums)):
        if nums[right] != nums[right - 1]:
            nums[left] = nums[right]
            left+=1
    return left


a = [1,1,2]
a = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(a))

'''
#--------------------------------------------------#
'''
1122. Relative Sort Array
link: https://leetcode.com/problems/rel-sort-array/

def relativeSortArray(arr1, arr2):
    res = []
    for a in arr2:
        for i, v in enumerate(arr1):
            if a == v:
                res.append(arr1[i])
    res = res+sorted([a for a in arr1 if a not in arr2])
    return res


arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
print(relativeSortArray(arr1,arr2))

'''
#--------------------------------------------------#
'''
75. Sort Colors
Link: https://leetcode.com/problems/sort-colors/description/?envType=daily-question&envId=2024-06-12

def sortColors(nums):
    n = len(nums)

    for i in range(n-1):
        swapped = False
        for j in range(0, n-i-1):
            if nums[j]>nums[j+1]:
                swapped = True
                nums[j], nums[j+1] = nums[j+1], nums[j]

        if not swapped:
            return



num = [2,0,2,1,1,0]
sortColors(num)
for i in range(len(num)):
    print(num[i])
    
'''
#--------------------------------------------------#
'''
344. Reverse String
Link: https://leetcode.com/problems/reverse-string/description/?envType=daily-question&envId=2024-06-02

def reverseString(s):
    left, right = 0, len(s)-1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left +=1
        right -= 1


s = ["h","e","l","l","o"]
reverseString(s)
print(s)
'''
#--------------------------------------------------#
'''
1979. Find Greatest Common Divisor of Array
Link: https://leetcode.com/problems/find-greatest-common-divisor-of-array/

def findGCD(nums):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    min_num = min(nums)
    max_num = max(nums)

    return gcd(min_num, max_num)


nums = [2, 5, 6, 9, 10]
print(findGCD(nums))

'''
#--------------------------------------------------#
'''
344. Reverse String
Link: https://leetcode.com/problems/reverse-string/

def reverseString(s):
    left, right = 0, len(s)-1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left+=1
        right-=1

s = ["h","e","l","l","o"]
reverseString(s)
print(s)
'''
#--------------------------------------------------#
'''
2037. Minimum Number of Moves to Seat Everyone
Link: https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/

def minMoves(seats, students):
    temp = 0
    seats.sort()
    students.sort()
    for i in range(len(seats)):
        temp += abs(seats[i] - students[i])
    return temp

seats = [3,1,5]
students = [2,7,4]
print(minMoves(seats, students))
'''
#--------------------------------------------------#

'''
945. Minimum Increment to Make Array Unique
Link: https://leetcode.com/problems/minimum-increment-to-make-array-unique/?envType=daily-question&envId=2024-06-14

def minIncrementForUnique(nums):
    nums.sort()
    temp = 0
    for i in range(1,len(nums)):
        pre = nums[i - 1]
        cur = nums[i]
        if pre >= cur:
            temp += pre-cur+1
            nums[i] = pre + 1
    return temp


nums = [1,1,2,2,3,7]
print(minIncrementForUnique(nums))
'''