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

        for right in range(len(s)):
            if s[right] in wcount:
                wcount[s[right]] += 1
            else:
                wcount[s[right]] = 1

            while self.valid(wcount, tcount): # all chars of tcount should be in wcount
                if min_str_len > (right-left+1):
                    min_str_len = right-left+1
                    min_str = s[left:right+1]
                wcount[s[left]] -= 1
                left += 1
        
        return min_str
    
    def valid(self, wcount: dict, tcount: dict) -> bool:
        for i, j in tcount.items():
            if i not in wcount:
                return False
            if wcount[i] < j:
                return False
        return True