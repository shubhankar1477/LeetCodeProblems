class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        left = 0
        right =  1
        nums.sort()
        print(nums)
        while right < len(nums):
            if nums[left] == nums[right]:
                return True
            left+=1
            right+=1
        return False