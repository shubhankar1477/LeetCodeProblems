class Solution:
    def atoi(self,s):
        rtr=0
        for c in s:
            rtr=rtr*10 + ord(c) - ord('0')

        return rtr
    def multiply(self, num1: str, num2: str) -> str:
        num1 = self.atoi(num1)
        num2 = self.atoi(num2)
        num3 = num1 * num2
        return str(num3)