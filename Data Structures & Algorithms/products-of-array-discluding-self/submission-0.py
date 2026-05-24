class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        product = 1
        for i in range(len(nums)):
            cnum = nums.copy()
            cnum.remove(nums[i])
            for c in cnum:
                product *= c
            output.append(product)
            product = 1
        return output
