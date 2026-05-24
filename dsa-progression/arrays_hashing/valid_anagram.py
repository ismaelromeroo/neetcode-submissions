"""
Pattern: sorting
Time Complexity: o(n log n)
Space Complexity:o(n)

Key Idea: two sting are anagrams if same length and same unique characters + frequencies
function: we use the sorted function to make the strings sorted list and comapre to establish if they are anagrams or not

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


can also use counter(s) == counter(t)
which is o(n) and o(n) since sorting adds an o(n) causing the n log n time complexity
"""