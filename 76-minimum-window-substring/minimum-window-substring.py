# min substring of S, such that every char in T (including duplicates) is included
# valid? every char in t should be in window
# if no soln, return ""
# so len(s) >= len(t)
# dynamic subwindow
# return the minimum substring

# track char counts in substring, wcount
# track char counts in t string, tcount
# track min_str
# track min_str_len

# for right < len(s)
    # wcount[s[right]] += 1
    
    # while valid: what is valid -> window should have all chars of t, with counts
        # if min_str_len > window_size:
            # update min_str_len
            # update min_str
        # decrement window size

# return min_str

# time complex, O(N*M)
# space complex, O(N+M)

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        wcount = dict()
        tcount = dict()
        left = 0
        min_str = ""
        min_str_len = float('inf')

        # build tcount
        for i in t:
            if i in tcount:
                tcount[i] += 1
            else:
                tcount[i] = 1
        
        need = len(tcount)
        have = 0

        for right in range(len(s)):
            if s[right] in wcount:
                wcount[s[right]] += 1
            else:
                wcount[s[right]] = 1
            
            if s[right] in tcount:
                if wcount[s[right]] == tcount[s[right]]:
                    have += 1

            while need == have: # all chars of tcount should be in wcount
                if min_str_len > (right-left+1):
                    min_str_len = right-left+1
                    min_str = s[left:right+1]
                left_char = s[left]
                wcount[s[left]] -= 1

                if left_char in tcount and (wcount[left_char] < tcount[left_char]):
                    have -= 1
                left += 1
        
        return min_str
    