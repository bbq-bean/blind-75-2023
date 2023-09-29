class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # O(n)
        length = len(nums)

        left = [1] * length
        right = [1] * length
        ans = [1] * length

        # nums
        # [1,2,3,4]

        # build left
        # [1, 1, 2, 6]
        #     ^  ^  ^
        for i in range(1, length):
            left[i] = nums[i - 1] * left[i - 1]
        print(left)

        # build right
        # [24, 12, 4, 1]
        #   ^   ^  ^
        for i in reversed(range(length - 1)):
            right[i] = nums[i + 1] * right[i + 1]
        print(right)

        # build ans
        for i in range(length):
            ans[i] = left[i] * right[i]

        return ans
