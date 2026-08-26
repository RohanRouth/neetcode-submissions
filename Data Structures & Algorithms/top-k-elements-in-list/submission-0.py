class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1


        sorted_items = sorted(count.items(),key= lambda x: x[1], reverse= True)

        final_list = []

        for i in range(k):
            final_list.append(sorted_items[i][0])

        return final_list