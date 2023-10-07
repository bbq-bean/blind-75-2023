class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # let l be 0 and lets start finding  these vals
        l = 0
        for r in range(len(nums)):
            if nums[r] != val:
                nums[l] = nums[r]
                l += 1

        return l
