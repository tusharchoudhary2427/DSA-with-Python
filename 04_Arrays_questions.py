''' question -> Finding the largest element in an array? '''

def largest_element(nums): # we do not pass largest here becuase its self-contained, no need for the caller to know what initial value to use.
    n = len(nums)
    largest = nums[0] # the first element is a safe and valid choice. 

    for i in range(0, n):
        largest = max(largest, nums[i])

    return largest

nums = [55, 32, -97, 99, 3, 67]
result = largest_element(nums)
print(result)
 
''' question -> Finding the 2nd largest element in an array? '''

def second_largest(nums):
    largest = float("-inf") # At the start, we don’t know what the array contains — it might even be all negative numbers. This makes sure any number in the list will be larger than these starting values, so the comparisons work correctly.

    second_largest = float("-inf")
    n = len(nums)

    for i in range(0,n):
        if nums[i] > largest:
            second_largest = largest
            largest = nums[i]

        elif nums[i] > second_largest and nums[i] != largest:
            second_largest = nums[i] 

    return second_largest

nums = [55,32,97,-55,45, 32, 88, 21]
nums.sort()
result = second_largest(nums)
print(result)

''' question -> check if an Array is Sorted or not? '''

def sorted_array(nums):
    n = len(nums)

    for i in range(0 , n - 1): # here we are comparing nums[i] with nums[i+1] and you don't want to exceeds the list
        if nums[i] < nums[i+1]:
            return True
        else:
            return False
        
nums = [55,32,97,-55,45, 32, 88, 21]

result = sorted_array(nums)
print(result)

''' question -> removing duplicates from a sorted array? '''

def removing_duplicates(nums):  # -> Brute force solution
    n = len(nums)
    freq_map = {}

    for i in range(0 , n):
        freq_map[nums[i]] = 0

    j = 0
    for k in freq_map: # in this loop, it takes the unique keys from the dictionary and place it in the original list (nums).
        nums[j] = k
        j+=1

    return j

nums = [1,1,1,2,3,4,4,7,9,9,9,10]

result = removing_duplicates(nums)
print(f"The number of duplicates are: {result}")

# optimal solution 

def remove_dupli(nums):
    n = len(nums)
    if n == 1:
        return 1
    
    i = 0
    j = i + 1

    while j < n:
        if nums[j] != nums[i]:
            i += 1
            nums[i],nums[j] = nums[j],nums[i]
        j += 1
    
    return i + 1

nums = [1,2,1,1,3,4,4,7,9,9,9,10]

result = remove_dupli(nums)
print(f"The number of duplicates are: {result}")



