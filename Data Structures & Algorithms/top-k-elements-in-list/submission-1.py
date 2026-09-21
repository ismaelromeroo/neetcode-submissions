class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = collections.defaultdict(int)
        for n in nums:
            freq[n] = freq.get(n,0)+1
        return sorted(freq.keys(), key=lambda x: freq[x], reverse=True)[:k]

        
           