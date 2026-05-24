"""
Pattern: hash set/map
Time Complexity: O(n)
Space Complexity: O(n)

Key Idea: true is list of num has a duplicate integer value
utilized a set to idenity if the given list had duplicates. if the lengths are equal then doesnt have dupes if set and list have different lengths then contains dupes

Mistake Learned:
reinforced how nesed loops work, however that way of solving the problem had poor time complexity comapared to the set method.

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False
        
"""