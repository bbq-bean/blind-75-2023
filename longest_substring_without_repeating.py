class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = set()
        l = 0
        max_sub = 0
        # a b c a b c b b
        # p w w k e w
        '''
        why remove the leftmost until r is gone?
        because it has to be contiguous. r is whats 
        causing the double letter. so we have to keep
        removing from the left until its gone.
        there are no substrings we might delete that
        *we havent already counted*
        '''
        for r, char in enumerate(s):
            while char in substring:
                substring.remove(s[l])
                l += 1

            substring.add(char)
            max_sub = max(max_sub, r - l + 1)

        return max_sub
