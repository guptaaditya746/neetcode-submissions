class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = set()
        groups = 0


        def explore(r, c):
            # 1. boundary check
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return

            # 2. only interested in 1s
            if grid[r][c] != "1":
                return

            # 3. don't process same cell twice
            if (r, c) in visited:
                return

            # this cell belongs to the current group
            visited.add((r, c))

            # explore its neighbors
            explore(r - 1, c)
            explore(r + 1, c)
            explore(r, c - 1)
            explore(r, c + 1)


        # OUTER SCAN
        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == "1" and (r, c) not in visited:
                    groups += 1
                    explore(r, c)
        return groups