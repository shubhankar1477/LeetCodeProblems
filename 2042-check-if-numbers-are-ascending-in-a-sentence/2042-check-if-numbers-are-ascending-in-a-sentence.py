class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        numbers = [int(i) for i in s.split() if i.isalpha() ==False]
        flag = True
        for  i in range(1,len(numbers)):
            if flag:
                j=i-1
                if numbers[j] < numbers[i]:
                    flag = True
                else:
                    flag = False
            else:
                break
        return flag    