class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLength = 0
        length = 0
        next = 0
        consec = True
        for val in nums:
            length = 1
            next = val + 1
            consec = True
            while consec:
                consec = False
                if next in nums:
                    length = length + 1
                    next = next + 1
                    consec = True
            maxLength = max(length, maxLength)
        return maxLength

            