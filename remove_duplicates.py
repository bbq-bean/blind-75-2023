class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # left is actually building the list as it moved left to right
        # nums[0] will never need to change because the list is sorted
        L = 1
        # R moves ahead of L, looking for "new" numbers
        # a "new" number is found when a number != the number before it
        # (this is true because the list is already sorted)
        # nums[L] gets the "new" number and R continues to find more
        # the description is confusing, because padding the array with "_"
        # is not required, we can just leave our mess of numbers after L
        # that R was looking at to the end of the array
        # L is also a builtin counter for the number of uniques(the answer)
        for R in range(1, len(nums)):
            if nums[R] != nums[R - 1]:
                nums[L] = nums[R]
                L += 1

        return L
