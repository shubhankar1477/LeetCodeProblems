class Solution:
    def convert(self, s):
        converted = ""
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for char in s:
            converted += str(alphabet.index(char) + 1)
        return converted
    def getSum(self, converted):
        result = 0
        for char in str(converted):
            result += int(char)
        return str(result)
    def getLucky(self, s: str, k: int) -> int:
        converted = self.convert(s)
        result = converted
        for i in range(k):
            result = self.getSum(result)
        return int(result)

            
    