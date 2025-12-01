class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        if len(sentence) < 26:
            return False
        
        for i in "abcdefghijklmnopqrstuvwxyz":
            if i not in sentence:
                return False
        return True