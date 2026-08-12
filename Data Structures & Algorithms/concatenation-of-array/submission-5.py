class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return list(chain(nums, nums))