import copy

class Solution:
    def min_cost(self, cost: "arr"):
        ln = len(cost)
        cost.append(0)
        cost_arr = copy.deepcopy(cost)
        for i in range(ln-3, -1, -1):
            cost_arr[i] += min(cost_arr[i+1], cost_arr[i+2])
        
        return min(cost_arr[0], cost_arr[1])

def main():
    s = Solution()
    cost = [1,100,1,1,1,100,1,1,100,1]
    print(s.min_cost(cost))


if __name__ == "__main__":
    main()
    
# Time: O(n)
# Space: O(n) if we copy the entire array else it will be O(1) if we calculate the cost in place.
