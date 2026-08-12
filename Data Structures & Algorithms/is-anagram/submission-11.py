class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set_s = {}
        set_t = {}


        for i in s:


            set_s[i] = set_s.get(i,0) + 1

        for j in t:

            set_t[j] = set_t.get(j,0) + 1


        return (True if set_s == set_t else False)