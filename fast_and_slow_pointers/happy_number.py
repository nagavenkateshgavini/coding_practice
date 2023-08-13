class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_of_squares(num) -> int:
            sum = 0
            while num:
                digit = num % 10
                sum += digit ** 2
                num = num//10

            return sum
        
        slow = n
        fast = n
        while True:
            slow = sum_of_squares(slow)
            fast = sum_of_squares(sum_of_squares(fast))
            
            if slow == fast:
                break
        
        return (slow == 1)
            

    
