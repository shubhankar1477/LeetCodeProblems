class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        
        row1 = int(s[1])
        row2 = int(s[-1])
        
        col1 = s[0]
        col2 = s[3]
        op = []
        for col in range(alpha.index(col1), alpha.index(col2)+1):
            for row in range(row1, row2+1):
                op.append(alpha[col] + str(row))
        return op    
