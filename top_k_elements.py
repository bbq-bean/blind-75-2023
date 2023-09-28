class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # brute force
        k_counter = {}
        for num in nums:
            k_counter[num] = 1 + k_counter.get(num, 0)

        # the answer
        k_elements = []

        i = k
        # we just want it to run k times
        while i > 0: # I think this is still O(n)
            largest_count = 0
            for key, val in k_counter.items():
                # this will always match at least once
                if val > largest_count:
                    largest_count = val
                    largest_key = key

            k_elements.append(largest_key)
            del k_counter[largest_key]

            i -= 1

        return k_elements