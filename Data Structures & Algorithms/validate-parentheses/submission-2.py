class Solution:
    def isValid(self, s: str) -> bool:
        curr = []
        for val in s:
            if val == '(' or val == '{' or val == '[':
                curr.append(val)
            else:
                if not curr:
                    return False
                if val == ')' and curr.pop() != '(':
                    return False
                elif val == '}' and curr.pop() != '{':
                    return False
                elif val == ']' and curr.pop() != '[':
                    return False
        return True