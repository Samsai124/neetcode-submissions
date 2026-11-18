class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maps = {}
        difference = 0
        
        for index, i in enumerate(nums):
            difference = target - i
            if difference in maps:
                return [maps.get(difference),index]
            else:
                maps[i] = index