class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # O(log n)
        # lets try dis
        nums.sort()
        # now, if we have 2 nums, we know what the third must be
        ans = []
        for p1 in range(len(nums)):
            # this is how we skip duplicates for p1 in the sorted array
            # eg [-1, -1, 1, 2, 2, 3]
            #                   ^ skip already did it
            if p1 > 0 and nums[p1 - 1] == nums[p1]:
                continue

            # for each iteration, p1 is the curr num
            # and p2 is just + 1 ahead of p1
            # p3 is at the end
            # eg [1, 2, ]
            p2 = p1 + 1
            p3 = len(nums) - 1

            # 2 pointers
            while p2 < p3:
                curr_sum = nums[p1] + nums[p2] + nums[p3]

                # WE FOUND AN ANSWER, APPEND!
                if curr_sum == 0:
                    ans.append([nums[p1], nums[p2], nums[p3]])
                    # but now we have to update our pointers to keep searching for more triplets
                    p2 += 1

                    # condition to just skip duplicates for p2: keep adding +1 until adjacent new numbers not equal
                    while nums[p2] == nums[p2 - 1] and p2 < p3:
                        p2 += 1


                # keep scooching
                elif curr_sum < 0:
                    p2 += 1

                else:
                    p3 -= 1

        return ans
