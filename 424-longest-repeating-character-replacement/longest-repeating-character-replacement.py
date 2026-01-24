# dynamic sliding window
# arr to maintain counts of all letters
# loop through count arr to find most frequent letter
# track max_len of substring
# window is valid, if, window size - most freq char count <= k
    # i.e total stray char count <= k

# while right < len(s):
    # if window valid
        # check and update max_len accordingly
        # increment right pointer
        # increment count of char at right pointer
    # else
        # decrease count of left pointer char
        # increment left pointer
# return max_len

# for right in range len(s):
    # increment right char count
    # while invalid
        # shrink
        # s[left] -= 1
        # left += 1
    # update max_len
    

# one edge case is when 

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        count = {key:0 for key in letters}
        max_len = float('-inf')
        left = 0
        right = 0

        len_s = len(s)
        for right in range(len_s):
            count[s[right]] += 1
            # while invalid shrink
            while (right-left+1-self._max(count)) > k:
                count[s[left]] -= 1
                left += 1
            max_len = max(max_len, right-left+1)
                
        return max_len

    def _max(self, count):
        max_count = 0
        for i in count.keys():
            if count[i] > max_count:
                max_count = count[i]
        return max_count
