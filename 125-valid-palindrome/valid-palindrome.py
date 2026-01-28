# all in lowercase, remove non-alphanum chars
    # then should be a palindrome

# given input string
    # return bool if palindrome or not

###########################################

# first turn to lowercase
# remove non-alphanum chars
    # rebuild string w only alphanum chars
# use two pointers starting at each end and move inwards
    # if not equal
        # return false
# return true

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        final_list = []

        for i in s:
            if i.isalnum():
                final_list.append(i)

        left = 0
        right = len(final_list)-1

        while left < right:
            if final_list[left] != final_list[right]:
                return False
            left += 1
            right -= 1
        
        return True