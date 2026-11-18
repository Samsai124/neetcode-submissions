class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        target = {}
        for val in s1:
            target[val] = target.get(val,0) + 1
        sub = {}

        for i in range(len(s2)):
            sub[s2[i]] = sub.get(s2[i],0) + 1
            if i - left == len(s1):
                if sub[s2[left]] == 1:
                    sub.pop(s2[left], None)
                else:
                    sub[s2[left]] = sub.get(s2[left],0) - 1
                left += 1
            if sub == target:
                return True
            
                
        return False