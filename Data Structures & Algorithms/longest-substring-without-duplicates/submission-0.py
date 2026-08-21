class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        l = 0

        size = 0

        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1

            char_set.add(s[r])
            size = max(size,r-l+1)


        
    
        return size

        # char_set = set()
        # left = 0  # Left pointer of the sliding window
        # max_length = 0  # Maximum length of substring found so far

        # for right in range(len(s)):
        #     # If the character is already in the set, remove characters from the left
        #     while s[right] in char_set:
        #         char_set.remove(s[left])
        #         left += 1
        #     # Add the current character to the set
        #     char_set.add(s[right])
        #     # Update the maximum length if necessary
        #     max_length = max(max_length, right - left + 1)
        
        # return max_length
