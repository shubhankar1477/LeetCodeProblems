class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        candies_ = [i+extraCandies for i in candies]
        bool_list = []
        for i in candies_:
            if  i >= max(candies):
                bool_list.append(True)
            else:
                bool_list.append(False)
        return bool_list