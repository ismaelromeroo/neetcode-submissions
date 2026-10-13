class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minnum = prices[0]
        profit = 0
        for p in prices:
            if p<minnum:
                minnum = p
            if p-minnum>profit:
                profit = p-minnum
        return profit
       