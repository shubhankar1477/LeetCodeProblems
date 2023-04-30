class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        count=0
        letters = 'abcdefghijklmnopqrstuvwxyz'
        for char in letters:
            if char not in sentence:
                return False
            else:
                count+=1
        if count > 1:
            return True
            
                
        