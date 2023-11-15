class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        words = [i for i in words if len(i) > 0]
        
        return ' '.join(list(reversed(words)))
        
        