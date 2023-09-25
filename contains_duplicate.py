class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seent = {}
        for num in nums:
            if num in seent:
                return True
            seent[num] = 1
