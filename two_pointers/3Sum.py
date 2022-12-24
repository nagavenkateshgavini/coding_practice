from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for idx, n in enumerate(nums):
            if idx > 0 and nums[idx - 1] == nums[idx]:
                continue
            
            low = idx + 1
            high = len(nums) - 1
            while low < high:
                threeSum = nums[idx] + nums[low] + nums[high]
                if threeSum > 0:
                    high -= 1
                elif threeSum < 0:
                    low += 1
                else:
                    res.append([nums[idx], nums[low], nums[high]])
                    low += 1
                    while nums[low] == nums[low - 1] and low < high:
                        low += 1

        return res

if __name__ == "__main__":
    s = Solution()
    print(s.threeSum([-1,0,1,2,-1,-4]))

# Time: O(logn) + O(n^2) = O(n^2)
# Space: O(n) for sorting
