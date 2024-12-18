class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique_set = set()

        for i in range(len(nums)):
            if nums[i] in unique_set:
                return True
            unique_set.add(nums[i])
        return False
        