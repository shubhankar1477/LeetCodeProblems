class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r_count = 0
        l_count = 0
        w_count = 0
        for char in s:
            if char == 'R':
                r_count+=1
            elif char == 'L':
                l_count += 1
            if r_count == l_count:
                w_count+=1
        return w_count
                
        