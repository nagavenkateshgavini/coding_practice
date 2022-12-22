class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)
        for idx in range(1, len(nums)):
            answer[idx] = answer[idx-1] * nums[idx-1]

        #the second argument is one less than the final value. so if you put -1 then the range stops at 0, if you put -5, the range stops at -4 (for an increment of -1) 
        right_prod = 1
        for idx in range(len(nums)-1, -1, -1):
            answer[idx] *= right_prod
            right_prod *= nums[idx]
        
        return answer

if __name__ == "__main__":
    s = Solution()
    print(s.productExceptSelf([1, 2, 3, 4]))
