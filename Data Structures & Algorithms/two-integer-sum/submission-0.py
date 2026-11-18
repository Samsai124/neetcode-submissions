class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maps = {}
        difference = 0
        answer = []
        for index, i in enumerate(nums):
            difference = target - i
            if difference in maps:
                answer = [maps.get(difference),index]
            else:
                maps[i] = index
        return answer