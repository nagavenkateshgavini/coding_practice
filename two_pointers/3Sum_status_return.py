def find_sum_of_three(nums, target):
   nums.sort()
   for i in range(len(nums)):
      left = i+1
      right = len(nums) - 1
      while left < right:
         _sum = nums[i] + nums[left] + nums[right]
         if _sum == target:
            return True

         if _sum > target:
            right -= 1
         
         if _sum < target:
            left += 1
   return False