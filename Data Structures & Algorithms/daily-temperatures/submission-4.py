class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Pre-fill the result array with 0s. 
        # Now we only need to update it when we find a warmer day.
        result = [0] * len(temperatures)
        
        # The stack will store the INDICES of the temperatures, not the temperatures themselves.
        stack = [] 
        
        for i, current_temp in enumerate(temperatures):
            # While the stack is not empty AND the current day is warmer 
            # than the temperature at the index stored at the top of the stack
            while stack and current_temp > temperatures[stack[-1]]:
                prev_index = stack.pop()
                # Calculate how many days have passed
                result[prev_index] = i - prev_index
            
            # Add the current day's index to the stack to wait for a warmer day
            stack.append(i)
            
        return result