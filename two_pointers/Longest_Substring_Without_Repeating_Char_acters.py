from typing import List


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        max_count = 0
        left = 0
        for right, char in enumerate(s):
            if char in d:
                left = max(left, d[char] + 1)
            max_count = max(max_count, right - left + 1)
            d[char] = right
                
        return max_count

if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))

# Time Complexity: O(n)
# Space Complexity: O(n)
