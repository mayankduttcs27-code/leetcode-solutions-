class Solution:
    def shiftGrid(self, grid, k):
        m = len(grid)
        n = len(grid[0])
        total = m * n

        k %= total

        # Flatten the grid
        arr = []
        for row in grid:
            arr.extend(row)

        # Shift
        arr = arr[-k:] + arr[:-k]

        # Convert back to grid
        for i in range(m):
            for j in range(n):
                grid[i][j] = arr[i * n + j]

        return grid