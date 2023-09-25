class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seent = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in seent:
                return [i, seent[diff]]

            seent[num] = i
