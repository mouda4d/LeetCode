class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
            1- so the logic is that we keep summing the elements till we find a negative
            2- once we find the negative we compare our current sum to the negative we found
               if the negative is greater then start a new array from that point on
            3- so the simple logic is: iterate over array, drop subarray if -ve > sum
        '''
        sum = 0
        sum2 = 0
        #sum = nums[0] if nums[0] > 0 else 0
        
        for i in range(0, len(nums)):
            #print(nums[i])
            if nums[i] < 0 and abs(nums[i]) > sum:
                sum = 0
                #print(f' check failed, sum reset = {sum}')
            else:
                sum += nums[i]
                #print(f' check passed, sum = {sum}')
                #print(f' check passed, sum2 = {sum2}')

                if sum > sum2:
                    sum2 = sum
                else:
                    pass
        if max(nums) < 0:
            return max(nums)
        return sum2