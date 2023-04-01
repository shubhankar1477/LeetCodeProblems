class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        mydict = dict()
        for k, v in enumerate(sorted(nums)):
            if v not in mydict:
                mydict[v] = k
        return [mydict[item] for item in nums]
        