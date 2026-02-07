# s and t strings given
# if s and t are anagrams
    # return true
# return false

# two hashmaps, for s and t
# for i in s
    # add to hashmap
# for i in t
    # add to hashmap
# if s==t
    # return true
# return false


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        smap = dict()
        tmap = dict()

        for i in s:
            if i in smap:
                smap[i] += 1
            else:
                smap[i] = 1
        
        for i in t:
            if i in tmap:
                tmap[i] += 1
            else:
                tmap[i] = 1
        
        if smap == tmap:
            return True
        return False