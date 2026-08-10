import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()

        sorted_queries = sorted((q, i) for i, q in enumerate(queries))

        result = [-1] * len(queries)
        heap = []

        i = 0

        for q, original_index in sorted_queries:

            # Add intervals that could contain q
            while i < len(intervals) and intervals[i][0] <= q:
                start, end = intervals[i]
                length = end - start + 1

                # store length and end
                heapq.heappush(heap, (length, end))
                i += 1

            # Remove intervals that ended before q
            while heap and heap[0][1] < q:
                heapq.heappop(heap)

            # Smallest valid interval
            if heap:
                result[original_index] = heap[0][0]

        return result