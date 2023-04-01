class Solution:
    def defangIPaddr(self, address: str) -> str:
        final =''
        for j,i in enumerate(address.split(".")):
            if j == len(address.split("."))-1:
                final+=i
            else:
                final+=i + '[.]'
        return final
            