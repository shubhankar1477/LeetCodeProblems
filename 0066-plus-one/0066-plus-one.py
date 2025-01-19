class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        carry , start_index = 1,0

        while carry:
            if start_index < len(digits):
                if digits[start_index] == 9:
                    digits[start_index] = 0 
                else:
                    digits[start_index] +=1
                    carry = 0
            else:
                digits.append(1)
                carry = 0
            start_index +=1
        return digits[::-1]

        # int_ = int(''.join(str(i) for i in digits))
        # new_number = int_ + 1
        # return [int(i) for i in str(new_number)]
