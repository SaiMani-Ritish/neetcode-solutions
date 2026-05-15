class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hmap = {}
        for i in range(len(s)):
            hmap[s[i]] = 1 + hmap.get(s[i],0)
            hmap[t[i]] = hmap.get(t[i],0) - 1
        for val in hmap.values():
            if val != 0:
                return False 
        return True 


























        if len(s) != len(t):
            return False
        smap = {}
        tmap = {}

        for i in range(len(s)):
            smap[s[i]] = 1 + smap.get(s[i],0)
            tmap[t[i]] = 1 + tmap.get(t[i],0)
        return smap == tmap
        
