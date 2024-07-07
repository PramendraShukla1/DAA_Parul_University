
# MERGE SORT ALGORITHM
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

# MERGE SORT ALGORITHM

#BUBBLE SORT ALGORITHM
def bubbleSort(nums):
    for i in range(len(nums)-1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp

#BUBBLE SORT ALGORITHM

# SELECTION SORT ALGORITHM
def selectionSort(nums):
    for i in range(len(nums)-1):
        min_index = i
        for j in range (i+1, len(nums)):
            if nums[min_index] > nums[j]:
                min_index = j

        nums[i], nums[min_index] = nums[min_index], nums[i]
# SELECTION SORT ALGORITHM


#INSERTION SORT ALGORITHM
def insertionSort(nums):
    # Traverse through 1 to len(arr)
    for i in range(1, len(nums)):
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i
        while nums[j - 1] > nums[j] and j > 0:
            nums[j - 1], nums[j] = nums[j], nums[j - 1]
            j -= 1
#INSERTION SORT ALGORITHM

#BUBBLE SORT ALGORITHM
def bubbleSort2(arr):
    n = len(arr)
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    # Traverse through all array elements
    for i in range(n-1):

        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        swapped = False
        for j in range(0, n-i-1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if not swapped:
            # if we haven't needed to make a single swap, we
            # can just exit the main loop.
            return

#BUBBLESORT


#QUICK SORT ALGORITHM

#QUICK SORT ALGORITHM


# Example usage:
arr = [5, 2, 8, 3, 1, 6, 4]
arr = merge_sort(arr)
print(arr)