class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        set_list = set(nums)
        longest = 0

        for num in set_list:
        # [100, 4, 250, 1, 3, 2]
            # is 100 - 1 in the set?
            # if not, we are at the beginning of a streak
            # notice the 2nd while loop only runs if a "beginning" of a streak is found
            if num - 1 not in set_list:
                current_num = num
                streak = 1

                # now we look to see how far the streak might go
                while current_num + 1 in set_list:
                    current_num += 1
                    streak += 1

                longest = max(longest, streak)

        return longest
