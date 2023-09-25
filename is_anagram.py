class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counter_s = {}
        counter_t = {}

        for i in range(len(s)):
            counter_s[s[i]] = 1 + counter_s.get(s[i], 0)
            counter_t[t[i]] = 1 + counter_t.get(t[i], 0)

        if counter_s == counter_t:
            return True

        return False

        # TC is O(n)
        # SC is O(n)
