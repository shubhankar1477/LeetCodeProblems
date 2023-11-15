class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a' , 'e' ,'i' ,'o' ,'u' , 'A' ,'E' ,'I' ,'O' ,'U']
        vowels_list = [i for i in s if i in vowels]
        vowels_list = list(reversed(vowels_list))
        counter = 0
        new_string =''
        for index , value in enumerate(s):
            if value in vowels:
                new_string += vowels_list[counter]
                counter+=1
            else:
                new_string+=value
                
        return new_string