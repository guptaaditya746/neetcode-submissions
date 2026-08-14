class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        
        # Start from the second-to-last day and go backwards to 0
        for i in range(n - 2, -1, -1):
            j = i + 1
            
            while j < n:
                if temperatures[j] > temperatures[i]:
                    # We found a warmer day!
                    result[i] = j - i
                    break
                elif result[j] == 0:
                    # Day j is colder, AND day j has no warmer days after it.
                    # This means day i also has no warmer days after it.
                    break
                else:
                    # Day j is colder, so jump directly to the next warmer day for j
                    j += result[j]
                    
        return result