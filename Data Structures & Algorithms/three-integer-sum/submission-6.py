class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sort = sorted(nums)
        output = []
        for i in range(len(nums)-1):
            n=i+1
            m=len(nums)-1
            a=sort[i]*-1
            if i>0 and sort[i] == sort[i-1]:
                continue
            while(n<m):
                curr = sort[n] + sort[m]
                if curr<a:
                    n+=1
                if curr>a:
                    m-=1
                if curr==a:
                    output.append([sort[i],sort[n],sort[m]])
                    n,m=n+1,m-1
                    while n<m and sort[n] == sort[n - 1]:
                        n+=1
                    while n<m and sort[m] == sort[m + 1]:
                        m-=1
        return output
