class Solution:
    def sortSentence(self, s: str) -> str:
        mapping_dict = {i[-1]:i[:len(i)-1] for i in s.split()}
        res = []
        for i in range(1,len(mapping_dict)+1):
            res.append(mapping_dict[str(i)])
        return ' '.join(res)