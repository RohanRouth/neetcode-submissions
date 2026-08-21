class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = {}
        for num in nums:
            if num in counter.keys():
                counter[num] += 1
            else:
                counter[num] = 1
        
        for k in counter.keys():
            if counter[k] > 1:
                return True
            
        return False

            

            
       
