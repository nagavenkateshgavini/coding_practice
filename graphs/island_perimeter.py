from typing import List


class Solution:
    def __init__(self):
        self.res = 0
        self.visited = set()

    def islandPerimeter(self, grid: List[List[int]]) -> int:

        def traverse(i, j):
            if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or grid[i][j] == 0:
                return 1
            if (i, j) in self.visited:
                return 0
            
            self.visited.add((i, j))

            self.res = traverse(i+1, j)
            self.res += traverse(i, j+1)
            self.res += traverse(i, j-1)
            self.res += traverse(i-1, j)

            return self.res

        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return traverse(i, j)


if __name__ == "__main__":
    s = Solution()
    print(s.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))
