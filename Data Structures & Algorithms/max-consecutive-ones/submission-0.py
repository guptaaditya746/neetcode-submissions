class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0

        for i in nums:
            if i != 0:
                count = count + 1
            else:
                count = 0
        return count 