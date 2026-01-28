# true if s can be a palindrome after deleting at most one char
# unsure if we can return true if its a palindrome before deleting a char, WE CAN !!!!!

# if palindrome
    # return true
# else:
    # while
        # if left != right
            # ignore each character at a time and check
            # ignoring left
                # if self.remainingCheck(left+1, right, s)
                    # return True
                # don't do anything (cause you have to check ignoring right too)
            # ignoring right
                # if self. remainingCheck(left, right+1, s)
                    # return True
                # return False
        # left +
        # right -


class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1

        if self.isPalindrome(left, right, s):
            return True

        while left < right:
            if s[left] != s[right]:
                # ignoring characters
                # ignoring left
                if self.isPalindrome(left+1, right, s):
                    return True
                # else we ignore it for now
                # ignoring right
                if self.isPalindrome(left, right-1, s):
                    return True
                return False
            left += 1
            right -= 1

    def isPalindrome(self, left, right, s):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        
        return True