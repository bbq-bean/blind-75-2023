class Solution:
    def maxArea(self, height: List[int]) -> int:
        # brute force
        #most_agua = 0
        #for i in range(len(height)):
        #    for j in range(i + 1, len(height)):
        #        min_agua = min(height[i], height[j])
        #        width_agua = j - i
        #        curr_agua = min_agua * width_agua
        #
        #        most_agua = max(most_agua, curr_agua)
        #
        l = 0
        r = len(height) - 1

        most_agua = 0

        while l < r:
            min_agua = min(height[l], height[r])
            width_agua = r - l
            curr_agua = min_agua * width_agua

            most_agua = max(most_agua, curr_agua)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return most_agua
