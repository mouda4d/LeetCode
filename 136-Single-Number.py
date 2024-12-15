class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # dict = {}
        # for i in nums:
        #     #print(i)
        #     if i in dict:
        #         dict[i] += 1
        #     else:
        #         dict[i] = 1 
        # print(dict)
        # print(dict.values())
        # for j, k in dict.items():
        #     if k == 1:
        #         return j
        for i in nums:
            if nums.count(i) == 1:
                return i
