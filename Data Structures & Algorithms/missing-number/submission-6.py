class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        nums.sort()
        
        # 1. If 0 is missing, return 0
        if nums[0] != 0:
            return 0
            
        # 2. Check for a gap in the middle
        for i in range(len(nums)):
            if nums[i] != i:
                return i
                
        # 3. If no gaps were found, the missing number is at the very end
        return len(nums)