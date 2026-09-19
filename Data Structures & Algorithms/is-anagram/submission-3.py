import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      hash1 = dict()
      hash2 = dict()

      for num in s:
        hash1[num] = hash1.get(num,0) +1
      for num in t:
        hash2[num] = hash2.get(num,0) +1

      return hash1 == hash2
