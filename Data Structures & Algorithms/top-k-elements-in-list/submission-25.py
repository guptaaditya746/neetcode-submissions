class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        nums_dict = {}
        result =  []
        for num in nums:

            if num in nums_dict:
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1
        
        ## arrange nums_dict accoring to desceing order .and return keys of values which is equal or higher than k 


        pairs = sorted(nums_dict.items(), key=lambda x:x[1], reverse=True)
    

        return print(list(pairs.keys())[0:k])