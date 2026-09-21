class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = collections.defaultdict(list)
        for s in strs:
            lis = [0] * 26
            for c in s:
                lis[ord(c)-ord('a')] += 1
        
            output[tuple(lis)].append(s)
        return list(output.values())