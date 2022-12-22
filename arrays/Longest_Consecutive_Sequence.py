from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)

        longest_streak = 0
        for n in nums:
            current_streak = 1
            if (n-1) not in num_set:
                current_num = n
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

            longest_streak = max(current_streak, longest_streak)

        return longest_streak

if __name__ == "__main__":
    s = Solution()
    print(s.longestConsecutive([100,4,200,1,3,2]))
