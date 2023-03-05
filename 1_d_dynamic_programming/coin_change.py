from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        size = amount + 1
        res = [amount+1] * size
        res[0] = 0
        for change_number in range(1, amount+1):
            for coin in coins:
                if change_number - coin >= 0:
                    res[change_number] = min(res[change_number], 1 + res[change_number - coin])
        
        return res[amount] if res[amount] != amount + 1 else -1

if __name__ == "__main__":
    s = Solution()
    s.coinChange([1, 2, 5], 11)
