class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = []
        maps = {}
        for val in strs:
            sorts = sorted(val)
            sorts = "".join(sorts)
            if sorts in maps:
                temp = maps.get(sorts)
                anagram[temp].append(val)
            else:
                anagram.append([val])
                maps[sorts] = len(anagram)-1
        return anagram