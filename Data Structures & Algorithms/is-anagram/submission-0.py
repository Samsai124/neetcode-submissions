class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        maps = {}
        map2 = {}
        for let in s:
            maps[let] = maps.get(let,0) + 1
        for l in t:
            map2[l] = map2.get(l,0) + 1
        
        for key, value in maps.items():
            if value != map2.get(key,0):
                return False
        for key, value in map2.items():
            if value != maps.get(key,0):
                return False
        return True
