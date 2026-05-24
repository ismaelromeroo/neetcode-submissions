class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums) + 1)]
        res = {}

        for n in nums:
            res[n] = 1 + res.get(n, 0)

        count = list(res.items())
        for num,rate in count:
            freq[rate].append(num)

        final = []
        for i in range(len(nums),0,-1):
            for num in freq[i]:
                final.append(num)
                if len(final) == k:
                    return final
           