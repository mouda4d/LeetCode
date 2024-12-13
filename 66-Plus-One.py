class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for num in range(len(digits) -1, -1, -1):
            if digits[num] != 9:
                digits[num] += 1
                return digits
            digits[num] = 0
        digits.insert(0, 1)
        return digits
            
            

# 10**0 + 10**1 + 10**2 + 10**3