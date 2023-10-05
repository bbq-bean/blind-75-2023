class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # brute force
        # profit = 0
        # for i in range(len(prices)):
        #    for j in range(i + i, len(prices)):
        #        curr_profit = prices[j] - prices[i]
        #        profit = max(profit, curr_profit)

        profit = 0
        l = 0
        r = 1

        while r < len(prices):
            curr_profit = prices[r] - prices[l]
            profit = max(curr_profit, profit)

            if prices[r] < prices[l]:
                l = r
                r = l + 1
            else:
                r += 1

        return profit
