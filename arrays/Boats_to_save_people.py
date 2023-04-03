from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people) - 1
        boats = 0
        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
            r -= 1
            boats += 1
        return boats      

if __name__ == "__main__":
    s = Solution()
    b = s.numRescueBoats([3,2,2,1], 3)
    print(b)

