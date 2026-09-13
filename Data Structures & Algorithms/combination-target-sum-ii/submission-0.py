class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []

        candidates.sort()

        def explore(start, path, current_sum):

            # 1. too large -> stop
            if current_sum > target:
                return path

            # 2. exactly target -> save path

            if current_sum == target:
                results.append(path[:])
                return path
            for i in range(start, len(candidates)):

                # 3. skip duplicate choice at the same recursion level

                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                    
                else:
                    path.append(candidates[i])

                    explore(i+1, path, current_sum + candidates[i])

                    path.pop()

                # 4. choose


                # 5. explore
                # important: use i + 1 because each element can be used once


                # 6. undo


        explore(0, [], 0)
        return results