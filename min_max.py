#Min Max using divide and conquer approach
'''
def max_min(arr):
    if len(arr) == 1:
        return arr[0], arr[0]

    mid = len(arr) // 2
    left_max, left_min = max_min(arr[:mid])
    right_max, right_min = max_min(arr[mid:])

    return max(left_max, right_max), min(left_min, right_min)

# Example usage
arr = [3, 1, 4, 1, 5, 9, 2, 6]
max_element, min_element = max_min(arr)
print("Max element:", max_element)
print("Min element:", min_element)

'''
#Min Max using linear approach
'''
def find_max_min(arr):
    n = len(arr)
    max_index = 0
    min_index = 0

    for i in range(1, n):
        if arr[i] > arr[max_index]:
            max_index = i
        if arr[i] < arr[min_index]:
            min_index = i

    print("Max element is:", arr[max_index])
    print("Min element is:", arr[min_index])

# Example usage
arr = [20, 3, 40, 2, 60, 12]
find_max_min(arr)
'''
