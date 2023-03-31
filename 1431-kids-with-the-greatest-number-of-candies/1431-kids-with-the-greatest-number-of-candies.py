class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        total_candies = max(candies)
        bool_list=[]
        for i in candies:
            if (i+extraCandies) >= total_candies:
                bool_list.append(True)
            else:
                bool_list.append(False)
        return bool_list