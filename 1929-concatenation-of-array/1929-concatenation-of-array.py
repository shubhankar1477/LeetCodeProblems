class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        list_=nums.copy()
        nums.extend(list_)
        if len(nums) == 2*len(list_):
            return nums
        else:
            return []