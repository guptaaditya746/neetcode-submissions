class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        # ans = 2*len(nums)
        ans = nums
        for i in range(len(nums)):
            # print(i)
            ans.append(nums[i])
            
        return ans