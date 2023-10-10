class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # find all unique triplets with sum of 0
        # brute force
        ans = []
        some_list = nums
        for i in range(len(some_list)):
            for j in range(i + 1, len(some_list)):
                for k in range(j + 1, len(some_list)):
                    if some_list[i] + some_list[j] + some_list[k] == 0 \
                            and i != j and j != k and k != i:
                        curr = sorted(
                            [some_list[i], some_list[j], some_list[k]])
                        if curr not in ans:
                            ans.append(curr)

        return ans
