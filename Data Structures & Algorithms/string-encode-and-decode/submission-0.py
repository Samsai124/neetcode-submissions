class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ''
        for val in strs:
            string += str(len(val))
            string += '#'
            string += val
        return string

    def decode(self, s: str) -> List[str]:
        original = []
        leng = 0
        while leng < len(s):
            num = leng
            while s[num] != '#':
                num += 1
            truenum = int(s[leng:num])
            original.append(s[num+1:num+truenum+1])
            leng = num + truenum + 1
        return original