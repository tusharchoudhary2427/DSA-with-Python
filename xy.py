from typing import List  # Needed for List[int] type hint

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if not nums:
            return 0

        i = 0
        for j in range(1, n):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        return i + 1

nums = [1,1,1,2,3,4,4,7,9,9,9,10]

solution = Solution()
length = solution.removeDuplicates(nums)
print("Length of unique elements:", length)
print("Array after removing duplicates:", nums[:length])

# 

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i


# Example to test
nums = [3, 2, 2, 3]
val = 3
solution = Solution()
length = solution.removeElement(nums, val)
print("Length after removing:", length)
print("Array after removing:", nums[:length])



    

