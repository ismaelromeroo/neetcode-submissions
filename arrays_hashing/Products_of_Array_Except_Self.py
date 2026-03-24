"""
pattern:array prefix postfix summation
time: o(n)
space: o(n)

key insight:
was able to code out the solution without seeing the solution at first by solely looking at the solution
video however used chat to help debug need to force myslef to do it on my own but definitly one of 
my better preformances

code:
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        prefix = 1
        postfix = 1
        for i in range(len(nums)):
           output[i] = prefix
           prefix *= nums[i]
        for j in range(len(nums)-1,-1,-1):
            output[j] = output[j] * postfix
            postfix *= nums[j]
        return output
"""