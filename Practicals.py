#-------------------Practical-1---------------------#
'''
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
'''

#-------------------Practical-2---------------------#
#Link: https://leetcode.com/problems/binary-search/description/
'''
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left,right = 0, len(nums)-1
        while(left<=right):
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid]<target:
                left = mid+1
            else:
                    right = mid-1
        return left
        
'''
#-------------------Practical-3---------------------#
#Link: https://leetcode.com/problems/candy/description/
'''
class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        arr = [1] * len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i - 1] < ratings[i]:
                arr[i] = arr[i - 1] + 1

        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                arr[i] = max(arr[i], arr[i + 1] + 1)

        return sum(arr)
'''

#-------------------Practical-4---------------------#
#Link: https://www.naukri.com/code360/problems/aggressive-cows_1082559
'''
def aggressiveCows(stalls, k):
    stalls.sort()
    s, e = 0, stalls[-1]
    ans = -1
    
    while s <= e:
        mid = (s + e) // 2
        if isPossible(stalls, k, mid, len(stalls)):
            ans = mid
            s = mid + 1
        else:
            e = mid - 1
        mid = (s + e) // 2
    
    return ans


def isPossible(stalls, k, mid, n):
    cowCount = 1
    lastPos = stalls[0]
    
    for i in range(n):
        if stalls[i] - lastPos >= mid:
            cowCount += 1
            if cowCount == k:
                return True
            lastPos = stalls[i]
    
    return False
'''
#-------------------Practical-5---------------------#
#Link: https://www.naukri.com/code360/problems/detect-cycle-in-an-undirected-graph_758967