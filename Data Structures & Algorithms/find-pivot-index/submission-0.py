class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        prefix_sum = [0]
        val = 0
        n  = len(nums)
        ## making prefix_sum first 
        for i in nums:
            val = i + val
            prefix_sum.append(val)
        
        for i in range(n):
            sum_left = prefix_sum[i]
            sum_right = prefix_sum[n] - prefix_sum[i+1]
            if sum_left == sum_right:
                return i
        else:
            return -1


        return ""