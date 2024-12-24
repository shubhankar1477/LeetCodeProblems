class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        i = 0
        longest_string = len(word1) if len(word1) > len(word2) else len(word2)

        while i <= longest_string:
            if i < len(word1):
                result+=word1[i]
                
            if i < len(word2):
                result+=word2[i]

            i+=1
        return result
