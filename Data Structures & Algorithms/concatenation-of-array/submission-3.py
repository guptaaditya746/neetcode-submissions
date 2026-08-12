class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums.copy()  # Create a real copy first so we don't modify the input
        ans.extend(nums)   # Slaps the second list onto the end in one fast C-level operation
        return ans