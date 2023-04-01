class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        if original not in nums:
            return original
        else:
            original = original * 2
            return self.findFinalValue(nums,original)
        