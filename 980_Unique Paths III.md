# 980. Unique Paths III
## Hard
### Backtracking/Depth-first Seach
#
Relative: 37, 63, 212
#

On a 2-dimensional ```grid```, there are 4 types of squares:

* ```1``` represents the starting square.  There is exactly one starting square.
* ```2``` represents the ending square.  There is exactly one ending square.
* ```0``` represents empty squares we can walk over.
* ```-1``` represents obstacles that we cannot walk over.

Return the number of 4-directional walks from the starting square to the ending square, that **walk over every non-obstacle square exactly once**.

Example1:
> Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
> 
> Output: 2
>
> Explanation: We have the following two paths: 
> 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
> 2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)

Example2:
> Input: [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
> 
> Output: 4
>
> Explanation: We have the following four paths: 
> 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
> 2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
> 3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
> 4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)

Example3:
> Input: [[0,1],[2,0]]
> 
> Output: 0
>
> Explanation: There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.

**Note:** 
* ```1 <= grid.length * grid[0].length <= 20```

**My Note:**
* Typical Backtracking
* Iterate the grid count the #0's
* Find the start and end points
* Do backtracking
* Using a set to keep the visited position

Solution1:
*Time: O(n)*
*Space: O(n)*
```python
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.res = 0
        num_row = len(grid)
        num_col = len(grid[0])
        zero_cnt = 0
        for r in range(num_row):
            for c in range(num_col):
                if grid[r][c] == 0:
                    zero_cnt += 1
                if grid[r][c] == 1:
                    start = (r, c)
                if grid[r][c] == 2:
                    end = (r, c)
        # print(num_row, num_col)
        # print(zero_cnt)
        # print(start, end)
        
        def helper(cur, remain_zero, visited):
            # print(cur, remain_zero)
            if cur == end and remain_zero == 0:
                self.res += 1
                return
            if cur == end or remain_zero == 0:
                return
            x, y = cur
            direction = {(0, 1), (1, 0), (-1, 0), (0, -1)}
            for dx, dy in direction:
                if (x+dx, y+dy) not in visited:
                    if 0 <= x+dx < num_row and 0 <= y+dy < num_col and grid[x+dx][y+dy] != -1:
                        visited.add((x+dx, y+dy))
                        helper((x+dx, y+dy), remain_zero-1, visited)
                        visited.remove((x+dx, y+dy))
                        
        v = set()
        v.add(start)
        helper(start, zero_cnt+1, v)
        return self.res
```

Solution2:
*Time: O(n)*
*Space: O(n)*
```python
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.res = 0
        num_row = len(grid)
        num_col = len(grid[0])
        zero_cnt = 0
        for r in range(num_row):
            for c in range(num_col):
                if grid[r][c] == 0:
                    zero_cnt += 1
                if grid[r][c] == 1:
                    start = (r, c)
                    grid[r][c] = -1
                if grid[r][c] == 2:
                    end = (r, c)

        def helper(cur, remain_zero):
            if cur == end and remain_zero == 0:
                self.res += 1
                return
            if cur == end or remain_zero == 0:
                return
            x, y = cur
            direction = {(0, 1), (1, 0), (-1, 0), (0, -1)}
            for dx, dy in direction:
                if 0 <= x+dx < num_row and 0 <= y+dy < num_col and grid[x+dx][y+dy] != -1:
                    grid[x+dx][y+dy] = -1
                    helper((x+dx, y+dy), remain_zero-1)
                    grid[x+dx][y+dy] = 0
                    
        helper(start, zero_cnt+1)
        return self.res
```
