from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # defaultdict(list) automatically creates an empty list for new keys
        anagram_map = defaultdict(list)
        
        for s in strs:
            # Sort the string to create a consistent key (e.g., 'tea' -> 'aet')
            signature = "".join(sorted(s))
            
            # Group the original string into that signature's list
            anagram_map[signature].append(s)
            
        # Return all the grouped lists
        return list(anagram_map.values())