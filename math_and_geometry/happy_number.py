class Solution:
    def sum_of_squares(self, n):
        op = 0
        while n:
            d = n % 10
            op += d ** 2
            n = n // 10
        return op

    def isHappy(self, n: int) -> bool:
        calc_nums = set()

        while n not in calc_nums:
            calc_nums.add(n)
            n = self.sum_of_squares(n)

            if n == 1:
                return True

        return False

if __name__ == "__main__":
    s = Solution()
    print(s.isHappy(19))
