class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []

        def explore(start, path, current_sum):

            # if current_sum is too large:
            #     stop this branch
            if current_sum > target:
                return path

            # if current_sum reaches target:
            #     save a copy of path
            #     stop this branch
            if current_sum == target:
                results.append(path[:])
                return path

            for i in range(start, len(candidates)):

                # choose candidate[i]
                path.append(candidates[i])
                explore(i,path, current_sum + candidates[i])

                path.pop()

                # explore again
                # remember: same number can be reused

                # undo choice

        explore(0, [], 0)
        return results