from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for i in nums:
            temp = max(i + rob1, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2

if __name__ == "__main__":
    s = Solution()
    res = s.rob([1,2,3,1])
    print(res)
