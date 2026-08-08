from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                # minimum is on the right side
                left = mid+1
            else:
                # minimum is at mid or on the left side
                right = mid

        return nums[left]