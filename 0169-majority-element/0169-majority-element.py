class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash = {}
        maj , res = 0,0

        for num in nums:
            hash[num] = 1 + hash.get(num,0)
            if hash[num] > maj:
                res = num
                maj = hash[num]
        return res
        