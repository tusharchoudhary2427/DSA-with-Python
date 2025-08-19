'''Two Sum -> Given an array of 'integers' nums and an integer 'target', return indices of the two numbers such that they add up to target. '''

class Solution:
    def TwoSum(self, nums: list[int], target: int) -> list[int]:
        dic = {}
        n = len(nums)

        for i in range(n):
            remaining = target - nums[i]
            if remaining in dic:
                return [dic[remaining], i]
            else:
                dic[nums[i]] = i

nums = [2,7,11,15,19]
target = 9
sol = Solution()

result = sol.TwoSum(nums,target)
print(result)


'''Binary Searh -> Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1. '''

class Binary:
    def BinarySearch(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        low = 0
        high = n - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid
            
            elif nums[mid] < target:
                low = mid + 1

            else:
                high = mid - 1

        return -1
    
nums = [-1,0,3,5,9,12,18]
target = 9
sol = Binary()

result = sol.BinarySearch(nums,target)
print(result)


'''Removing duplicates from Sorted Array -> Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.'''

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        if not nums:
            return 0     
    
        i = 0

        for j in range(1,n):
            if nums[j] != nums[i]:
                i += 1
            nums[i] = nums[j]

        return i + 1

nums = [3,2,2,3]
val = 3
sol = Solution()

result = sol.removeDuplicates(nums)
print(result)


'''Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.'''

class MinStack:
    def __init__(self):
        self.items = []

    def push(self,val: int):
        if len(self.items) == 0:
            self.items.append([val,val])
        else:
            mini = min(self.items[-1][1],val)
            self.items.append([val,mini])

    def pop(self):
        if len(self.items) != 0:
            self.items.pop()

    def top(self):
        if len(self.items) == 0:
            return None
        else:
            return self.items [-1][0]

    def getMin(self):
        if len(self.items) == 0:
            return None
        else:
            return self.items[-1][1]

m = MinStack()
m.push(5)
m.push(7)
m.push(2)
m.push(10)
m.push(8)
m.push(15)
  
print(m.top())
print(m.getMin())


'''Valid Parenthesis -> Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.'''

class Parenthesis:
    def isValid(self,s:str) -> bool:
        stack = []
        for b in s:
            if b in "{[(":
                stack.append(b)

            else:
                if len(stack) == 0:
                    return False
                
                ch = stack.pop()
                if (b == ")" and ch != "(") or \
                   (b == "}" and ch != "{") or \
                   (b == "]" and ch != "["):
                   return False

        return len(stack) == 0
                

