class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counter_s = {}

        for char in s:
            counter_s[char] = counter_s.get(char,0) + 1

        for char in t:
            if char not in counter_s:
                return False

            counter_s[char] -= 1

            if counter_s[char] < 0:
                return False

        return True



        