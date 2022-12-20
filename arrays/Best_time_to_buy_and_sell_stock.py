from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]
        for idx, price in enumerate(prices[1:], 1):
            current_diff = price - min_price
            if current_diff > max_profit:
                max_profit = current_diff

            if price < min_price:
                min_price = price

        return max_profit

if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([7,1,5,3,6,4]))
