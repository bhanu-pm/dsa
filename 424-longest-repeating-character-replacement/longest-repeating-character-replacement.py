# given s string and k int
# k replacements possible
# validity checking should take only O(1)
# return length of longest possible substring with k replacements
# dynamic sliding window

# count = dict()
# max_len = -1
# i=0, j=1
# for j in range(len(s))
    # add j to count
    # while invalid????????:
        # shrink
        # decrease i's count from count dict
        # move i to right
    # max_len = max(max_len, j-i)
# return max_len

# invalid condition 
    # lenofSubstring - max(count.values) <= k for validity
    # lenSS - max(count.values) > k for invalidity condition

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = len(s)
        if k > l:
            return l
        count = dict()
        max_len = 0
        i = 0
        for j in range(l):
            if s[j] in count:
                count[s[j]] += 1
            else:
                count[s[j]] = 1
            while (j-i+1) - max(count.values()) > k:
                count[s[i]] -= 1
                i+=1
            max_len = max(max_len, j-i+1)
        return max_len