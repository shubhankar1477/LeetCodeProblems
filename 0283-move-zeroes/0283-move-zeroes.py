class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums  
        : List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if (len(nums) == 1) and (nums[0] == 0):
            return nums
        else:
            zero_count = nums.count(0)
            # Remove all zeroes from the original list
            nums[:] = [x for x in nums if x != 0]
            # Append zeroes at the end
            nums.extend([0] * zero_count)