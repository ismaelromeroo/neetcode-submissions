class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n,m=0,len(numbers)-1
        while(n<m):
            curr = numbers[n] + numbers[m]
            if curr<target:
                n+=1
            if curr>target:
                m-=1
            if curr==target:
                return[n+1,m+1]        