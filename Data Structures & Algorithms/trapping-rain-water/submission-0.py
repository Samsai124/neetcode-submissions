class Solution:
    def trap(self, height: List[int]) -> int:
        maxed = 0
        left = []
        right = []
        area = 0

        for i in range(len(height)):
            maxed = max(maxed,height[i])
            left.append(maxed)
        maxed = 0
        for i in range(len(height) - 1, -1, -1):
            maxed = max(maxed,height[i])
            right.append(maxed)
        right.reverse()
        for i in range(len(height)):
            area += min(left[i],right[i]) - height[i]
        return area