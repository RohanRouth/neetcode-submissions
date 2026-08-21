

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict1 = {}

        for n in nums:
            if n in dict1:
                dict1[n] +=1
            else:
                dict1[n] = 1
        
        for k,v in dict1.items():
            if v>1:
                return True

        return False

         