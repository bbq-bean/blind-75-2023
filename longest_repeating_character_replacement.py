class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0

        l = 0
        counter = {}
        for r in range(len(s)):
            # counter is counter for current window
            # while r moves ahead, we build the dict
            counter[s[r]] = 1 + counter.get(s[r], 0)

            # r - l + 1 is current window length
            # minus the MOST seen value in current window
            # if GREATER than k, means theres not enough
            # k to replace the other values and create a uniform substring
            while (r - l + 1) - max(counter.values()) > k:
                # THEREFORE, minus 1 count from whatever char l was on, and move l ahead
                counter[s[l]] -= 1
                l += 1

            # once we get past the above while loop, this means theres enough k to create a uniform substring, so we can check it against max.
            longest = max(r - l + 1, longest)

        return longest
