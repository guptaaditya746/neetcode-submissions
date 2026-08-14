class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        # Iterate through each number, treating it as the first number of our pair
        for i in range(len(numbers)):
            # Calculate the exact value we need to find
            complement = target - numbers[i]
            
            # Start our binary search ONLY in the remaining part of the array
            # This prevents us from using the same element twice
            low = i + 1
            high = len(numbers) - 1
            
            while low <= high:
                # Find the middle index of our search space
                mid = (low + high) // 2
                
                # If we found the complement, return the 1-based indices
                if numbers[mid] == complement:
                    return [i + 1, mid + 1]
                
                # If the middle number is too small, search the right half
                elif numbers[mid] < complement:
                    low = mid + 1
                    
                # If the middle number is too big, search the left half
                else:
                    high = mid - 1
                    
        return []