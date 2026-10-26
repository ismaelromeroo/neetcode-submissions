from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = Counter(nums)
        max_val = 0
        output = 0
        for num , f in freq.items():
            if f>max_val:
                max_val = f
                output = num
        return output

        

        