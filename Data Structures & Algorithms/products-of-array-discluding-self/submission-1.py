class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        output = []
        zero_count = nums.count(0)
        for val in nums:
            if val != 0:
                product *= val
        if zero_count > 1:
            return [0] * len(nums)
        if 0 in nums:
            for vals in nums:
                if vals != 0:
                    output.append(0)
                else:
                    output.append(product)
        else:
            for vals in nums:
                output.append(product//vals)
        return output
