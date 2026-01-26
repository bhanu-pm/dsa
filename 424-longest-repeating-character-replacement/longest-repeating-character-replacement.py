# 26 possible english uppercase characters
# no. of switches <= k
# need the longest valid substring's length
# what is valid? -> substring length - most occurences of single character <= k

# dynamic subwindow
# need a dict of 26 Uppercase english letters, to track counts, count
# track max_len

# for right loop
    # count[right] +1

    # while substr len - max_count > k: (non-validity condition)
        # count[left] -1
        # left += 1
    
    # max_len = max (maxlen, current len)
# return max_len

# time complex, O(26*N), 26 to find max_count in the count dict
# O(1) space complexity, cause count dict fixed size, other variables

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = float('-inf')
        alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        count = {key:0 for key in alph}
        left = 0

        for right in range(len(s)):
            count[s[right]] += 1

            while (right-left+1 - max(count.values())) > k:
                count[s[left]] -= 1
                left += 1
            
            max_len = max(max_len, right-left+1)
        
        return max_len