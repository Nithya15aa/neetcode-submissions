class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        for i,a in enumerate(heights):
            l = i 
            r = len(heights) - 1
            

            while l < r:
                maxArea=max(maxArea, min(a,heights[r]) *( r -l))
                if heights[l] < heights[r]:
                    l +=1
                else:
                    r -=1
        return maxArea
        

                


        