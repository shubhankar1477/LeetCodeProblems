class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        int_ = int(''.join(str(i) for i in digits))
        new_number = int_ + 1
        return [int(i) for i in str(new_number)]
