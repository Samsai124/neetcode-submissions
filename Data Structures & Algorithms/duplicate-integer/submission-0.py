class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        maps = set()
        for val in nums:
            if val in maps:
                return True
            else:
                maps.add(val)
        return False

        