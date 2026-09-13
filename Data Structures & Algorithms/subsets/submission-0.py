class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []

        def explore(start, path):
            results.append(path[:])

            for i in range(start, len(nums)):
                path.append(nums[i])      # choose
                explore(i + 1, path)      # explore
                path.pop()                # undo

        explore(0, [])
        return results