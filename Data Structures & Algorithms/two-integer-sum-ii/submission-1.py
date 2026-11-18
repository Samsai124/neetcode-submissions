class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        diff = 0
        result = []
        for index, val in enumerate(numbers):
            diff = target - val
            if diff in numbers:
                result.append(index+1)
                count = 1
                for vals in numbers:
                    if vals == diff:
                        result.append(count)
                        return result
                    count = count + 1

                        

        