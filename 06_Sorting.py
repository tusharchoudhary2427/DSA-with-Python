'''Sorting -> It is used to rearrange a given array or list of elements in an order.'''


# bubble sort -> algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order.

nums = [5,8,1,6,9,2,4]

n = len(nums)

for i in range(0 , n-1):
    is_swap = False,

    for j in range(n - 1 - i):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
            is_swap =True
    
    if is_swap == False:
        break

    print(nums) # TC-> O(n(n+1))/2 => O(n^2) for avg and worst and O(n) for best case and SC -> O(1)


# selection sort -> Finding the smallest number, and putting it at the beginning, then repeating this for the rest of the list.

nums = [5,7,8,4,1,6,9,2]

n = len(nums)

for i in range(0,n):
    min_index = i

    for j in range(i + 1, n):
        if nums[j] < nums[min_index]:
            min_index = j

    nums[i], nums[min_index] = nums[min_index], nums[i]


print(nums) # TC-> O(n(n+1))/2 => O(n^2), it is same for all the cases and SC -> O(1)



# insertion sort -> It works by iteratively inserting each element of an unsorted list into its correct position in a sorted portion of the list.

nums = [3,5,6,4,8,9,10,7,1]

n = len(nums)

for i in range(0, n):
    key = nums[i]
    j = i - 1

    while j >= 0 and nums[j] > key:
        nums[j + 1] = nums[j]
        j-=1

    nums[j + 1] = key

print(nums)

# merge sort -> It follows the divide-and-conquer approach. It works by dividing the input array into two halves, and the sorting the two halves and finally merging them back together to obtain the sorted array.

nums = [3,1,2,4,1,5,2,6,4]

def merge_array(left,right):
    result = [ ]
    i,j = 0,0
    n,m = len(left), len(right)

    while i < n and j < m:
        if left[i] < right[j]:
            result.append(left[i])
            i+=1

        else:
            result.append(right[j])
            j+=1

    if i < n:
        while i < n:
            result.append(left[i])
            i+=1

    if j < m:
        while j < m:
            result.append(right[j])
            j+=1

    return result

def merge_sort(arr):
    if len(arr) <=1:
        return arr
    
    mid = len(arr)//2
    left =  merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge_array(left,right)

print(merge_sort(nums))
    
# quick sort -> It picks an element as a pivot and partitions the given array around the picked pivot by placing the pivot in its correct position in the sorted array.

nums = [4,1,7,6,3,2,8]

def partition(nums, low, high):
    pivot = nums[low]
    i = low
    j = high

    while i < j:
        while nums[i] <= pivot and i <= high - 1:
            i += 1

        while nums[j] > pivot and j >= low + 1:
            j -= 1

        if i<j:
            nums[i],nums[j] = nums[j],nums[i]

    nums[low], nums[j] = nums[j], nums[low] 

    return j 

p_index = partition(nums, 0, len(nums) - 1)  # TC-> best/avg - O(nlogn), worst -> O(n^2) ans SC-> O(1)
print(nums)



