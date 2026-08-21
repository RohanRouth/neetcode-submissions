class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        freq_map = {}
        res = 0

        for r in range(len(s)):
            if s[r] in freq_map.keys():
                freq_map[s[r]] += 1
            else:
                freq_map[s[r]] = 1
            while (r-l+1) -  max(freq_map.values()) > k:
                freq_map[s[l]] -= 1
                l += 1
                

            res = max(res, r-l +1)
        return res

