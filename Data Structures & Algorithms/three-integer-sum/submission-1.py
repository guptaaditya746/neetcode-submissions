class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # 1. Sort the array first! This is required for the two-pointer approach.
        nums.sort()
        
        result = []

        # 2. Iterate through the array. 
        # We can stop at len(nums) - 2 because we need at least 3 numbers.
        for i in range(len(nums) - 2):
            
            # 3. Skip duplicate 'i' values to prevent duplicate triplets in our result
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # Set our goal and pointers
            item = nums[i]
            goal = 0 - item
            left = i + 1
            right = len(nums) - 1

            while left < right:
                current_sum = nums[left] + nums[right]
                
                if current_sum == goal:
                    # We found a match! Append the VALUES, not indices.
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # 4. Skip duplicate 'left' and 'right' values
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                        
                    # 5. Move both pointers inward to look for the next pair
                    left += 1
                    right -= 1
                    
                # If sum is too big, decrease the right pointer
                elif current_sum > goal:
                    right -= 1
                    
                # If sum is too small, increase the left pointer
                else:
                    left += 1

        return result