class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            
        l, r = 0, len(nums) - 1
        i = 0
        while i <= r:
            if nums[i] == 0:
                swap(l, i)
                l += 1

            elif nums[i] == 2:
                swap(i, r)
                r -= 1
                i -= 1 # when i is 2, i don't need to move forward because the swapped number can be a zero
            i += 1
            
        