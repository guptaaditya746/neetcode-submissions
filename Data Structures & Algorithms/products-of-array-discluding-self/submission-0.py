class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = []

        for i in range(len(nums)):
            if i == 0:
                left[i] = 1
            else:
                lett[i] = left[i-1]
        

        return print(left)