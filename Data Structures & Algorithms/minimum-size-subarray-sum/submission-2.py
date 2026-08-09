class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        current = float("inf")

        for i in range(len(nums)):
            temp_sum = 0

            for j in range(i, len(nums)):
                temp_sum += nums[j]

                if temp_sum >= target:
                    current = min(current, j - i + 1)
                    break

        return current if current != float("inf") else 0