class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1

        one = 1
        two = 1
        for i in range(n-1):
            final_sum = two + one
            one = two
            two = final_sum

        return final_sum


if __name__ == "__main__":
    s = Solution()
    print(s.climbStairs(5))
