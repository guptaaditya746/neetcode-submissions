class Solution:

    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:

        # -------------------------
        # Build Trie
        # -------------------------
        trie = {}

        for word in words:
            node = trie

            for char in word:
                if char not in node:
                    node[char] = {}

                node = node[char]

            # Store the complete word at the end
            node["#"] = word

        rows = len(board)
        cols = len(board[0])

        result = []

        # -------------------------
        # DFS / Backtracking
        # -------------------------
        def dfs(row, col, node):

            char = board[row][col]

            # If this character is not in the Trie,
            # there is no word with this path
            if char not in node:
                return

            # Move to the next Trie node
            next_node = node[char]

            # If "#" exists, we found a complete word
            if "#" in next_node:
                result.append(next_node["#"])

                # Remove it so we don't add duplicates
                del next_node["#"]

            # Mark this board cell as visited
            board[row][col] = "#"

            # Check all 4 directions
            directions = [
                (1, 0),   # down
                (-1, 0),  # up
                (0, 1),   # right
                (0, -1)   # left
            ]

            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc

                # Make sure the new position is inside the board
                if (
                    0 <= new_row < rows
                    and 0 <= new_col < cols
                    and board[new_row][new_col] != "#"
                ):
                    dfs(new_row, new_col, next_node)

            # Backtrack:
            # restore the original character
            board[row][col] = char

        # Start DFS from every cell
        for row in range(rows):
            for col in range(cols):
                dfs(row, col, trie)

        return result