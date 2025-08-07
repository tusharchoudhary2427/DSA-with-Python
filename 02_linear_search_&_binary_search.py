'''Linear Search -> iterating over all the elements of the array and check if it the current element is equal to the target element.'''

def find_target(nums, target):
    n = len(nums)
    for i in range(0, n):
        if nums[i] == target:
            return i
    return -1


nums = [5,3,9,8,6,4,-10,-69]
target = 4

result = find_target(nums, target)
print(result)

'''Binary Search -> It searches through an array and returns the index of the value it searches for. It works by checking the value in the center of the array. If the target value is lower, the next value to check is in the center of the left half of the array. '''

def binary_search(nums,target):
    n =  len(nums)
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high)//2

        if nums[mid] == target:
            return mid
        
        elif nums[mid] < target:
            low = mid + 1

        else:
            high = mid - 1
        
    return -1



nums = [2,4,6,7,9,11,18,19] # here, low = 0 and high = n-1 => 8 - 1 -> 7.
target = 9

result = binary_search(nums, target)
print(result) # it's time complexity is log2(n), where n is the no. of elements in list


'''Lower Bound -> smallest index such that nums[i] >= target'''

def lower_bound(nums,target):
    n = len(nums)
    lb = -1
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high)//2
        if nums[mid] >= target:
            lb = mid
            high = mid - 1
        else:
            low = mid + 1

    return lb

nums = [1,1,1,2,3,3,5,6,7,7,7,9,12,13]
target = 7

result = lower_bound(nums,target)
print(result)

'''Upper Bound -> smallest index such that nums[i] > target'''

def upper_bound(nums,target):
    n = len(nums)
    ub = n # to avoid off-by-one errors. 
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high)//2
        if nums[mid] > target:
            ub = mid
            high = mid - 1
        else:
            low = mid + 1

    return ub


nums = [1,1,1,2,3,3,5,6,7,7,7,9,12,13]
target = 9

result = upper_bound(nums,target)
print(result)












