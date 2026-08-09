class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        nums_dict = {}

        for num in nums:

            if num in nums_dict:
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1
        
        ## arrange nums_dict accoring to desceing order .and return keys of values which is equal or higher than k 

        # if  
        return nums_dict.items()