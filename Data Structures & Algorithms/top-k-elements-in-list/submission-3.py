class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums) + 1)]
        count = {}

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for num,rate in list(count.items()):
            freq[rate].append(num)

        res = []
        for i in range(len(nums),0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
           