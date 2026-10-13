class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area,n,m=0,0,len(heights)-1
        while(n<m):
            w = min(heights[n],heights[m])
            l = m-n
            area=max(area,w*l)
            if heights[n] == w and n<m:
                n+=1
            else:
                m-=1
        return area