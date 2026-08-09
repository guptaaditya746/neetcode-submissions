from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        mind_wind_size = len(t)

    
        # count_s = {}
        # count_t = {}
        # for c in s:
        #     count_s[c] = count_s.get(c, 0) + 1
        # for c in t :
        #     count_t[c] = count_t.get(c, 0) + 1
        count_s = Counter(s)
        count_t = Counter(t)

        for x in count_t:
            if count_s.get(x, 0) - count_t[x]   < 0 : 
                return ""
        


        ## now we know that t is subset of s , sliding widnow
        for min_wind_size in range(len(t), len(s) + 1):
            window_count = Counter(s[0:min_wind_size])
            
            for i in range(len(s)-min_wind_size+1):

                for x in count_t:
                    
                    if window_count.get(x,0) < count_t[x]:
                        break
                else:   
                    return s[i:min_wind_size+i]
                
                if i + min_wind_size < len(s):
                    window_count[s[i]] -= 1
                    window_count[s[i+min_wind_size]] += 1
        return ""