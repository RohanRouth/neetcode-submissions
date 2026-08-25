class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = {}

        for word in strs:
            sortd = "".join(sorted(word))
            if sortd in count:
                count[sortd].append(word)
            else:
                count[sortd] = [word]

        return list(count.values())

        