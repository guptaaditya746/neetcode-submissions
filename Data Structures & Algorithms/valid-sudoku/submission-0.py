class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        blocks = {}

        for i in range(9):
            for j in range(9):
                value = board[i][j]

                if value == ".":
                    continue

                block_key = (i // 3, j // 3)

                if i not in rows:
                    rows[i] = set()
                if j not in cols:
                    cols[j] = set()
                if block_key not in blocks:
                    blocks[block_key] = set()

                if value in rows[i]:
                    return False
                if value in cols[j]:
                    return False
                if value in blocks[block_key]:
                    return False

                rows[i].add(value)
                cols[j].add(value)
                blocks[block_key].add(value)

        return True