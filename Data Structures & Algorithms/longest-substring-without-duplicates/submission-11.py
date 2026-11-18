class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        r = 0
        l = 0
        longest = 0
        seen = {}
        if len(s) > 0:
            seen[s[0]] = 0
            longest = max(longest, r-l+1)
        r += 1
        while r < len(s):
            if s[r] in seen and seen[s[r]] >= l:
                l = seen.get(s[r]) + 1

            seen[s[r]] = r
            longest = max(longest, r-l+1)
            r += 1
           
        return longest
