from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        

        ## edge case if not return ""
        ## if all the values 
        count_s = {}
        count_t = {}
        for c in s:
            count_s[c] = count.get(c, 0) + 1
        for c in t :
            count_t[c] = count.get(c, 0) + 1
        

        for x in count_t:
            if count_t[x] - count_s.get(x) != 0 : 
                return False
        


        ## now we know that t is subset of s , sliding widnow
        for min_wind_size in range(len(s)):
            for i in range(len(s)-min_wind_size+1):
                if Counter(s[i:min_wind_size]) == count_t:
                    return s[i:min_wind_size]
                
             