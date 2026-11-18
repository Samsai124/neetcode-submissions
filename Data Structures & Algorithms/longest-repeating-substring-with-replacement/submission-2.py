class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        freq = 0
        second = 0
        for right in range(len(s)):
            count[s[right]] = count.get(s[right],0) + 1
            freq = max(freq, count.get(s[right]))
            second = (right - left + 1) - freq
            if second > k:
                while second > k:
                    count[s[left]] = count.get(s[left]) - 1
                    left += 1
                    second = (right - left + 1) - freq
        return freq + second


        