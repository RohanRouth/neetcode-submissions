class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indxmap = {}
        for i,v in enumerate(nums):
            complement = target - v
            print(v, complement)
            if complement in indxmap:
                return sorted([i,indxmap[complement]])
            indxmap[v] = i 
            
        # for i in nums:
        #     complement = target - i
        #     if complement in indxmap and indxmap[complement] != indxmap[i]:
        #         return sorted([indxmap[i],indxmap[complement]] )