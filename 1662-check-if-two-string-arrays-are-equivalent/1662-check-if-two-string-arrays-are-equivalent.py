class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        if (len(word2) >=1) and (len(word1) >=1):
            joined_word1 = ''.join(word for word in word1)
            joined_word2 = ''.join(word for word in word2)
            if (joined_word1) == (joined_word2):
                return True
            else:
                return False
        else:
            return False
            
        