class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        max_now = 0
        current = 0
        for i in range(len(nums)):
            temp_sum = 0

            for j in range(0,i):
                temp_sum +=  nums[j]
                if temp_sum > max_now:
                        current = (j-i+1)
                        max_now = temp_sum
        

        return current