class Solution:
    def isPalindrome(self, s: str) -> bool:
        # clean it up
        cleaned_str = ""
        for char in s:
            if char.isalnum():
                cleaned_str += char.lower()

        # cheater solution with builtin
        # if cleaned_str != cleaned_str[::-1]:
        #    return False

        char_list = [*cleaned_str]
        l = 0
        r = len(char_list) - 1

        while l < r:
            if char_list[l] != char_list[r]:
                return False

            l += 1
            r -= 1

        return True
