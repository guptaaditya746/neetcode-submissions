class WordDictionary:

    def __init__(self):
        # Dictionary to store child Trie nodes
        self.children = {}

        # Marks whether a complete word ends at this node
        self.is_end = False

    def addWord(self, word: str) -> None:
        # Start from the root node
        node = self

        # Go through every character in the word
        for char in word:

            # If the character does not exist,
            # create a new Trie node
            if char not in node.children:
                node.children[char] = WordDictionary()

            # Move to the next node
            node = node.children[char]

        # Mark the last node as the end of a word
        node.is_end = True

    def search(self, word: str) -> bool:

        # DFS is needed because "." can represent any character
        def dfs(index, node):

            # If we checked every character,
            # return True only if this is the end of a stored word
            if index == len(word):
                return node.is_end

            char = word[index]

            # "." can match any single character
            if char == ".":

                # Try every possible child node
                for child in node.children.values():

                    # If any path successfully matches,
                    # return True
                    if dfs(index + 1, child):
                        return True

                # No child path matched
                return False

            # For a normal character,
            # it must exist in the current node's children
            if char not in node.children:
                return False

            # Continue searching from the matching child
            return dfs(index + 1, node.children[char])

        # Start DFS from index 0 and the root node
        return dfs(0, self)