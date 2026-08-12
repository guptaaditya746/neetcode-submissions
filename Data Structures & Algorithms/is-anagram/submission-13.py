class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        # Create an array of 26 zeros
        counts = [0] * 26
        
        for i in range(len(s)):
            # ord() gets the ASCII value. ord('a') - ord('a') = index 0
            counts[ord(s[i]) - ord('a')] += 1
            counts[ord(t[i]) - ord('a')] -= 1
            
        # Check if all counts are completely balanced back to 0
        return all(count == 0 for count in counts)