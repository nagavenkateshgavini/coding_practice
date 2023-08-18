from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq = deque()
        output = []
        
        # First window
        for i in range(k):
            while deq and nums[i] > deq[-1]:
                deq.pop()
            deq.append(nums[i])
        output.append(deq[0])
        
        # Rest of the windows
        for i in range(k, len(nums)):
            while deq and nums[i] > deq[-1]:
                deq.pop()
            deq.append(nums[i])
            
            # check whether first element of queue is out of window or not
            if deq[0] == nums[i-k]:
                deq.popleft()
                
            output.append(deq[0])

        return output
