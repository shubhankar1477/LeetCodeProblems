class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        count_mapping = {}
        for value in nums:
            if value not in count_mapping:
                count_mapping[value] = 0
            count_mapping[value]+=1
        return [key for key , value in count_mapping.items() if value == 1 ][0]
        
        