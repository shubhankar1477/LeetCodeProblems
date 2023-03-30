class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result=[]
        first_list = nums[:n]
        second_list = nums[n:]
        for fst, sd in zip(first_list,second_list):
            result.extend([fst,sd])
        return result