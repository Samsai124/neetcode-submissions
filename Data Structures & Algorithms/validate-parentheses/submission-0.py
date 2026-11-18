class Solution:
    def isValid(self, s: str) -> bool:
        maps = []
        for val in s:
            if val == ')':
                if not maps:
                    return False
                if maps.pop() != '(':
                    return False 
            elif val == ']':
                if not maps:
                    return False 
                if maps.pop() != '[':
                    return False 
            elif val == '}':
                if not maps:
                    return False 
                if maps.pop() != '{':
                    return False 
            else:
                maps.append(val)
        if maps:
            return False
        return True
                