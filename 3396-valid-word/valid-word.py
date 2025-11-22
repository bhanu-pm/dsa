class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        
        vowels = set("aeiouAEIOU")
        seen_vowel = False
        seen_consonant = False

        for char in word:
            if not char.isalnum():
                return False
            
            if char.isalpha():
                if char in vowels:
                    seen_vowel = True
                else:
                    seen_consonant = True
        
        if seen_vowel and seen_consonant:
            return True
        else:
            return False