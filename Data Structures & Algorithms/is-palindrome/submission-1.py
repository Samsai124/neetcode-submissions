class Solution:
    def isPalindrome(self, s: str) -> bool:
        point1 = 0
        point2 = len(s)-1
        while(point1 < point2):
            if s[point1].isalnum() and s[point2].isalnum():
                if s[point1].lower() != s[point2].lower():
                    return False
            if not s[point1].isalnum() and not s[point2].isalnum():
                point1 = point1 + 1
                point2 = point2 - 1
                continue
            if not s[point1].isalnum():
                point1 = point1 + 1
                continue
            if not s[point2].isalnum():
                point2 = point2 - 1
                continue
            point1 = point1 + 1
            point2 = point2 - 1

        return True
        