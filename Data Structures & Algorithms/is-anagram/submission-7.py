class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter_s = {}
        counter_t = {}
        for char in s:
            if char in counter_s.keys():
                counter_s[char] += 1
            else:
                counter_s[char] = 1
        
        for char in t:
            if char in counter_t.keys():
                counter_t[char] += 1
            else:
                counter_t[char] = 1

        if counter_s == counter_t:
            return True
        
        return False

        