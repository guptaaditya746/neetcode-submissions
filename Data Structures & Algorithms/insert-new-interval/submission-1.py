class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        for i in range(len(intervals)):
            start, end = intervals[i]
            new_start, new_end = newInterval

            # 1. Current interval is completely before newInterval
            if end < new_start:
                result.append(intervals[i])

            # 2. Current interval is completely after newInterval
            elif start > new_end:
                result.append(newInterval)
                result.extend(intervals[i:])
                return result

            # 3. They overlap, so merge
            else:
                newInterval = [
                    min(start, new_start),
                    max(end, new_end)
                ]

        # newInterval belongs at the end,
        # or intervals was empty
        result.append(newInterval)

        return result