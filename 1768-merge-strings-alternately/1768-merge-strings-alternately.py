class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged_str=''
        len_word1 = len(word1)
        len_word2 = len(word2)
        long_len = len_word1 if len_word1 > len_word2 else len_word2
        for i in range(0,long_len):
            if i < (len_word1):
                merged_str+=word1[i]
            if i < (len_word2): 
                 merged_str+=word2[i]
        return merged_str
    