from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Counter creates a frequency dictionary automatically
        return Counter(s) == Counter(t)