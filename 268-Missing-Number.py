class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        for index, i in enumerate(sorted(nums)):
            if index != i:
                return index
        return index + 1
            
            