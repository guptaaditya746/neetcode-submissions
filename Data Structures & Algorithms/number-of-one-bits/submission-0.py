class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        for i in range(n):
            if i is 1:
                count += 1
            
        return count