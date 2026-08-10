from collections import Counter
from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Step 1: Count how many 0s, 1s, and 2s exist
        nums_hash = Counter(nums)
        
        # Step 2: Overwrite the original 'nums' array in-place
        # We need to ensure we insert them in order: 0, then 1, then 2.
        index = 0
        
        for color in [0, 1, 2]:
            count = nums_hash[color] # Check how many times this color appeared
            
            # Write the color into the array 'count' times
            for _ in range(count):
                nums[index] = color
                index += 1