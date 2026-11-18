class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        point1 = 0
        point2 = len(heights) - 1
        while point2 > point1: 
            if heights[point1] < heights[point2]:
                area = max(area, (point2 - point1) * heights[point1]) 
                point1 = point1 + 1
            else:
                area = max(area, (point2 - point1) * heights[point2])
                point2 = point2 - 1
            
        
        return area


        