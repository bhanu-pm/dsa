# longest ss containing only unique chars
# dynamic subwindow
# track max_len
# track exist in a dict

# for right in range(len(s))
    # exist[right] = 1
    # while invalid:
        # decrement left
    # max_len = max(...)
# return max_len

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        exist = dict()
        left = 0

        for right in range(len(s)):
            if s[right] in exist:
                exist[s[right]] += 1
            else:
                exist[s[right]] = 1
            
            while max(exist.values()) > 1:
                exist[s[left]] -= 1
                left += 1
            
            max_len = max(max_len, right-left+1)
        
        return max_len