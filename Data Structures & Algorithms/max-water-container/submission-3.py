class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area,n,m=0,0,len(heights)-1
        while(n<m):
            w = min(heights[n],heights[m])
            l = m-n
            if heights[n] == w and n<m:
                n+=1
            else:
                m-=1
            if w*l>area:
                area=w*l
        return area