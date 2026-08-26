class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1


        buckets = [[] for _ in range(len(nums) + 1)]

        for num, key in count.items():
            buckets[key].append(num)

        results = []

        for i in range(len(buckets)-1,0,-1):
            for j in buckets[i]:
                results.append(j)

                if len(results) == k:
                    return results