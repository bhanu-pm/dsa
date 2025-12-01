#  - so anagrams are composed of same letters in same quantities
#     - make each word a hashmap
#     - check equality and append them 
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) < 2:
            return [strs]
        
        hashmap = defaultdict(list)
        for i in strs:
            key = tuple(sorted(i))
            hashmap[key].append(i)
        return list(hashmap.values())
        