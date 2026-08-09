from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        count_s = Counter(s)
        count_t = Counter(t)

        # Edge case: s does not contain enough characters for t
        for x in count_t:
            if count_s.get(x, 0) < count_t[x]:
                return ""

        # Try windows from smallest size to largest
        for min_wind_size in range(len(t), len(s) + 1):

            window_count = Counter(s[0:min_wind_size])

            for i in range(len(s) - min_wind_size + 1):

                # Check whether current window satisfies t
                for x in count_t:
                    if window_count.get(x, 0) < count_t[x]:
                        break
                else:
                    return s[i:i + min_wind_size]

                # Slide window one position right
                if i + min_wind_size < len(s):
                    window_count[s[i]] -= 1
                    window_count[s[i + min_wind_size]] += 1

        return ""